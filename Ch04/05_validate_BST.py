import unittest
from Tree import Tree

def validate_BST_without_same_value(tree):
	
	def inorder_validate(tree):
		if tree:
			yield from inorder_validate(tree.left)
			yield tree.data
			yield from inorder_validate(tree.right)
	
	pre = None
	for val in inorder_validate(tree):
		if pre is not None and val < pre:
			return False
		pre = val
	return True

def validate_BST(tree):
	return check_BST(tree, None, None)

def check_BST(tree, mini, maxi):
	if not tree: return True
	if mini and mini >= tree.data: return False
	if maxi and maxi < tree.data: return False
	if not check_BST(tree.left, mini, tree.data) or \
	   not check_BST(tree.right, tree.data, maxi):
		return False
	return True


class TestValidateBST(unittest.TestCase):

	def setUp(self):
		self.BST = Tree(8)
		self.BST.set_left(4)
		self.BST.set_right(12)
		self.BST.left.set_left(2)
		self.BST.left.set_right(6)
		self.BST.right.set_left(10)
		self.BST.right.set_right(20)
		self.not_BST = Tree(8)
		self.not_BST.set_left(4)
		self.not_BST.set_right(10)
		self.not_BST.left.set_left(2)
		self.not_BST.left.set_right(12)
		self.not_BST.right.set_left(15)
		self.not_BST.right.set_right(20)
		self.small_BST = Tree(20)
		self.small_BST.set_left(20)
		self.small_not_BST = Tree(20)
		self.small_not_BST.set_right(20)
	
	def tearDown(self):
		pass

	def test_validate_BST(self):
		self.assertTrue(validate_BST(Tree(0)))
		self.assertTrue(validate_BST(self.BST))
		self.assertFalse(validate_BST(self.not_BST))
		self.assertTrue(validate_BST(self.small_BST))
		self.assertFalse(validate_BST(self.small_not_BST))


if __name__ == "__main__":
	unittest.main()

