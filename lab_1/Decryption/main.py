from Decryption import decrypt_text, make_key
from file_work import read_encrypted_text, read_json, write_to_file
from Parser import get_arguments


def main():
    try:
        args = get_arguments()
        rus_frequency = read_json(args.json_path)
        encrypted_text = read_encrypted_text(args.encrypted_text)
        key = make_key(encrypted_text, rus_frequency)
        decrypted_text = decrypt_text(encrypted_text, key)
        write_to_file('decrypted_text.txt', decrypted_text)
        write_to_file('key.txt', str(key))
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()