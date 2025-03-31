import json


def read_json(json_path: str) -> dict[str, float]:
    """
    Function read json file as a dictionary
    :param json_path: path of file.json
    :return: dictionary with russian letters frequency
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {json_path}")


def read_encrypted_text(file_path: str) -> str:
    """
    Function reads file into string
    :param file_path: path to file
    :return: string text
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Encrypted_text file not found: {file_path}")


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