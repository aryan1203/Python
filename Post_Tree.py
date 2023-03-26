
# class to define node
class Node:
	
	# constructor to create node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# function post_Tree 
def post_Tree(root):

	if root is None:
		return	
	
	# define row stack- stack_A and stack_B
	stack_A = []
	stack_B = []
	
	# start from root node and push to stack_A
	stack_A.append(root)
	
	# Repeat untill stack_A is empty
	while stack_A:
		
		# pop node from stack_A and push to stack_B
		node = stack_A.pop()
		stack_B.append(node)
	
		# push left and right node of popped node
		if node.left:
			stack_A.append(node.left)
		if node.right:
			stack_A.append(node.right)

		# if stack_A is empty print all nodes of stack_B
	while stack_B:
		node = stack_B.pop()
		print(node.data,end=" ")

# program to run function
# Display: [6,1,11,7,14,25,21]
root = Node(21)
root.left = Node(11)
root.right = Node(25)
root.left.left = Node(6)
root.left.right = Node(1)
root.right.left = Node(7)
root.right.right = Node(14)
post_Tree(root)

