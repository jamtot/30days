"""Find the binary for a decimal number, then print the number of consecutive 1s."""


def get_binary(int_n):
    """Convert num to binary."""
    binary = list()
    while int_n > 0:
        binary.append(str(int_n%2))
        int_n = int(int_n/2)
    bin_num = ''.join(reversed(binary))
    print(bin_num)
    return bin_num

def consecutive_ones(binary_number):
    """Return how many 1's happen in a row."""
    max_consec = 0
    cur_count = 0
    for cur_b in binary_number:
        if cur_b == '1':
            cur_count += 1
            if max_consec < cur_count:
                max_consec = cur_count
        else:
            cur_count = 0

    return max_consec

if __name__ == '__main__':
    BIN_NUM = get_binary(int(input()))
    print(consecutive_ones(BIN_NUM))
