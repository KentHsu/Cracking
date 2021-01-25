import unittest
from Tree import Tree

def first_common_ancestor_0(tree, node1, node2):
	if tree == node1 or tree == node2:
		return tree
	if tree.left and tree.right:
		if (node1 in tree.left and node2 in tree.right) or \
		   (node1 in tree.right and node2 in tree.left):
			return tree
	left = first_common_ancestor(tree.left, node1, node2) \
			   if tree.left else None
	right = first_common_ancestor(tree.right, node1, node2) \
			if tree.right else None
	return left or right


def first_common_ancestor(tree, node1, node2):
	if tree is None or tree == node1 or tree == node2:
		return tree

	left = first_common_ancestor(tree.left, node1, node2)
	if left and left != node1 and left != node2:
		return left
	right = first_common_ancestor(tree.right, node1, node2)
	if right and right != node1 and right != node2: 
		return right

	if left and right:
		return tree
	return left or right 


def first_common_ancestor_(tree, node1, node2):
	if tree is None:
		return None
	if tree == node1 and tree == node2:
		return tree
	
	left = first_common_ancestor(tree.left, node1, node2)
	if left and left != node1 and left != node2:
		return left
	right = first_common_ancestor(tree.right, node1, node2)
	if right and right != node1 and right != node2:
		return right

	if left and right:
		return tree
	elif tree == node1 or tree == node2:
		return tree
	else:
		return left or right


class TestFirstCommonAncestor(unittest.TestCase):

	def setUp(self):
		self.BST = Tree(8)
		self.BST.set_left(4)
		self.BST.set_right(12)
		self.BST.left.set_left(2)
		self.BST.left.set_right(6)
		self.BST.right.set_left(10)
		self.BST.right.set_right(20)

	def tearDown(self):
		pass

	def test_first_common_ancestor(self):
		node1 = self.BST.left.right
		node2 = self.BST.right.left
		node3 = self.BST.left.left
		node4 = self.BST.right.right
		self.assertEqual(first_common_ancestor(self.BST, \
						 node1, node2), self.BST)
		self.assertEqual(first_common_ancestor(self.BST, \
						 node3, node4), self.BST)
		self.assertEqual(first_common_ancestor(self.BST, \
						 node1, node3), self.BST.left)
		self.assertEqual(first_common_ancestor(self.BST, \
						 node2, node4), self.BST.right)
		self.assertEqual(first_common_ancestor(self.BST, \
						 self.BST, self.BST.left), self.BST)
		self.assertEqual(first_common_ancestor(Tree(1), node1, Tree(2)), None)
		self.assertEqual(first_common_ancestor(Tree(1), node1, node2), None)

if __name__ == "__main__":
	unittest.main()

