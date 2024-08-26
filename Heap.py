class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def display(self):
        print(self.heap)

# Example usage
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(1)

min_heap.display()  # Output: [1, 5, 20, 10]

print(min_heap.extract_min())  # Output: 1
min_heap.display()  # Output: [5, 10, 20]
