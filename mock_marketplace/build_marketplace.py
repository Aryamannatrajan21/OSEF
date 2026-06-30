import json
import tarfile
from pathlib import Path
from osef.sdk.ecosystem.security import PluginSigner

PROJECT_ROOT = Path("/Users/macair/Documents/OSEF")
PLUGINS_DIR = PROJECT_ROOT / "reference-plugins"
MARKETPLACE_DIR = PROJECT_ROOT / "mock_marketplace"
PACKAGES_DIR = MARKETPLACE_DIR / "packages"
INDEX_PATH = MARKETPLACE_DIR / "marketplace-index.json"
PRIVATE_KEY_PATH = MARKETPLACE_DIR / "plugin_private_key.pem"

def main():
    PACKAGES_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(PRIVATE_KEY_PATH, "rb") as f:
        priv_pem = f.read()

    index_data = {"plugins": []}

    # Find all plugins (they usually have a plugin_manifest.json, or at least a src/ directory)
    for plugin_path in PLUGINS_DIR.iterdir():
        if not plugin_path.is_dir():
            continue
            
        manifest_path = plugin_path / "plugin_manifest.json"
        
        name = plugin_path.name
        description = f"{name} plugin for OSEF"
        version = "1.0.0"
        
        if manifest_path.exists():
            with open(manifest_path, "r") as f:
                try:
                    manifest = json.load(f)
                    description = manifest.get("description", description)
                    version = manifest.get("version", version)
                    name = manifest.get("name", name)
                except:
                    pass

        # Create tar.gz
        tar_name = f"{name}-{version}.tar.gz"
        tar_path = PACKAGES_DIR / tar_name
        
        print(f"Packaging {name}...")
        # Exclude .venv, __pycache__, .pytest_cache
        def filter_func(tarinfo):
            if any(x in tarinfo.name for x in ['.venv', '__pycache__', '.pytest_cache', '.git']):
                return None
            return tarinfo
            
        with tarfile.open(tar_path, "w:gz") as tar:
            tar.add(plugin_path, arcname=name, filter=filter_func)
            
        # Sign it
        print(f"Signing {name}...")
        signature = PluginSigner.sign_file(str(tar_path), priv_pem)
        
        # Add to index
        index_data["plugins"].append({
            "name": name,
            "version": version,
            "description": description,
            "download_url": f"http://127.0.0.1:8000/packages/{tar_name}",
            "signature": signature.hex()
        })
        
    # Also add the mock-plugin and soc2 compliance pack if we want
    # We will just write the new index
    with open(INDEX_PATH, "w") as f:
        json.dump(index_data, f, indent=2)
        
    print(f"Marketplace built with {len(index_data['plugins'])} plugins!")

if __name__ == "__main__":
    main()
