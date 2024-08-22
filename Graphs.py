class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                if vertex in self.adjacency_list[adjacent]:
                    self.adjacency_list[adjacent].remove(vertex)
            del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
        if vertex2 in self.adjacency_list and vertex1 in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].remove(vertex1)

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")


def main():
    graph = Graph()
    graph.add_vertex("X")
    graph.add_vertex("Y")
    graph.add_vertex("Z")
    graph.print_graph()
    graph.add_edge("X", "Y")
    graph.add_edge("Y", "Z")
    graph.add_edge("X", "Z")
    graph.print_graph()
    graph.remove_edge("X", "Z")
    graph.remove_vertex("Y")
    graph.print_graph()


main()
