"""Get largest absolute difference between 2 numbers in a list.

Also exploring scope.
"""

class Difference: # pylint: disable=too-few-public-methods
    """Hold elements and max difference, and a function to compute difference."""

    def __init__(self, a):
        """Initialise the __elements list and maximumDifference."""
        self.__elements = a
        self.maximum_difference = 0

    def compute_difference(self):
        """Sort the list and taking the first and last values."""
        self.__elements.sort()
        self.maximum_difference = abs(self.__elements[-1] - self.__elements[0])

if __name__ == "__main__":
    _ = input()
    ARRAY = [int(ELEMENT) for ELEMENT in input().split(' ')]

    DIFFERENCE = Difference(ARRAY)
    DIFFERENCE.compute_difference()

    print(DIFFERENCE.maximum_difference)
