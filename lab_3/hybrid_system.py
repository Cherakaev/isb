import os

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from file_worker import FileWorker


class HybridSystem:
    @staticmethod
    def decrypt_symmetric_key(encrypted_key_path: str,
                          private_key_path: str) -> bytes:
        """
        Reads and decrypts symmetric key
        :param encrypted_key_path: path to file with key
        :param private_key_path: path to file with private key
        :return: decrypted symmetric key
        """
        encrypted_symmetric_key = FileWorker.read_txt(encrypted_key_path)
        private_key = FileWorker.deserialize_private_key(private_key_path)

        symmetric_key = private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            )
        )
        return symmetric_key

    @staticmethod
    def encrypt_file(initial_file_path: str,
                     symmetric_key: bytes,
                     encrypted_file_path: str) -> None:
        """
        Method encrypts file using RSA and symmetric key
        :param initial_file_path: file path to encrypt
        :param symmetric_key: already decrypted key
        :param encrypted_file_path: file path to save result
        :return: None
        """
        plaintext = FileWorker.read_txt(initial_file_path)

        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(symmetric_key),
                        modes.CBC(iv),
                        backend=default_backend())
        encryptor = cipher.encryptor()

        padder = sym_padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        FileWorker.write_txt(encrypted_file_path, iv+ciphertext)

    @staticmethod
    def decrypt_file(encrypted_file_path: str, symmetric_key: bytes,
                     decrypted_file_path: str) -> None:
        """
        Method encrypts file using RSA and symmetric key
        :param encrypted_file_path: file path with encrypted text
        :param symmetric_key: already decrypted key
        :param decrypted_file_path: file path to save result
        :return: None
        """
        data = FileWorker.read_txt(encrypted_file_path)

        iv = data[:16]
        ciphertext = data[16:]

        cipher = Cipher(
            algorithms.Camellia(symmetric_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()

        decrypted_padded = (decryptor.update(ciphertext) +
                            decryptor.finalize())

        unpadder = sym_padding.PKCS7(128).unpadder()
        decrypted_data = (unpadder.update(decrypted_padded)
                          + unpadder.finalize())

        FileWorker.write_txt(decrypted_file_path, decrypted_data)