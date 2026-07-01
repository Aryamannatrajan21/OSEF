import os
import json
import tarfile
from pathlib import Path
from osef.sdk.ecosystem.security import PluginSigner


def main():
    # Setup paths
    project_root = Path(
        os.environ.get("GITHUB_WORKSPACE", Path(__file__).parent.parent)
    )
    plugins_dir = project_root / "reference-plugins"
    packages_dir = project_root / "packages"
    index_path = project_root / "marketplace-index.json"

    # Read private key from env
    priv_pem_str = os.environ.get("OSEF_PLUGIN_PRIVATE_KEY")
    if not priv_pem_str:
        raise ValueError("OSEF_PLUGIN_PRIVATE_KEY environment variable is not set")
    priv_pem = priv_pem_str.encode("utf-8")

    packages_dir.mkdir(parents=True, exist_ok=True)
    index_data = {"plugins": []}

    for plugin_path in plugins_dir.iterdir():
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
                except Exception as e:
                    print(f"Warning: Failed to parse manifest for {name}: {e}")

        # Create tar.gz
        tar_name = f"{name}-{version}.tar.gz"
        tar_path = packages_dir / tar_name

        print(f"Packaging {name}...")

        def filter_func(tarinfo):
            if any(
                x in tarinfo.name
                for x in [".venv", "__pycache__", ".pytest_cache", ".git"]
            ):
                return None
            return tarinfo

        with tarfile.open(tar_path, "w:gz") as tar:
            tar.add(plugin_path, arcname=name, filter=filter_func)

        # Sign it
        print(f"Signing {name}...")
        signature = PluginSigner.sign_file(str(tar_path), priv_pem)

        # Add to index
        index_data["plugins"].append(
            {
                "name": name,
                "version": version,
                "description": description,
                "download_url": f"https://github.com/Aryamannatrajan21/OSEF/releases/download/plugins-latest/{tar_name}",
                "signature": signature.hex(),
            }
        )

    with open(index_path, "w") as f:
        json.dump(index_data, f, indent=2)

    print(f"Marketplace built with {len(index_data['plugins'])} plugins!")


if __name__ == "__main__":
    main()
# Trigger workflow
