class Stack:
    
    def __init__(self) -> None:
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        self.stack.pop()
        
    def display(self):
        print(self.stack)
        
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.stack[-1]
    
    def base(self):
        if self.is_empty():
            return None
        
        return self.stack[0]
    
    
def main():
    stack = Stack()
    stack.display()
    
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(100)
    stack.pop()
    stack.display()
    stack.push(200)
    stack.push(120)
    stack.push(89)
    print(stack.is_empty())
    stack.display()
    print(stack.peek())
    print(stack.base())
    
main()