import unittest
from Tree import Tree

def successor(node):
	if not node: return None
	if node.right:
		curr = node.right
		while curr.left:
			curr = curr.left
		return curr
	else:
		curr = node
		while curr.parent is not None and curr != curr.parent.left:
			curr = curr.parent
		return curr.parent


class TestSuccessor(unittest.TestCase):

	def setUp(self):
		nodes = [1, 4, 2, 5, 7, 6, 3]
		self.tree = Tree().create_tree(nodes)
		self.BST = Tree(8)
		self.BST.set_left(4)
		self.BST.set_right(12)
		self.BST.left.set_left(2)
		self.BST.left.set_right(6)
		self.BST.right.set_left(10)
		self.BST.right.set_right(20)
	
	def tearDown(self):
		pass

	def test_successor(self):
		# test BST
		self.assertEqual(successor(self.BST.left.left), self.BST.left)
		self.assertEqual(successor(self.BST.left), self.BST.left.right)
		self.assertEqual(successor(self.BST.left.right), self.BST)
		self.assertEqual(successor(self.BST), self.BST.right.left)
		self.assertEqual(successor(self.BST.right.left), self.BST.right)
		self.assertEqual(successor(self.BST.right), self.BST.right.right)
		self.assertEqual(successor(self.BST.right.right), None)

		# test normal tree
		self.assertEqual(successor(self.tree), self.tree.right.left)
		self.assertEqual(successor(self.tree.right.left), self.tree.right.left.right)
		
		self.assertEqual(successor(self.tree.right.left.right), self.tree.right)
		self.assertEqual(successor(self.tree.right), self.tree.right.right)
		self.assertEqual(successor(self.tree.right.right), self.tree.right.right.right.left)
		self.assertEqual(successor(self.tree.right.right.right.left), self.tree.right.right.right)
		self.assertEqual(successor(self.tree.right.right.right), None)
		


if __name__ == "__main__":
	unittest.main()

