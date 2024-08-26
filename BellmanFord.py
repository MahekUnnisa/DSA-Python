import heapq


class Graph:
    def __init__(self):
        self.adj_list = {}

    def insert(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge_with_weight(self, u, v, w):
        if u not in self.adj_list:
            self.insert(u)
        if v not in self.adj_list:
            self.insert(v)

        temp_u = [u, w]
        temp_v = [v, w]

        if temp_v not in self.adj_list[u]:
            self.adj_list[u].append(temp_v)

        if temp_u not in self.adj_list[v]:
            self.adj_list[v].append(temp_u)

    def print_graph(self):
        for each in self.adj_list:
            print(f"{each}: {self.adj_list[each]}")

    def bellman_ford(self, edges, src, E, V):
        distances = {i: float("inf") for i in range(1, V + 1)}
        distances[src] = 0

        for _ in range(1, V):  # Loop V-1 times
            for edge in edges:  # Loop over all edges
                u, v, w = edge
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    
        for edge in edges:
            u, v, w = edge
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return None
        
        # return distances
        return distances


def main():
    graph = Graph()

    src = 1
    E = 4
    V = 4
    edges = [[4, 4, 1], [1, 2, 4], [1, 3, 3], [2, 4, 7], [3, 4, -2]]
    shortest_path = graph.bellman_ford(edges, src, E, V)
    print(shortest_path)


if __name__ == "__main__":
    main()
