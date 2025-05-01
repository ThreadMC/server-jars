import os
import requests
import json
import shutil

API_VERSIONS_URL = "https://mcutils.com/api/server-jars/vanilla"
MOJANG_VERSION_MANIFEST_URL = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
JARS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../versions"))

def fetch_versions():
    resp = requests.get(API_VERSIONS_URL)
    resp.raise_for_status()
    return resp.json()

def fetch_version_data(version):
    url = f"{API_VERSIONS_URL}/{version}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def download_jar(version, dest_dir):
    url = f"https://mcutils.com/api/server-jars/vanilla/{version}/download"
    dest_path = os.path.join(dest_dir, "server.jar")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def write_version_json(version_data, dest_dir):
    minimal_data = {
        "version": version_data.get("version"),
        "release": version_data.get("release")
    }
    json_path = os.path.join(dest_dir, f"{version_data['version']}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(minimal_data, f, indent=2)

def format_version_for_log(version):
    parts = version.split('.')
    if len(parts) == 2:
        return f"{version}.0"
    return version

def fetch_mojang_version_manifest():
    resp = requests.get(MOJANG_VERSION_MANIFEST_URL)
    resp.raise_for_status()
    return resp.json()

def get_mojang_version_info(manifest, version):
    for v in manifest["versions"]:
        if v["id"] == version:
            return v
    return None

def download_mojang_mappings(version_info, dest_dir):
    resp = requests.get(version_info["url"])
    resp.raise_for_status()
    version_data = resp.json()

    client_mappings = version_data.get("downloads", {}).get("client_mappings")
    if not client_mappings:
        print(f"No mappings available for {version_info['id']} (probably very old version)")
        return False

    mappings_url = client_mappings["url"]
    mappings_dest = os.path.join(dest_dir, "mojang-mappings.tiny")

    with requests.get(mappings_url, stream=True) as r:
        r.raise_for_status()
        with open(mappings_dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return True

def is_tiny_v2_format(mapping_file_path):
    """Check if mapping file is Tiny v2 by reading the first line"""
    try:
        with open(mapping_file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            return first_line.startswith('tiny') and '2' in first_line.split('\t')[0]
    except Exception as e:
        print(f"Failed to check format of {mapping_file_path}: {e}")
        return False

def convert_mappings_to_tiny_v2(mapping_file_path):
    """Converts a Mojang mapping file (ProGuard format) to Tiny v2 format and skips duplicates (classes, methods, fields)"""
    try:
        with open(mapping_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        tiny_lines = []
        tiny_lines.append('tiny\t2\t0\tofficial\tnamed\n')

        current_class = None
        seen_class_obfuscated_names = set()
        seen_method_mappings = dict()  # { class_name: set((descriptor, obf_name)) }
        seen_field_mappings = dict()   # { class_name: set((field_name, obf_name)) }

        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if '->' in line and not line.startswith('    '):
                # Class mapping
                parts = line.split('->')
                original = parts[0].strip()
                obf = parts[1].replace(':', '').strip()

                if obf in seen_class_obfuscated_names:
                    # Skip duplicate obfuscated class target
                    continue
                seen_class_obfuscated_names.add(obf)

                tiny_lines.append(f'c\t{original}\t{obf}\n')
                current_class = original
                seen_method_mappings[current_class] = set()
                seen_field_mappings[current_class] = set()

            elif line.startswith('    ') and current_class:
                parts = line.strip().split(' ')
                if len(parts) >= 2 and '->' in parts[-1]:
                    arrow_index = parts.index('->')
                    type_sig = ' '.join(parts[:arrow_index])
                    name = parts[arrow_index - 1]
                    obf_name = parts[-1]

                    if '(' in type_sig:  # method
                        descriptor = type_sig
                        key = (descriptor, obf_name)
                        if key in seen_method_mappings[current_class]:
                            continue
                        seen_method_mappings[current_class].add(key)

                        tiny_lines.append(f'm\t{current_class}\t{descriptor}\t{name}\t{obf_name}\n')
                    else:  # field
                        descriptor = type_sig
                        key = (name, obf_name)
                        if key in seen_field_mappings[current_class]:
                            continue
                        seen_field_mappings[current_class].add(key)

                        tiny_lines.append(f'f\t{current_class}\t{descriptor}\t{name}\t{obf_name}\n')

        with open(mapping_file_path, 'w', encoding='utf-8') as f:
            f.writelines(tiny_lines)

        print(f"Converted {os.path.basename(mapping_file_path)} to Tiny v2 format successfully (duplicates skipped).")

    except Exception as e:
        print(f"Failed to convert {mapping_file_path} to Tiny v2: {e}")

def ensure_mappings_are_tiny_v2(mappings_path, version, mojang_manifest, version_dir):
    """Ensure mappings are present and in Tiny v2 format"""
    if not os.path.isfile(mappings_path):
        print(f"Downloading mappings for {version}...")
        mojang_version_info = get_mojang_version_info(mojang_manifest, version)
        if mojang_version_info:
            success = download_mojang_mappings(mojang_version_info, version_dir)
            if success:
                print(f"Downloaded mappings for {version} successfully.")
        else:
            print(f"Version {version} not found in Mojang manifest (snapshot or invalid version?).")

    if os.path.isfile(mappings_path):
        if not is_tiny_v2_format(mappings_path):
            print(f"Converting mappings for {version} to Tiny v2 format...")
            convert_mappings_to_tiny_v2(mappings_path)
        else:
            print(f"Mappings for {version} already in Tiny v2 format, skipping conversion.")

def main():
    os.makedirs(JARS_DIR, exist_ok=True)
    versions_data = fetch_versions()
    mojang_manifest = fetch_mojang_version_manifest()

    for version_data in versions_data:
        version = version_data["version"]
        version_dir = os.path.join(JARS_DIR, version)
        jar_path = os.path.join(version_dir, "server.jar")
        json_path = os.path.join(version_dir, f"{version}.json")
        mappings_path = os.path.join(version_dir, "mojang-mappings.tiny")
        os.makedirs(version_dir, exist_ok=True)

        detailed_version_data = fetch_version_data(version)
        write_version_json(detailed_version_data, version_dir)

        log_version = format_version_for_log(version)

        if not os.path.isfile(jar_path):
            print(f"Downloading server jar for {log_version}...")
            try:
                download_jar(version, version_dir)
                print(f"Downloaded server jar for {log_version} successfully.")
            except Exception as e:
                shutil.rmtree(version_dir, ignore_errors=True)
                print(f"Failed to download {log_version} server jar: {e}")
                continue
        else:
            print(f"Skipping download for {log_version}, already downloaded jar.")

        ensure_mappings_are_tiny_v2(mappings_path, log_version, mojang_manifest, version_dir)

if __name__ == "__main__":
    main()