import unittest

from src.main import find_successor, BinaryTree


class TestFind(unittest.TestCase):
    def test_first(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5, parent=root)
        root.right = BinaryTree(12, parent=root)
        root.left.left = BinaryTree(3, parent=root.left)
        root.left.right = BinaryTree(7, parent=root.left)
        root.right.right = BinaryTree(20, parent=root.right)
        root.right.right.left = BinaryTree(15, parent=root.right.right)
        successor_node = find_successor(root.left.right)

        self.assertEqual(successor_node.value, 10)

    if __name__ == '__main__':
        unittest.main()
