"""Exploring linked lists in Python."""

class Node: # pylint: disable=too-few-public-methods
    """Node class to create the linked list."""

    def __init__(self, data):
        """Initialise the data and the next node."""
        self.data = data
        self.next = None

class Solution:
    """Display and Insert funcitons."""

    def display(self, head): # pylint: disable=no-self-use
        """Display all node's data."""
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data): # pylint: disable=no-self-use
        """Insert a node to the end of the list."""
        temp = Node(data)
        if head is None:
            head = temp
        else:
            last = head
            while last.next is not None:
                last = last.next
            last.next = temp
        return head

if __name__ == "__main__":
    MY_LIST = Solution()
    TESTS = int(input())
    HEAD = None
    for i in range(TESTS):
        DATA = int(input())
        HEAD = MY_LIST.insert(HEAD, DATA)
    MY_LIST.display(HEAD)
