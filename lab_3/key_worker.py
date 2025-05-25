from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey


class KeyWorker:
    @staticmethod
    def generate_rsa_keys(key_size: int = 2048) -> tuple[RSAPublicKey,
    RSAPrivateKey]:
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
            raise ValueError("Camellia key size must be 128, 192,"
                             " or 256 bits")
        camellia_key = get_random_bytes(key_size // 8)
        return camellia_key

    @staticmethod
    def encrypt_camellia_key(symmetric_key: bytes, public_key: RSAPublicKey) -> bytes:
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

    @staticmethod
    def serialize_public_key(public_key: RSAPublicKey,
                           public_key_path: str) -> None:
        """
        Method serialize rsa public key to .pem file
        :param public_key: key to serialize
        :param public_key_path: path to file to save key
        :return: None
        """
        if not public_key:
            raise ValueError("Keys are not provided")

        with open(public_key_path, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

    @staticmethod
    def serialize_private_key(private_key: RSAPrivateKey,
                              private_key_path: str) -> None:
        """
        Method serialize rsa private key to .pem file
        :param private_key: key to serialize
        :param private_key_path: path to file to save key
        :return: None
        """
        if not private_key:
            raise ValueError("Key is not provided")

        with open(private_key_path, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )