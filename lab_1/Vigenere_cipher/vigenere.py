import json


def read_json(json_path: str) -> tuple:
    """
    Function read json file as a tuple with 3 elements
    :param json_path: path of file.json
    :return: tuple (key, alphabet, text_to_encrypt)
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            key = data['key']
            alphabet = data['alphabet']
            text_to_encrypt = data['text_to_encrypt']
        return key, alphabet, text_to_encrypt
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    except KeyError as e:
        raise KeyError(f"Missing required key in JSON: {e}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {json_path}")


def write_to_file(file_name: str, data: str) -> None:
    """
    Function writes string to file in directory with project
    :param file_name: the name of new file
    :param data: data to write
    :return: None
    """
    if not isinstance(data, str):
        raise ValueError("Data must be a string")

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


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
            raise ValueError(f"Bad key. Unallowable character: '{char}'")

    text = text.upper()
    key = key.upper()
    key_length = len(key)
    alphabet_length = len(alphabet)
    encrypted_text = ""

    for index, char in enumerate(text):
        if char in alphabet:
            key_char = key[index % key_length]
            char_shift = alphabet.find(char)
            key_shift = alphabet.find(key_char)
            new_index = (char_shift + key_shift) % alphabet_length
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text