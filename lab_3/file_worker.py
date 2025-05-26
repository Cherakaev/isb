import json

from typing import Dict
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import (
    RSAPublicKey,
    RSAPrivateKey
)


class FileWorker:
    @staticmethod
    def read_json(json_path: str) -> Dict[str, str]:
        """
        Method read json file as a dict with requirements
        :param json_path: path of file.json
        :return: dictionary
        """
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {json_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {json_path}")

    @staticmethod
    def read_txt(txt_path: str) -> bytes:
        """
        Method reads file as a string
        :param txt_path: path of file.txt
        :return: text as str
        """
        try:
            with open(txt_path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {txt_path}")

    @staticmethod
    def write_txt(file_path: str, text: bytes) -> None:
        """
        Writes down text to the file
        :param file_path: file path to write
        :param text: text to write
        :return: None
        """
        try:
            with open(file_path, 'wb') as file:
                file.write(text)
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    @staticmethod
    def serialize_public_key(public_key: RSAPublicKey,
                             public_key_path: str) -> None:
        """
        Method serializes rsa public key to .pem file
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
        try:
            with open(private_key_path, "wb") as f:
                f.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
        except Exception as e:
            raise IOError(f"Failed to serialize private key: {str(e)}")

    @staticmethod
    def deserialize_private_key(private_key_path: str) -> RSAPrivateKey:
        """
        Method deserialize rsa private key from .pem file
        :param private_key_path: path to file with key
        :return: private key as class RSA
        """
        if not private_key_path:
            raise ValueError("Key file path cannot be empty")

        try:
            with open(private_key_path, 'rb') as f:
                private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None
                )

            if not isinstance(private_key, RSAPrivateKey):
                raise ValueError("The file does not contain a valid "
                                 "RSA private key")

            return private_key

        except Exception as e:
            raise IOError(f"Failed to deserialize private key: {str(e)}")

    @staticmethod
    def deserialize_public_key(public_key_path: str) -> RSAPublicKey:
        """
        Method deserialize rsa public key from .pem file
        :param public_key_path: path to file with key
        :return: public key as class RSA
        """
        if not public_key_path:
            raise ValueError("Key file path cannot be empty")

        try:
            with open(public_key_path, 'rb') as f:
                public_key = serialization.load_pem_public_key(
                    f.read(),
                )

            if not isinstance(public_key, RSAPublicKey):
                raise ValueError("The file does not contain a valid "
                                 "RSA public key")

            return public_key

        except Exception as e:
            raise IOError(f"Failed to deserialize public key: {str(e)}")