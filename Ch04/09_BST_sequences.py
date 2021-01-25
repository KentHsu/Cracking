import unittest
from Tree import Tree, levelorder_traversal

def BST_sequences(tree):
	i = 1
	levelorder_BST = levelorder_traversal(tree)
	result = [[next(levelorder_BST).data]]
	for node in levelorder_BST:
		for sequence in result:
			sequence.append(node.data)
		if i % 2 == 0:
			for idx in range(len(result)):
				reversed_sequence = list(result[idx])
				reversed_sequence[i-1], reversed_sequence[i] = \
				reversed_sequence[i], reversed_sequence[i-1]
				result.append(reversed_sequence)
		i += 1
	return result


class TestBSTSequences(unittest.TestCase):

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

	def test_BST_Sequences(self):
		self.assertTrue(1 == 0, 'recursion')
		for result in BST_sequences(self.BST):
			result_tree = Tree().create_tree(result)
			self.assertEqual(result_tree, self.BST)



if __name__ == "__main__":
	unittest.main()

