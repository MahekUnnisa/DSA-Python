class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete_with_value(self, data):
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
        current_node= self.head
        while current_node != None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
        
    def reverse(self):
        if self.head ==None:
            return self.head
        
        prev = None
        next = None
        current = self.head
        
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        self.head = prev
        
    def length(self):
        curr = self.head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count
    
    def middle(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self.head.data
        
        slow = self.head
        fast = self.head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
       
    def tail(self):
        curr = self.head
        tail = self.head
        while curr:
            tail = curr.data
            curr = curr.next
        return tail 
    
def main():
    print("ok")
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(15)
    linked_list.append(20)
    linked_list.prepend(5)
    linked_list.prepend(0)
    linked_list.display()
    print(linked_list.length())
    print("len: ",linked_list.length())
    print("tail: ",linked_list.tail())
    print("mid: ",linked_list.middle())
    
main()