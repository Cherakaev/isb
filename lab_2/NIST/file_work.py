import json


def read_json(json_path: str) -> tuple:
    """
    Function read json file as a tuple with 3 elements
    :param json_path: path of file.json
    :return: tuple (cpp_file, java_file, probabilities)
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            cpp_file = data['cpp_file']
            java_file = data['java_file']
            probabilities = data['probabilities']
        return cpp_file, java_file, probabilities
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    except KeyError as e:
        raise KeyError(f"Missing required key in JSON: {e}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {json_path}")


def read_txt(txt_path: str) -> str:
    """
    Function reads file as a string
    :param txt_path: path of file.txt
    :return: text as str
    """
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f"TXT file not found: {txt_path}")


def write_results(frequency_cpp: float, frequency_java: float,
                  consecutive_cpp: float, consecutive_java: float,
                  long_cpp:float, long_java: float, file_name: str = "results.txt") -> None:
    """
    Function writes results into results.txt
    :param frequency_cpp: p_value for frequency test for cpp
    :param frequency_java: p_value for frequency test for java
    :param consecutive_cpp: p_value for consecutive test for cpp
    :param consecutive_java: p_value for consecutive test for java
    :param long_cpp: p_value for long test for cpp
    :param long_java: p_value for long test for java
    :param file_name: name of file to save results
    :return: None
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(
                "Test results:\n\n"
                f"1. Bit frequency test:\n"
                f"   C++: {frequency_cpp:.6f}\n"
                f"   Java: {frequency_java:.6f}\n\n"
                f"2. Test for identical consecutive bits:\n"
                f"   C++: {consecutive_cpp:.6f}\n"
                f"   Java: {consecutive_java:.6f}\n\n"
                f"3. Longest sequence of ones in a block test:\n"
                f"   C++: {long_cpp:.6f}\n"
                f"   Java: {long_java:.6f}\n"
            )

    except PermissionError:
        print(f"Error: acces denied to write to file {file_name}")