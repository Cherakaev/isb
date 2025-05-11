import java.security.SecureRandom;

public class BinarySequenceGenerator {
    public static void main(String[] args) {
        int length = 128;
        String binarySequence = generateRandomBinarySequence(length);
        System.out.println("Binary sequence " + binarySequence);
    }

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