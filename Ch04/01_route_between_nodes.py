import unittest
from Graph import Graph


def bfs(graph, start, end):
	visited = set()
	queue = list(graph[start])
	while queue:
		node = queue.pop(0)
		if node == end:
			return True
		if node not in visited:
			visited.add(node)
			for neighbor in graph[node]:
				queue.append(neighbor)
	return False

def dfs(graph, start, end, visited):
	if start == end:
		return True
	if start not in visited:
		visited.add(start)
		for neighbor in graph[start]:
			if dfs(graph, neighbor, end, visited):
				return True
	return False


class TestRouteBetweenNodes(unittest.TestCase):
	
	def setUp(self):
		cities = {
			'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
			'Mannheim' : ['Karlsruhe'],
			'Karlsurhe': ['Augsburg'],
			'Augsburg' : ['Munchen'],
			'Wurzburg' : ['Erfurt', 'Murnberg'],
			'Nurnberg' : ['Stuttgart', 'Munchen'],
			'Kassel'   : ['Munchen'],
			'Erfurt'   : [],
			'Stuttgart': [],
			'Munchen'  : [], 
		}
		self.graph = Graph(cities).graph
	
	def tearDown(self):
		pass
	
	def test_route_between_nodes(self):
		self.assertTrue(bfs(self.graph, 'Frankfurt', 'Munchen'))
		self.assertFalse(bfs(self.graph, 'Frankfurt', 'Stuttgart'))
		self.assertTrue(dfs(self.graph ,'Frankfurt', 'Munchen', set()))
		self.assertFalse(dfs(self.graph, 'Frankfurt', 'Stuttgart', set()))
	

if __name__ == "__main__":
	unittest.main()

