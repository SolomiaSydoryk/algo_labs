from collections import deque


class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def min_depth(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        if node.left is None and node.right is None:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


def build_tree(edges):
    node_list = {}
    for edge in edges:
        parent, child = map(int, edge.split(','))
        if parent not in node_list:
            node_list[parent] = Node(parent)
        if child not in node_list:
            node_list[child] = Node(child)
        parent_node = node_list[parent]
        child_node = node_list[child]
        if parent_node.left is None:
            parent_node.left = child_node
        else:
            parent_node.right = child_node
    return node_list[1]


if __name__ == "__main__":
    with open('../input.txt', 'r') as input_file:
        root_value = int(input_file.readline().strip())
        edges = input_file.read().strip().split('\n')

    root = build_tree(edges)
    result = min_depth(root)

    with open('../output.txt', 'w') as output_file:
        output_file.write(str(result))
