import argparse


def get_arguments() -> argparse.Namespace:
    """
    Function gets parameters from cmd
    :return: argparse.Namespace - simple argparse class which have parameters from cmd
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('json_path', type=str, help='print path to file.json')
    parser.add_argument('encrypted_text', type=str, help='print path to encrypted_text.txt')
    args = parser.parse_args()
    return args