import unittest
from Tree import Tree
from LinkedList import ListNode

def check_balanced_1(tree):
	if not tree: return True
	if abs(tree_height_1(tree.left) - tree_height_1(tree.right)) > 1:
		return False
	return check_balanced_1(tree.left) and check_balanced_1(tree.right)

def tree_height_1(tree):
	if not tree: return -1
	return 1 + max(tree_height_1(tree.left), tree_height_1(tree.right))


def check_balanced(tree):
	return check_height(tree) != -float('inf')

def check_height(tree):
	if not tree: return -1
	left_height = check_height(tree.left)
	if left_height == -float('inf'):
		return -float('inf')

	right_height = check_height(tree.right)
	if right_height == -float('inf'):
		return -float('inf')

	height_diff = abs(left_height - right_height)
	if height_diff > 1:
		return -float('inf')
	else:
		return 1 + max(left_height, right_height)


class TestCheckBalanced(unittest.TestCase):

	def setUp(self):
		self.balanced_tree = Tree(1)
		self.balanced_tree.set_left(2)
		self.balanced_tree.set_right(3)
		self.balanced_tree.left.set_left(4)
		self.balanced_tree.left.set_right(5)
		self.balanced_tree.right.set_left(6)
		self.balanced_tree.right.set_right(7)
		self.unbalanced_tree = Tree(1)
		self.unbalanced_tree.set_left(2)
		self.unbalanced_tree.left.set_left(3)
		self.unbalanced_tree.left.left.set_left(4)
		self.unbalanced_tree.left.left.left.set_left(5)
		self.unbalanced_tree.set_right(6)
		self.unbalanced_tree.right.set_right(7)
		self.unbalanced_tree.right.right.set_right(8)
		self.unbalanced_tree.right.right.right.set_right(9)
	
	def tearDown(self):
		pass

	def test_check_balanced(self):
		self.assertTrue(check_balanced(Tree()))
		self.assertTrue(check_balanced(self.balanced_tree))
		self.assertFalse(check_balanced(self.unbalanced_tree))


if __name__ == "__main__":
	unittest.main()

