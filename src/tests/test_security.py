import tempfile
import os
from osef.sdk.ecosystem.security import PluginSigner


def test_generate_keypair():
    priv, pub = PluginSigner.generate_keypair()
    assert b"PRIVATE KEY" in priv
    assert b"PUBLIC KEY" in pub


def test_sign_and_verify_file():
    priv, pub = PluginSigner.generate_keypair()

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"mock plugin data")
        temp_path = f.name

    try:
        signature = PluginSigner.sign_file(temp_path, priv)
        assert len(signature) == 64  # ed25519 signatures are 64 bytes

        # Verify valid signature
        assert PluginSigner.verify_file(temp_path, signature, pub) is True

        # Verify invalid signature
        invalid_sig = b"A" * 64
        assert PluginSigner.verify_file(temp_path, invalid_sig, pub) is False

        # Verify modified file
        with open(temp_path, "wb") as f2:
            f2.write(b"modified data")
        assert PluginSigner.verify_file(temp_path, signature, pub) is False

    finally:
        os.remove(temp_path)
