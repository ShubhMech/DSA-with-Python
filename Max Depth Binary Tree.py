class Node:
    
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

root = Node(1)
            
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

def max_Depth(root):
  if root == None:
    return 0
  else: 
    return 1+max(max_Depth(root.left),max_Depth(root.right))
  
  print("The max depth of the tree is: ", max_Depth(root)-1) 
