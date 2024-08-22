class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def print_graph(self):
        for item in self.graph:
            print(f"{item}: {self.graph[item]}")

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def non_rec_dfs(self, source):
        visited = []
        stack = [source]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)

                for adjacent in self.graph[vertex]:
                    if adjacent not in visited:
                        stack.append(adjacent)
        return visited

    def dfs_util(self, vertex, visited):
        visited.append(vertex)

        for adjacent in self.graph[vertex]:
            if adjacent not in visited:

                self.dfs_util(adjacent, visited)

    def rec_dfs(self, source):
        visited = []

        self.dfs_util(source, visited)

        return visited


def main():
    V = 5  # Number of vertices
    source = 1
    g = Graph(V)
    E = 5  # Number of edges
    edges = [[1, 2], [1, 0], [0, 2], [2, 3], [2, 4]]
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    g.print_graph()
    print("DFS: ")
    print(g.non_rec_dfs(source))
    print(g.rec_dfs(source))


main()
