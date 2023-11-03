import unittest
from src.main import min_depth, build_tree, Node


class TestMinDepth(unittest.TestCase):
    def test_min_depth_empty_tree(self):
        root = None
        self.assertEqual(min_depth(root), 0)

    def test_min_depth_single_node(self):
        root = Node(1)
        self.assertEqual(min_depth(root), 1)

    def test_min_depth_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertEqual(min_depth(root), 3)

    def test_min_depth_balanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(min_depth(root), 2)

    def test_build_tree(self):
        edges = ["1,2", "1,3", "2,4", "2,5"]
        root = build_tree(edges)
        self.assertEqual(root.value, 1)
        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.right.value, 3)
        self.assertEqual(root.left.left.value, 4)
        self.assertEqual(root.left.right.value, 5)


if __name__ == '__main__':
    unittest.main()
