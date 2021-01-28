import unittest
import random
from Tree import Tree

class RandomNodeTree:
	
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.size = 1

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
		return " -> ".join([str(node.data) for node in self])

	def find(self, value):
		if self.data == value:
			return self
		elif self.data > value:
			if self.left:
				return self.left.find(value)
			else:
				return None
		else:
			if self.right:
				return self.right.find(value)
			else:
				return None

	def insert(self, value):
		#insert inorder
		if value <= self.data:
			if self.left is None:
				self.left = RandomNodeTree(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = RandomNodeTree(value)
			else:
				self.right.insert(value)
		self.size += 1
	
	def get_random_node(self):
		random_number = random.randint(0, self.size-1)
		left_size = self.left.size if self.left else 0
		if random_number < left_size:
			return self.left.get_random_node()
		elif random_number == left_size:
			return self
		else:
			return self.right.get_random_node()


class TestRandomNodeTree(unittest.TestCase):

	def setUp(self):
		nodes = [1, 4, 2, 5, 7, 6, 3]
		self.tree = RandomNodeTree(8)
		for node in nodes:
			self.tree.insert(node)
	
	def tearDown(self):
		pass

	def test_random_node_tree(self):
		random_node = self.tree.get_random_node()
		self.assertEqual(random_node, self.tree.find(random_node.data))


if __name__ == "__main__":
	unittest.main()

