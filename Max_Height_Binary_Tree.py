class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def height(root):
 
    # base case: empty tree has a height of 0
    if root is None:
        return 0
 
    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))
    

root = Node(1)
            
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6) 

height(root)
