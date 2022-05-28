class Node:
    
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def countNodes(root):
	if root is None:
		return 0
	return (1+ countNodes(root.left) + countNodes(root.right))


root = Node(1)
            
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

node_count = countNodes(root)
