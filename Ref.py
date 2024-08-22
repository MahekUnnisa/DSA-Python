class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Add a new vertex with an empty list of edges
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        # Add an edge between vertex1 and vertex2 (undirected)
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        
        # Add vertex2 to the adjacency list of vertex1
        self.adjacency_list[vertex1].append(vertex2)
        # Add vertex1 to the adjacency list of vertex2 (undirected edge)
        self.adjacency_list[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1, vertex2):
        # Remove the edge between vertex1 and vertex2
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
        if vertex2 in self.adjacency_list and vertex1 in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].remove(vertex1)
    
    def remove_vertex(self, vertex):
        # Remove a vertex and all its edges
        if vertex in self.adjacency_list:
            # Remove the vertex from all adjacency lists
            for adjacent in self.adjacency_list[vertex]:
                if vertex in self.adjacency_list[adjacent]:
                    self.adjacency_list[adjacent].remove(vertex)
            # Remove the vertex from the adjacency list
            del self.adjacency_list[vertex]
    
    def print_graph(self):
        # Print the adjacency list representation of the graph
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

# Example usage
def main():
    graph = Graph()
    
    # Add vertices and edges
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    
    print("Graph adjacency list:")
    graph.print_graph()
    
    print("\nRemoving edge A-C and vertex B:")
    graph.remove_edge("A", "C")
    graph.remove_vertex("B")
    
    print("\nGraph adjacency list after modifications:")
    graph.print_graph()

main()
