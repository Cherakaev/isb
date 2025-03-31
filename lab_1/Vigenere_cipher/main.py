from Parser import get_arguments

from Vigenere import encrypt_text, read_json, write_to_file


def main():
    try:
        args = get_arguments()
        key, alphabet, text_to_encrypt = read_json(args.data_json)
        write_to_file("text_to_encrypt.txt", text_to_encrypt)
        write_to_file("key.txt", key)
        encrypted_text = encrypt_text(text_to_encrypt, key, alphabet)
        write_to_file("encrypted_text.txt", encrypted_text)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()