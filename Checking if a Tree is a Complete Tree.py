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


index = 0


def Counting_Nodes(root):
    if not root:
        return 0
    else:
        return (1+Counting_Nodes(root.left)+Counting_Nodes(root.right))

num_nodes = Counting_Nodes(root)

def is_Complete(root,index,num_nodes):
    if root is None:
        return True
    if index >= num_nodes:
        return False
    
    return (is_Complete(root.left , 2*index+1 , num_nodes) and is_Complete(root.right, 2*index+2, num_nodes))
    
is_Complete(root,0,num_nodes)
