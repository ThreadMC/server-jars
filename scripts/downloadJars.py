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
    data = resp.json()
    return data

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

        if not os.path.isfile(mappings_path):
            print(f"Downloading mappings for {log_version}...")
            mojang_version_info = get_mojang_version_info(mojang_manifest, version)
            if mojang_version_info:
                success = download_mojang_mappings(mojang_version_info, version_dir)
                if success:
                    print(f"Downloaded mappings for {log_version} successfully.")
                else:
                    print(f"No mappings available for {log_version}.")
            else:
                print(f"Version {log_version} not found in Mojang manifest (snapshot or invalid version?).")
        else:
            print(f"Skipping mappings download for {log_version}, already exists.")

if __name__ == "__main__":
    main()