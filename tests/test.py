import unittest
from src.main import Graph


class TestMinMaxLatency(unittest.TestCase):
    def test_first(self):
        graph = Graph(6)
        graph.graph = [
            [0, 0, 10, 0, 0, 0],
            [0, 0, 40, 100, 0, 0],
            [10, 40, 0, 80, 0, 0],
            [0, 100, 80, 0, 50, 0],
            [0, 0, 0, 50, 0, 20],
            [0, 0, 0, 0, 20, 0]
        ]
        client_nodes = [1, 2, 6]
        result = graph.find_optimal_server_location(client_nodes)
        self.assertEqual(result, 100)

    def test_second(self):
        graph = Graph(9)
        graph.graph = [
            [0, 20, 0, 20, 0, 0, 0, 0, 0],
            [20, 0, 20, 0, 10, 0, 0, 0, 0],
            [0, 20, 0, 0, 0, 20, 0, 0, 0],
            [20, 0, 0, 0, 10, 0, 20, 0, 0],
            [0, 10, 0, 10, 0, 10, 10, 10, 10],
            [0, 0, 20, 0, 10, 0, 0, 20, 0],
            [0, 0, 0, 20, 10, 0, 0, 20, 0],
            [0, 0, 0, 0, 10, 20, 20, 0, 20],
            [0, 0, 0, 0, 10, 0, 0, 20, 0]
        ]
        client_nodes = [2, 4, 6]
        result = graph.find_optimal_server_location(client_nodes)
        self.assertEqual(result, 20)

    def test_third(self):
        graph = Graph(3)
        graph.graph = [
            [0, 50, 1000000000],
            [50, 0, 1000000000],
            [1000000000, 1000000000, 0]
        ]
        client_nodes = [1, 3]
        result = graph.find_optimal_server_location(client_nodes)
        self.assertEqual(result, 1000000000)


if __name__ == '__main__':
    unittest.main()
