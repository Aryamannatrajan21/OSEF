import httpx
import tempfile
import tarfile
import os
from typing import Dict, Any, Optional
from osef.sdk.ecosystem.security import PluginSigner


class MarketplaceClient:
    def __init__(self, index_url: str):
        self.index_url = index_url
        self.index_data: Dict[str, Any] = {}

    def fetch_index(self) -> None:
        """Fetches the marketplace index."""
        try:
            response = httpx.get(self.index_url, follow_redirects=True)
            response.raise_for_status()
            self.index_data = response.json()
        except Exception as e:
            raise ValueError(f"Failed to fetch marketplace index: {e}")

    def get_plugin_info(self, plugin_name: str) -> Optional[Dict[str, Any]]:
        """Returns plugin information from the index if available."""
        if not self.index_data:
            self.fetch_index()

        from typing import cast

        plugins = self.index_data.get("plugins", [])
        for plugin in plugins:
            if plugin.get("name") == plugin_name:
                return cast(Dict[str, Any], plugin)
        return None

    def search(self, query: str) -> list[Dict[str, Any]]:
        """Searches for plugins in the index matching the query."""
        if not self.index_data:
            self.fetch_index()

        query = query.lower()
        results = []
        for plugin in self.index_data.get("plugins", []):
            if (
                query in plugin.get("name", "").lower()
                or query in plugin.get("description", "").lower()
            ):
                results.append(plugin)
        return results

    def install_plugin(
        self,
        plugin_name: str,
        target_dir: str,
        trusted_public_key_pem: Optional[bytes] = None,
    ) -> str:
        """
        Downloads, verifies, and extracts a plugin.
        Returns the path to the extracted plugin directory.
        """
        plugin_info = self.get_plugin_info(plugin_name)
        if not plugin_info:
            raise ValueError(f"Plugin {plugin_name} not found in marketplace.")

        download_url = plugin_info.get("download_url")
        signature_hex = plugin_info.get("signature")

        if not download_url:
            raise ValueError(f"Plugin {plugin_name} has no download URL.")

        if trusted_public_key_pem and not signature_hex:
            raise ValueError(
                f"Plugin {plugin_name} is not signed, but verification is required."
            )

        try:
            # Download the tar.gz file
            response = httpx.get(download_url, follow_redirects=True)
            response.raise_for_status()

            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".tar.gz"
            ) as temp_file:
                temp_file.write(response.content)
                temp_file_path = temp_file.name

            # Verify signature if required
            if trusted_public_key_pem and signature_hex:
                signature_bytes = bytes.fromhex(signature_hex)
                is_valid = PluginSigner.verify_file(
                    temp_file_path, signature_bytes, trusted_public_key_pem
                )
                if not is_valid:
                    os.remove(temp_file_path)
                    raise ValueError(
                        f"Signature verification failed for plugin {plugin_name}."
                    )

            # Extract the plugin
            plugin_dir = os.path.join(target_dir, plugin_name)
            os.makedirs(plugin_dir, exist_ok=True)

            with tarfile.open(temp_file_path, "r:gz") as tar:
                tar.extractall(path=plugin_dir)

            return plugin_dir

        except Exception as e:
            raise ValueError(f"Failed to install plugin {plugin_name}: {e}")
        finally:
            if "temp_file_path" in locals() and os.path.exists(temp_file_path):
                os.remove(temp_file_path)
