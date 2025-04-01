from collections import Counter


def analyze_frequency(text: str) -> list[tuple[str, float]]:
    """
    Function makes frequency analysis of given text.
    This function is used in make_key.
    :param text: text as a string
    :return: list of pairs char + frequency
    """
    if not text:
        raise ValueError("Input text cannot be empty for frequency analysis")

    counter = Counter(text)
    total = len(text)
    return sorted(
        [(char, count / total) for char, count in counter.items()],
        key=lambda x: x[1], reverse=True
    )


def make_key(encrypted_text: str, rus_frequency: dict[str, float]) \
        -> dict[str, str]:
    """
    Function makes key dictionary between text and statistic based on books
    :param encrypted_text: text
    :param rus_frequency: frequency for rus letters
    :return: key as a dictionary
    """
    encrypted_frequency = analyze_frequency(encrypted_text)
    sorted_russian = sorted(rus_frequency.items(), key=lambda x: x[1],
                            reverse=True)
    encryption_key = {}
    for (key1, _), (key2, _) in zip(encrypted_frequency, sorted_russian):
        encryption_key[key1] = key2
    return encryption_key


def decrypt_text(encrypted_text: str, encryption_key: dict[str, str]) -> str:
    """
    Function decrypt text by using encryption key
    :param encrypted_text: text to encrypt
    :param encryption_key: key to replace letters
    :return: text as a string
    """
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_text += encryption_key.get(char, char)
    return decrypted_text