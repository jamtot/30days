"""Bubble sorting a list, and outputting the amount of swaps."""

def bubble_sort(unsorted_list, size):
    """Sort a list and return it."""
    number_of_swaps = 0
    for _ in range(size):
        for j in range(size-1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                number_of_swaps += 1
        if number_of_swaps == 0:
            break
    print("Array is sorted in " + str(number_of_swaps) + " swaps.")
    return unsorted_list

if __name__ == "__main__":
    NUM = int(input().strip())
    LIST = list(map(int, input().strip().split(' ')))
    LIST = bubble_sort(LIST, NUM)

    print("First Element: " + str(LIST[0]))
    print("Last Element: " + str(LIST[-1]))
