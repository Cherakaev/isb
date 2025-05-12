import java.security.SecureRandom;

/**
 * Generate random binary sequences
 */
public class BinarySequenceGenerator {
    /**
     * Main method to demonstrate binary sequence generation
     * Generates a binary sequence of default length (128) and prints it
     * 
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int length = 128;
        String binarySequence = generateRandomBinarySequence(length);
        System.out.println("Binary sequence: " + binarySequence);
    }

    /**
     * Generates a random binary sequence
     * 
     * @param length The length of sequence
     * @return A random binary string
     * @throws IllegalArgumentException If length is not positive number
     * @throws NullPointerException If the input is null
     */
    public static String generateRandomBinarySequence(int length) {
        if (length <= 0) {
            throw new IllegalArgumentException("Length must be positive number");
        }

        SecureRandom random = new SecureRandom();
        StringBuilder binaryString = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2);
            binaryString.append(bit);
        }

        return binaryString.toString();
    }
}