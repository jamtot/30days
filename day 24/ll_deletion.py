"""Delete duplicates from a linked list."""

class Node:#pylint:disable=too-few-public-methods
    """Node class holds data and points to next node."""

    def __init__(self, data):
        """Initalise the data and pointer to next."""
        self.data = data
        self.next = None

class Solution:
    """Solution class inserts, displays and removes duplicates."""

    def insert(self, head, data):#pylint:disable=no-self-use
        """Insert a new node to the list."""
        new_node = Node(data)
        if head is None:
            head = new_node
        elif head.next is None:
            head.next = new_node
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = new_node
        return head

    def display(self, head):#pylint:disable=no-self-use
        """Display the nodes."""
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def remove_duplicates(self, head):#pylint:disable=no-self-use
        """Remove the duplicates from the list."""
        curr = head
        prev = None
        num_list = list()
        while curr is not None:
            if curr.data not in num_list:
                num_list.append(curr.data)
                prev = curr
            else:
                prev.next = curr.next
            curr = prev.next
        return head

if __name__ == "__main__":
    MY_LIST = Solution()
    TESTS = int(input())
    HEAD = None
    for _ in range(TESTS):
        DATA = int(input())
        HEAD = MY_LIST.insert(HEAD, DATA)
    HEAD = MY_LIST.remove_duplicates(HEAD)
    MY_LIST.display(HEAD)
