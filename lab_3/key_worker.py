from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.rsa import (
    RSAPublicKey,
    RSAPrivateKey
)


class KeyWorker:
    @staticmethod
    def generate_rsa_keys(
            key_size: int = 2048
    ) -> tuple[RSAPublicKey, RSAPrivateKey]:
        """
        Method generates public and private rsa keys
        :param key_size: length for module in Euler function
        :return: tuple with public and private rsa keys
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )
        public_key = private_key.public_key()
        return public_key, private_key

    @staticmethod
    def generate_camellia_key(key_size: int = 256) -> bytes:
        """
        Method generates random string of bytes to use in Camellia cipher
        :param key_size: Length of the key (128, 192, 256)
        :return: return key as string of bytes
        """
        if key_size not in [128, 192, 256]:
            raise ValueError(
                "Camellia key size must be 128, 192, or 256 bits"
            )
        camellia_key = get_random_bytes(key_size // 8)
        return camellia_key

    @staticmethod
    def encrypt_camellia_key(
            symmetric_key: bytes,
            public_key: RSAPublicKey
    ) -> bytes:
        """
        Method encrypt symmetric key by using public key
        :param symmetric_key: symmetric key to encrypt
        :param public_key: rsa public key
        :return: encrypted symmetric key as string of bytes
        """
        if not symmetric_key:
            raise ValueError("Camellia key not provided.")

        encrypted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            )
        )
        return encrypted_key