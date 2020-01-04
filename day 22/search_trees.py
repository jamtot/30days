"""Get the height of a binary search tree."""

class Node:#pylint:disable=too-few-public-methods
    """Node class links the root to each leaf."""

    def __init__(self, data):
        """Initialise the Node."""
        self.right = self.left = None
        self.data = data

class Solution:
    """Solution class implements the node class."""

    def insert(self, root, data):
        """Insert a new node."""
        if root is None:
            return Node(data)
        if data <= root.data:
            cur = self.insert(root.left, data)
            root.left = cur
        else:
            cur = self.insert(root.right, data)
            root.right = cur
        return root

    def get_height(self, root):
        """Get the height of the tree recursively."""
        if root is None:
            return -1
        l_depth = self.get_height(root.left)
        r_depth = self.get_height(root.right)
        if l_depth > r_depth:
            return l_depth + 1
        return r_depth + 1

if __name__ == "__main__":
    T_INPUT = int(input())
    MY_TREE = Solution()
    ROOT = None
    for _ in range(T_INPUT):
        DATA = int(input())
        ROOT = MY_TREE.insert(ROOT, DATA)
    HEIGHT = MY_TREE.get_height(ROOT)
    print(HEIGHT)
