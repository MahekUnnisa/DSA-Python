from Stack import Stack

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val)
        
    def in_order(self, node):
        if node == None:
            return node
        self.in_order(node.left)
        print(node.data, end=" ")
        self.in_order(node.right)
        
    def in_order__stack(self, node):
        result = []
        stack = Stack()
        curr = node
        
        while curr is not None or stack is not None:
            while curr is not None:
                stack.push(curr)
                curr = curr.left
            
            if stack.is_empty():
                break
            
            curr = stack.pop()
            if curr is not None:  # Ensure curr is not None before accessing its data
                result.append(curr.data)
                curr = curr.right
        
        return result
                
    
    def pre_order(self, node):
        if node == None:
            return node
        print(node.data, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)
    
    def post_order(self,node):
        # LRN
        if node == None:
            return None
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=" ")
        
        

def main():
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)
    tree.root.right.right = TreeNode(7)
    # tree.left.left.right = TreeNode(4)
    
    print("\nInOrder Traversal:")
    tree.in_order(tree.root)
    
    print("\n\n\nInOrder Traversal Using Stack:")
    print(tree.in_order__stack(tree.root))
    
    print("\n\n\nPreOrder Traversal:")
    tree.pre_order(tree.root)
    
    print("\n\n\nPostOrder Traversal:")
    tree.post_order(tree.root)
    
main()