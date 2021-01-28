import unittest
from Tree import Tree, levelorder_traversal

def check_subtree(tree1, tree2):
	if not tree1 and not tree2:
		return True
	if tree1 and tree2:
		for node in levelorder_traversal(tree1):
			if node.data == tree2.data:
				return check_subtree(node.left, tree2.left) and \
					   check_subtree(node.right, tree2.right)
	return False



class TestCheckSubtree(unittest.TestCase):

	def setUp(self):
		self.tree = Tree(8)
		self.tree.set_left(4)
		self.tree.set_right(12)
		self.tree.left.set_left(2)
		self.tree.left.set_right(6)
		self.tree.right.set_left(10)
		self.tree.right.set_right(20)
		self.subtree = Tree(4)
		self.subtree.set_left(2)
		self.subtree.set_right(6)
		self.not_subtree = Tree(4)
		self.not_subtree.set_left(2)
		self.not_subtree.set_right(8)
	
	def tearDown(self):
		pass

	def test_check_subtree(self):
		self.assertTrue(check_subtree(self.tree, self.subtree))
		self.assertFalse(check_subtree(self.tree, self.not_subtree))


if __name__ == "__main__":
	unittest.main()

