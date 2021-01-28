import unittest
from Tree import Tree


def path_with_sum_(tree, summ, results):
	if not tree: return
	calculate_path(tree, summ, [], results)
	path_with_sum(tree.left, summ, results)
	path_with_sum(tree.right, summ, results)

def calculate_path(tree, summ, path, paths):
	if not tree: return
	if (summ - tree.data) == 0:
		paths.append(path + [tree.data])
	calculate_path(tree.left, summ-tree.data, path + [tree.data], paths)
	calculate_path(tree.right, summ-tree.data, path + [tree.data], paths)


def path_with_sum(tree, summ, results):
	if not tree: return
	collect_path(tree, summ, [], results)

def collect_path(tree, summ, paths, path):
	if not tree: return
	if not tree.left and not tree.right:
		paths.append(path + [tree.data])
		return
	collect_path(tree.left, summ, paths, path + [tree.data])
	collect_path(tree.right, summ, paths, path + [tree.data])


class TestPathsWithSum(unittest.TestCase):

	def setUp(self):
		self.target = 8
		self.tree = Tree(10)
		self.tree.set_left(5)
		self.tree.set_right(-3)
		self.tree.left.set_left(3)
		self.tree.left.set_right(2)
		self.tree.left.left.set_left(3)
		self.tree.left.left.set_right(-2)
		self.tree.left.right.set_right(1)
		self.tree.right.set_right(11)
	
	def tearDown(self):
		pass

	def test_paths_with_sum(self):
		self.assertTrue(1 == 0, 'can be faster')
		paths = []
		path_with_sum(self.tree, self.target, paths)
		print(paths)
		for path in paths:
			self.assertEqual(sum(path), self.target)


if __name__ == "__main__":
	unittest.main()


