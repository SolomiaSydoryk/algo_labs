class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_distance(self, dist, visited):
        index = 0
        dist_min = float('inf')
        for v in range(self.V):
            if dist[v] < dist_min and visited[v] is False:
                dist_min = dist[v]
                index = v
        return index

    def dijkstra(self, first_node):
        dist = [float('inf')] * self.V
        dist[first_node] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                        self.graph[u][v] > 0
                        and visited[v] is False
                        and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def find_optimal_server_location(self, client_nodes):
        min_max_latency = float('inf')

        for potential_server in range(self.V):
            current_graph = [row[:] for row in self.graph]

            for client in client_nodes:
                current_graph[client - 1][potential_server] = 0
                current_graph[potential_server][client - 1] = 0

            current_dist = self.dijkstra(potential_server)

            max_latency = max(current_dist)
            if max_latency < min_max_latency:
                min_max_latency = max_latency

        return min_max_latency


with open("../gamsrv.in", "r") as infile:
    N, M = map(int, infile.readline().split())
    client_nodes = list(map(int, infile.readline().split()))
    g = Graph(N)
    for _ in range(M):
        start, end, latency = map(int, infile.readline().split())
        g.graph[start - 1][end - 1] = latency
        g.graph[end - 1][start - 1] = latency

with open("../gamsrv.out", "w") as outfile:
    result = g.find_optimal_server_location(client_nodes)
    outfile.write(str(result))
