class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # The reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # The head (first node) of the list

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add a new node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        """Delete the first node with the given value."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next is None:
            return
        current_node.next = current_node.next.next

    def display(self):
        """Print out the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
