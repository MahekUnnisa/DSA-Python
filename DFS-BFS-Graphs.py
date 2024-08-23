from collections import deque


class Graph:
    def __init__(self, V):
        self.graph = {i: [] for i in range(V)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for item in self.graph:
            print(f"{item}: {self.graph[item]}")

    def dfs_util(self, source, visited):
        adjacents = self.graph[source]
        visited.append(source)

        for each in adjacents:
            if each not in visited:
                self.dfs_util(each, visited)

    def rec_dfs(self, source):
        visited = []

        self.dfs_util(source, visited)
        print(visited)
        return visited

    def non_rec_dfs(self, source):
        visited = []
        stack = [source]

        while stack:
            top = stack.pop()
            if top not in visited:
                visited.append(top)

                for neighbor in self.graph[top]:
                    stack.append(neighbor)

        print(visited)
        return visited

    def bfs_util(self, queue, seen):
        if not queue:
            return

        front = queue.popleft()
        print(queue)
        print(front)
        for each in self.graph[front]:
            if each not in seen:
                queue.append(each)

        if front not in seen:
            seen.append(front)
        self.bfs_util(queue, seen)

    def rec_bfs(self, source):
        seen = []
        queue = deque()
        queue.append(source)
        self.bfs_util(queue, seen)

        print(seen)
        return seen

    def non_rec_bfs(self, source):
        seen = []
        queue = deque()
        queue.append(source)

        while queue:
            front = queue.popleft()

            if front not in seen:
                seen.append(front)

                for each in self.graph[front]:
                    if each not in seen:
                        queue.append(each)
        print(seen)
        return seen


def main():
    source = 0
    V = 5
    E = 5
    graph = Graph(V)
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    graph.non_rec_dfs(source)
    graph.rec_dfs(source)
    print("BFS: ")
    graph.non_rec_bfs(source)
    graph.rec_bfs(source)


main()
