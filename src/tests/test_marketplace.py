import pytest
import os
import tempfile
import tarfile
from unittest.mock import patch, MagicMock
from osef.sdk.ecosystem.marketplace import MarketplaceClient
from osef.sdk.ecosystem.security import PluginSigner


def test_marketplace_client_search():
    client = MarketplaceClient("http://mock-index.json")
    client.index_data = {
        "plugins": [
            {"name": "test-plugin", "description": "A test plugin"},
            {"name": "other-plugin", "description": "Another one"},
        ]
    }

    # Bypass fetch_index
    with patch.object(client, "fetch_index"):
        results = client.search("test")
        assert len(results) == 1
        assert results[0]["name"] == "test-plugin"


def test_install_plugin_with_signature():
    client = MarketplaceClient("http://mock-index.json")

    # Create keypair
    priv, pub = PluginSigner.generate_keypair()

    # Create mock tar.gz
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tar.gz") as f:
        with tarfile.open(fileobj=f, mode="w:gz") as tar:
            # Just create an empty tar
            pass
        tar_path = f.name

    try:
        # Sign it
        signature = PluginSigner.sign_file(tar_path, priv)
        signature_hex = signature.hex()

        # Read the mock tar to bytes
        with open(tar_path, "rb") as f:
            tar_bytes = f.read()

        client.index_data = {
            "plugins": [
                {
                    "name": "secure-plugin",
                    "download_url": "http://download.com/plugin.tar.gz",
                    "signature": signature_hex,
                }
            ]
        }

        # Mock httpx.get to return tar_bytes
        mock_response = MagicMock()
        mock_response.content = tar_bytes
        mock_response.raise_for_status = MagicMock()

        with patch("httpx.get", return_value=mock_response):
            with patch.object(client, "fetch_index"):
                with tempfile.TemporaryDirectory() as target_dir:
                    plugin_dir = client.install_plugin("secure-plugin", target_dir, pub)
                    assert os.path.exists(plugin_dir)

        # Now try with bad signature
        client.index_data["plugins"][0]["signature"] = "00" * 64
        with patch("httpx.get", return_value=mock_response):
            with patch.object(client, "fetch_index"):
                with tempfile.TemporaryDirectory() as target_dir:
                    with pytest.raises(
                        ValueError, match="Signature verification failed"
                    ):
                        client.install_plugin("secure-plugin", target_dir, pub)

    finally:
        os.remove(tar_path)
