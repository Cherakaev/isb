import math

from scipy.special.cython_special import gammainc


def bit_frequency_test(sequence: str) -> float:
    """
    The function performs a bit-frequency test on a random generated sequence
    :param sequence: random generated binary sequence
    :return: p_value
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be string")

    if len(sequence) == 0:
        raise ValueError("Void string")

    if not all(c in ('0', '1') for c in sequence):
        raise ValueError("String must include only '0' and '1'")


    sum_bits = sum(1 if b == '1' else -1 for b in sequence)
    normalized_sum = abs(sum_bits) / math.sqrt(len(sequence))
    return math.erfc(normalized_sum / math.sqrt(2))


def consecutive_bits_test(sequence: str) -> float:
    """
    The function performs a test for identical consecutive bits on a random
    generated sequence
    :param sequence: random generated binary sequence
    :return: p_value
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be string")

    if len(sequence) == 0:
        raise ValueError("Void string")

    if not all(c in ('0', '1') for c in sequence):
        raise ValueError("String must include only '0' and '1'")

    length = len(sequence)
    if length < 2:
        raise ValueError("Sequence length must be at least 2 bits")

    ones_count = sum(1 for b in sequence if b == '1')
    proportion_ones = ones_count / length

    if abs(proportion_ones - 0.5) >= 2 / math.sqrt(length):
        return 0.0

    alternations = sum(1 for i in range(length - 1) if sequence[i]
                       != sequence[i + 1])

    numerator = abs(alternations - 2 * length * proportion_ones *
                    (1 - proportion_ones))
    denominator = (2 * math.sqrt(2 * length) * proportion_ones *
                   (1 - proportion_ones))

    return math.erfc(numerator / denominator)


def long_sequence_test(sequence: str, probabilities: list[float], block_size: int = 8) -> float:
    """
    The function performs the longest sequence of ones in a block
    test on a random generated sequence
    :param sequence: random generated binary sequence
    :param probabilities: list with Pi probabilities
    :param block_size: size of a block (default 8)
    :return: p_value
    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be string")

    if len(sequence) == 0:
        raise ValueError("Void string")

    if not all(c in ('0', '1') for c in sequence):
        raise ValueError("String must include only '0' and '1'")

    length = len(sequence)
    if length % block_size != 0:
        raise ValueError("Length must be a multiple of the block size")

    num_blocks = length // block_size
    max_lengths = [0, 0, 0, 0]
    for i in range(num_blocks):
        block = sequence[i * block_size: (i + 1) * block_size]
        max_len = 0
        current_len = 0

        for bit in block:
            if bit == '1':
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0

        match max_len:
            case 0 | 1:
                max_lengths[0] += 1
            case 2:
                max_lengths[1] += 1
            case 3:
                max_lengths[2] += 1
            case _:
                max_lengths[3] += 1

    chi_square = sum((max_lengths[i] - num_blocks * probabilities[i]) ** 2 /
                     num_blocks * probabilities[i] for i in range (4))
    return gammainc(1.5, chi_square / 2)