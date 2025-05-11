from file_work import read_json, read_txt, write_results
from nist import bit_frequency_test, consecutive_bits_test, long_sequence_test
from parser import get_arguments


def main():
    try:
        args = get_arguments()
        cpp_file, java_file, probabilities = read_json(args.data_json)
        cpp_sequence = read_txt(cpp_file)
        java_sequence = read_txt(java_file)
        frequency_cpp = bit_frequency_test(cpp_sequence)
        frequency_java = bit_frequency_test(java_sequence)
        consecutive_cpp = consecutive_bits_test(cpp_sequence)
        consecutive_java = consecutive_bits_test(java_sequence)
        long_cpp = long_sequence_test(cpp_sequence, probabilities)
        long_java = long_sequence_test(java_sequence, probabilities)
        write_results(frequency_cpp, frequency_java,  consecutive_cpp,
                      consecutive_java, long_cpp, long_java)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()