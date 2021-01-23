import unittest
from Tree import Tree, inorder_traversal


def minimal_tree(data):
	n = len(data) // 2
	tree = Tree(data[n])
	tree.left = minimal_tree(data[:n]) if data[:n] else None
	tree.right = minimal_tree(data[n+1:]) if data[n+1:] else None
	return tree


class TestMinimalTree(unittest.TestCase):
	
	def setUp(self):
		self.data = list(range(10))

	def tearDown(self):
		pass
	
	def test_route_between_nodes(self):
		tree = minimal_tree(self.data)
		inorder = [node for node in inorder_traversal(tree)]
		self.assertEqual(inorder, self.data)
	

if __name__ == "__main__":
	unittest.main()

