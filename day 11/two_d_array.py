"""Get the max sum of an hourglass in a 2D array.

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

The hourglasses are in the form:
1 1 1
  1
1 1 1
"""

def get_hour_glasses(arr, start_x, start_y):
    """Get an hourglass sum."""
    sum_hourglass = 0
    for i in range(3):
        for j in range(3):
            if j == 1:
                if i == 1:
                    sum_hourglass += arr[j+start_y][i+start_x]
            else:
                sum_hourglass += arr[j+start_y][i+start_x]
    return sum_hourglass

def get_max(arr):
    """Get the max hourglass sum from an array."""
    max_sum = -100
    for i in range(4):
        for j in range(4):
            cur = get_hour_glasses(arr, i, j)
            if max_sum < cur:
                max_sum = cur
    return max_sum

if __name__ == '__main__':
    ARR = []

    for _ in range(6):
        ARR.append(list(map(int, input().rstrip().split())))

    print(get_max(ARR))
