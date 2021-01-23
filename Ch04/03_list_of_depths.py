import unittest
from Tree import Tree
from LinkedList import ListNode

def list_of_depths(tree):
	queue = [tree]
	result = []
	while queue:
		level = []
		for _ in range(len(queue)):
			node = queue.pop(0)
			level.append(node.data)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		result.append(level)
	return result


class TestListOfDepths(unittest.TestCase):

	def setUp(self):
		nodes = [1, 4, 2, 5, 7, 6, 3]
		self.tree = Tree().create_tree(nodes)
	
	def test_list_of_depths(self):
		data = [[1], [4], [2, 5], [3, 7], [6]]
		answer = [ListNode(nodes) for nodes in data]
		result = [ListNode(res) for res in list_of_depths(self.tree)]
		for result_list, ans_list in zip(result, answer):
			self.assertEqual(result_list, ans_list)


if __name__ == "__main__":
	unittest.main()

