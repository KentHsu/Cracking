import unittest
from Graph import Graph


def build_order(graph, projects):
	result = []
	for project in projects:
		path = [node for node in bfs_traversal(graph, project)]
		result = path if len(path) > len(result) else result

	result_set = set(result)
	for project in projects:
		if project not in result_set:
			result.append(project)

	if len(result) != len(projects):
		return None
	else:
		return result

def bfs_traversal(graph, start):
	visited = set()
	queue = [start]
	while queue:
		node = queue.pop(0)
		if node not in visited:
			yield node
			visited.add(node)
		for neighbor in graph[node]:
			if neighbor not in visited:
				queue.append(neighbor)


class TestBuildOrder(unittest.TestCase):

	def setUp(self):
		self.projects = ['a', 'b', 'c', 'd', 'e', 'f']
		self.dependency = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
		self.graph = Graph(self.dependency).graph
	
	def tearDown(self):
		pass

	def test_build_order(self):
		self.assertTrue(1 == 0, 'Not Completed')
		order = build_order(self.graph, self.projects)
		print(order)
		dependency = {value: key for key, value in self.dependency}
		completed_projects = set()
		for project in order:
			if project in dependency:
				self.assertIn(dependency[project], completed_projects)
			completed_projects.add(project)


if __name__ == "__main__":
	unittest.main()

