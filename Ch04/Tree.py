class Tree:
	
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = None
	
	def __iter__(self):
		queue = [self]
		while queue:
			node = queue.pop(0)
			yield node
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
	
	def __str__(self):
		values = [str(node.data) for node in self]
		return " -> ".join(values)

	def __eq__(self, other):
		if not self or not other:
			return self is None and other is None 
		if self.data == other.data:
			return self.left == other.left and self.right == other.right
	
	def set_left(self, value):
		self.left = Tree(value)
		self.left.parent = self

	def set_right(self, value):
		self.right = Tree(value)
		self.right.parent = self

	def insert_inorder(self, value):
		if self.data is None:
			self.data = value
		else:
			if value <= self.data:
				if self.left is None:
					self.set_left(value)
				else:
					self.left.insert_inorder(value)
			else:
				if self.right is None:
					self.set_right(value)
				else:
					self.right.insert_inorder(value)

	def create_tree(self, values):
		for value in values:
			self.insert_inorder(value)
		return self


def inorder_traversal(tree):
	if tree:
		yield from inorder_traversal(tree.left)
		yield tree.data
		yield from inorder_traversal(tree.right)

def preorder_traversal(tree):
	if tree:
		yield tree.data
		yield from preorder_traversal(tree.left)
		yield from preorder_traversal(tree.right)

def postorder_traversal(tree):
	if tree:
		yield from postorder_traversal(tree.left)
		yield from postorder_traversal(tree.right)
		yield tree.data

def levelorder_traversal(tree):
	queue = [tree]
	while queue:
		node = queue.pop(0)
		yield node
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)


if __name__ == "__main__":
	data = [1, 4, 2, 5, 7, 6, 3]
	tree = Tree()
	tree.create_tree(data)
	print(tree)


