class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(node: BinaryTree) -> BinaryTree:
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor
    else:
        parent = node.parent
        while parent and parent.right == node:
            node = parent
            parent = parent.parent
        return parent


