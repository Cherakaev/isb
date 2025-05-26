import argparse
import sys

from key_worker import KeyWorker
from file_worker import FileWorker
from hybrid_system import HybridSystem


def parse_arguments() -> argparse.Namespace:
    """
    Function parses arguments from cmd
    :return: object with arguments
    """
    parser = argparse.ArgumentParser(
        description="Hybrid crypto system (RSA + Camillia)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    group = parser.add_mutually_exclusive_group(required = True)

    group.add_argument('-gen', '--generate', action='store_true',
                       help='Generate keys')
    group.add_argument('-enc', '--encrypt', action='store_true',
                       help='Encrypt file')
    group.add_argument('-dec', '--decrypt', action='store_true',
                       help='Decrypt file')

    parser.add_argument(
        '-c', '--config',
        type=str,
        default='settings.json',
        help='Path to JSON config file'
    )

    parser.add_argument(
        '-k', '--key-length',
        type=int,
        choices=[128, 192, 256],
        help='Key length (bits) for generation'
    )

    return parser.parse_args()

def main() :
    args = parse_arguments()

    try:
        settings = FileWorker.read_json(args.config)

        if args.generate:
            print("Keys generation..")

            public_key, private_key = KeyWorker.generate_rsa_keys()
            symmetric_key = KeyWorker.generate_camellia_key(
                args.key_length
            )
            encrypted_key = KeyWorker.encrypt_camellia_key(
                symmetric_key,
                public_key
            )

            FileWorker.serialize_private_key(
                private_key,
                settings["private_key"]
            )
            FileWorker.serialize_public_key(
                public_key,
                settings["public_key"]
            )
            FileWorker.write_txt(settings["symmetric_key"], encrypted_key)

            print("Keys have successfully saved")
        elif args.encrypt:
            print("Encryption..")

            symmetric_key = HybridSystem.decrypt_symmetric_key(
                settings["symmetric_key"],
                settings["private_key"]
            )

            HybridSystem.encrypt_file(
                settings["initial_file"],
                symmetric_key,
                settings["encrypted_file"]
            )

            print(f"Data saved to {settings['encrypted_file']}")
        else:
            print("Decryption..")

            symmetric_key = HybridSystem.decrypt_symmetric_key(
                settings["symmetric_key"],
                settings["private_key"]
            )

            HybridSystem.decrypt_file(
                settings["encrypted_file"],
                symmetric_key,
                settings["decrypted_file"]
            )

            print(f"Data saved to {settings['decrypted_file']}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)



if __name__ == '__main__':
    main()