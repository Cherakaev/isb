import json
import random


with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


key = data['key']
alphabet = data['alphabet']
text_to_encrypt = data['text_to_encrypt']


def encrypt_text(text: str, key: str, alphabet: str) -> str:
    """
    Function uses vigenere cipher
    :param text: text to encrypt
    :param key: key for cipher
    :param alphabet: alphabet for text
    :return: encrypted text
    """

    for char in key:
        if char not in alphabet:
            raise ValueError(f"Некорректный ключ. Недопустимый символ: '{char}'")

    text = text.upper()
    key = key.upper()
    key_length = len(key)
    alphabet_length = len(alphabet)
    encrypted_text = ""

    for char, index in enumerate(text):
        if char in alphabet:
            key_char = key[index % key_length]
            char_shift = alphabet.find(char)
            key_shift = alphabet.find(key_char)
            new_index = (char_shift + key_shift) % alphabet_length
            encrypted_text += alphabet[new_index]
        else:
            encrypt_text += char
    return encrypted_text
