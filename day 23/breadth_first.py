"""Breadth-first traversal of a binary search tree."""

class Node:#pylint:disable=too-few-public-methods
    """A node holds data, and points to child nodes left and right."""

    def __init__(self, data):
        """Initialise the Node to contain data and no children."""
        self.right = self.left = None
        self.data = data

class Solution:
    """Solution class implements the node class."""

    def insert(self, root, data):
        """Insert a node, checking whether it's a left or right child of the root."""
        if root is None:
            return Node(data)
        if data <= root.data:
            cur = self.insert(root.left, data)
            root.left = cur
        else:
            cur = self.insert(root.right, data)
            root.right = cur
        return root

    def level_order(self, root):#pylint:disable=no-self-use
        """Traverse the tree level by level."""
        if root is None:
            return
        my_q = list()
        my_q.append(root)
        while len(my_q) > 0:
            node = my_q[0]
            print(node.data, end=" ")
            my_q = my_q[1:]
            if node.left is not None:
                my_q.append(node.left)
            if node.right is not None:
                my_q.append(node.right)

if __name__ == "__main__":
    T = int(input())
    MY_TREE = Solution()
    ROOT = None
    for _ in range(T):
        DATA = int(input())
        ROOT = MY_TREE.insert(ROOT, DATA)
    MY_TREE.level_order(ROOT)
