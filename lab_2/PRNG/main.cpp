#include <iostream>
#include <fstream>
#include <random>
#include <string>

using namespace std;

/**
 * @brief Generates a random binary sequence and saves it to a file.
 *
 * @param length The length of the binary sequence (number of bits).
 * @param file_path The path to the output file (default: "C++_sequence.txt").
 *
 * @note Uses `std::random_device` for randomness (cryptographically secure if available).
 * @warning If the file cannot be opened, an error message is printed, and the function returns early.
 *
 * @example
 * @code
 * generateBinarySequence(128); // Saves 128 random bits to "C++_sequence.txt"
 * generateBinarySequence(256, "output.txt"); // Saves to custom file
 * @endcode
 */
void generateBinarySequence(int length, const string& file_path = "C++_sequence.txt") {
	random_device rd;
	uniform_int_distribution<int> distrib(0, 1);

	ofstream out_file(file_path);
	if (!out_file) {
		cerr << "Error: cannot open the file " << file_path << endl;
		return;
	}

	for (int i = 0; i < length; ++i) {
		out_file << distrib(rd);
	}

	cout << "Binary sequence with " << length << " bits saved to file " << file_path << endl;
	out_file.close();
}

/**
 * @brief Main function demonstrating binary sequence generation.
 *
 * @return int Exit status (0 on success).
 *
 * @par Usage:
 * Generates a default 128-bit sequence and saves it to "C++_sequence.txt".
 */
int main() {
	int length = 128;
	generateBinarySequence(length);
	return 0;
}