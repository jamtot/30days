"""Get the fine on a returned library book."""

def get_fine(expected, returned):
    """Use layered logic to find the fine due."""
    if expected[2] < returned[2]:#pylint:disable=no-else-return
        return 10000
    elif expected[2] > returned[2] or (expected[0] >= returned[0] and expected[1] >= returned[1]):
        return 0
    elif expected[0] < returned[0] and expected[1] == returned[1]:
        return 15 * (returned[0] - expected[0])
    return 500 * (returned[1] - expected[1])

if __name__ == "__main__":
    RETURNED = [int(num) for num in input().split()]
    EXPECTED = [int(num) for num in input().split()]
    print(get_fine(EXPECTED, RETURNED))
