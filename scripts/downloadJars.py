import os
import requests
import json
import shutil

MOJANG_VERSION_MANIFEST_URL = "https://piston-meta.mojang.com/mc/game/version_manifest.json"
JARS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../versions"))

def fetch_version_manifest():
    resp = requests.get(MOJANG_VERSION_MANIFEST_URL)
    resp.raise_for_status()
    return resp.json()

def get_release_versions(manifest):
    return [v for v in manifest["versions"] if v["type"] == "release"]

def fetch_version_metadata(version_url):
    resp = requests.get(version_url)
    resp.raise_for_status()
    return resp.json()

def download_server_jar(version_meta, dest_dir):
    server_info = version_meta.get("downloads", {}).get("server")
    if not server_info:
        print(f"No server jar info for {version_meta.get('id')}")
        return False
    url = server_info["url"]
    dest_path = os.path.join(dest_dir, "server.jar")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return True

def write_version_json(version_meta, dest_dir):
    json_path = os.path.join(dest_dir, f"{version_meta['id']}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(version_meta, f, indent=2)

def download_mojang_mappings(version_meta, dest_dir):
    server_mappings = version_meta.get("downloads", {}).get("server_mappings")
    if not server_mappings:
        print(f"No mappings available for {version_meta.get('id')} (probably very old version)")
        return False
    mappings_url = server_mappings["url"]
    mappings_dest = os.path.join(dest_dir, "mojang-mappings.txt")
    with requests.get(mappings_url, stream=True) as r:
        r.raise_for_status()
        with open(mappings_dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return True

def main():
    os.makedirs(JARS_DIR, exist_ok=True)
    manifest = fetch_version_manifest()
    release_versions = get_release_versions(manifest)

    for version in release_versions:
        version_id = version["id"]
        version_dir = os.path.join(JARS_DIR, version_id)
        jar_path = os.path.join(version_dir, "server.jar")
        json_path = os.path.join(version_dir, f"{version_id}.json")
        mappings_path = os.path.join(version_dir, "mojang-mappings.txt")
        os.makedirs(version_dir, exist_ok=True)

        version_meta = fetch_version_metadata(version["url"])
        write_version_json(version_meta, version_dir)

        if not os.path.isfile(jar_path):
            print(f"Downloading server jar for {version_id}...")
            try:
                if download_server_jar(version_meta, version_dir):
                    print(f"Downloaded server jar for {version_id} successfully.")
                else:
                    print(f"Failed to find server jar for {version_id}.")
            except Exception as e:
                shutil.rmtree(version_dir, ignore_errors=True)
                print(f"Failed to download {version_id} server jar: {e}")
                continue
        else:
            print(f"Skipping download for {version_id}, already downloaded jar.")

        if not os.path.isfile(mappings_path):
            print(f"Downloading mojang-mappings.txt for {version_id}...")
            try:
                if download_mojang_mappings(version_meta, version_dir):
                    print(f"Downloaded mojang-mappings.txt for {version_id} successfully.")
                else:
                    print(f"No mappings available for {version_id}.")
            except Exception as e:
                shutil.rmtree(version_dir, ignore_errors=True)
                print(f"Failed to download {version_id} mojang-mappings.txt: {e}")
        else:
            print(f"Skipping download for {version_id}, already downloaded mappings.")

if __name__ == "__main__":
    main()