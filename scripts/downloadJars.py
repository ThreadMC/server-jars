import os
import requests
import json
import shutil

API_VERSIONS_URL = "https://mcutils.com/api/server-jars/vanilla"
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

def main():
    os.makedirs(JARS_DIR, exist_ok=True)
    versions_data = fetch_versions()
    for version_data in versions_data:
        version = version_data["version"]
        version_dir = os.path.join(JARS_DIR, version)
        jar_path = os.path.join(version_dir, "server.jar")
        json_path = os.path.join(version_dir, f"{version}.json")
        os.makedirs(version_dir, exist_ok=True)
        detailed_version_data = fetch_version_data(version)
        write_version_json(detailed_version_data, version_dir)
        log_version = format_version_for_log(version)
        if os.path.isfile(jar_path):
            print(f"Skipping download for {log_version}, already downloaded jar. JSON updated.")
            continue
        print(f"Downloading {log_version}...")
        try:
            download_jar(version, version_dir)
            print(f"Downloaded {log_version} successfully.")
        except Exception as e:
            shutil.rmtree(version_dir, ignore_errors=True)
            print(f"Failed to download {log_version}: {e}")

if __name__ == "__main__":
    main()