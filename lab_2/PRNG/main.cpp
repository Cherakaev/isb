#include <iostream>
#include <fstream>
#include <random>
#include <string>


using namespace std;


void generateBinarySequence(int length, const string& file_path = "C++_sequence.txt")
{
	random_device rd;
	uniform_int_distribution<int> distrib(0, 1);

	ofstream out_file(file_path);
	if (!out_file) {
		cerr << "Error: cannot open the file " << file_path << endl;
		return;
	}

	for (size_t i = 0; i < length; ++i)
	{
		 out_file << (distrib(rd));
	}

	cout << "Binary sequence with " << length << " bits saved to file " << file_path << endl;
	out_file.close();
}

int main()
{
	int length = 128;
	generateBinarySequence(length);

	return 0;
}