import argparse


def get_arguments() -> argparse.Namespace:
    """
    Function gets parameters from cmd
    :return: argparse.Namespace - simple argparse class which have parameters from cmd
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('data_json', type=str, help='print path to file.json')
    args = parser.parse_args()
    return args