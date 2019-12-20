"""Print an array in reverse."""

def reverse_array(array):
    """Take an array of ints and print it reversed."""
    reversed_array = ""
    for item in reversed(array):
        reversed_array += str(item) + " "
    print(reversed_array)

if __name__ == '__main__':
    _ = int(input())
    reverse_array(list(map(int, input().rstrip().split())))
