from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature


class PluginSigner:
    """
    Handles cryptographic signing and verification of OSEF Plugins using ed25519.
    """

    @staticmethod
    def generate_keypair() -> Tuple[bytes, bytes]:
        """
        Generates a new ed25519 keypair.
        Returns:
            Tuple[bytes, bytes]: (private_key_pem, public_key_pem)
        """
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()

        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        public_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        return private_bytes, public_bytes

    @staticmethod
    def sign_file(file_path: str, private_key_pem: bytes) -> bytes:
        """
        Signs the contents of a file using the provided private key.
        """
        private_key = serialization.load_pem_private_key(private_key_pem, password=None)
        if not isinstance(private_key, ed25519.Ed25519PrivateKey):
            raise ValueError("Private key must be an ed25519 key")

        with open(file_path, "rb") as f:
            data = f.read()

        signature = private_key.sign(data)
        return signature

    @staticmethod
    def verify_file(file_path: str, signature: bytes, public_key_pem: bytes) -> bool:
        """
        Verifies the signature of a file using the provided public key.
        """
        try:
            public_key = serialization.load_pem_public_key(public_key_pem)
            if not isinstance(public_key, ed25519.Ed25519PublicKey):
                raise ValueError("Public key must be an ed25519 key")

            with open(file_path, "rb") as f:
                data = f.read()

            public_key.verify(signature, data)
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            raise ValueError(f"Signature verification failed: {e}")
