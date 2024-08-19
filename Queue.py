class Queue:
    def __init__(self) -> None:
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
        
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def display(self):
        print(self.queue)
        
def main():
    queue = Queue()
    
    queue.display()
    
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(100)
    
    queue.display()
    print(queue.dequeue())
    
    queue.display()
    queue.enqueue(200)
    queue.enqueue(120)
    queue.enqueue(89)
    
    print(queue.is_empty())
    
    queue.display()
    
    print(queue.peek())
        
        
main()