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

    def dijkstra(self, src, E, V):
        # Shortest path in a graph from src to all vertices

        distances = []
        # Index be the node and the value  be the distance of that node from src

        for each in range(V):
            distances.append(float("inf"))
        distances[src] = 0

        min_heap = []

        # Push a tuple of weight, node
        heapq.heappush(min_heap, (0, src))

        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)

            if curr_weight > distances[curr_node]:
                continue
            for node, weight in self.adj_list[curr_node]:
                final_distance = curr_weight + weight

                if final_distance < distances[node]:
                    distances[node] = final_distance
                    heapq.heappush(min_heap, (final_distance, node))

        return distances


def main():
    graph = Graph()
    graph.insert(0)
    graph.insert(1)
    graph.insert(2)
    graph.insert(3)
    graph.insert(4)

    graph.add_edge_with_weight(0, 1, 7)
    graph.add_edge_with_weight(0, 2, 1)
    graph.add_edge_with_weight(0, 3, 2)
    graph.add_edge_with_weight(1, 0, 7)
    graph.add_edge_with_weight(1, 3, 5)

    graph.add_edge_with_weight(1, 4, 1)
    graph.add_edge_with_weight(2, 1, 3)

    graph.add_edge_with_weight(2, 0, 1)
    graph.add_edge_with_weight(3, 0, 2)
    graph.add_edge_with_weight(3, 1, 5)
    graph.add_edge_with_weight(3, 4, 7)

    graph.add_edge_with_weight(4, 1, 1)
    graph.add_edge_with_weight(4, 3, 7)

    graph.print_graph()

    src = 0
    E = 14
    V = 5

    shortest_path = graph.dijkstra(src, E, V)
    print(shortest_path)


if __name__ == "__main__":
    main()
