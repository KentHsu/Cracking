from collections import defaultdict
from collections.abc import Sequence


class OOGraphNode:
	
	def __init__(self, data, children):
		self.data = data
		self.children = children

class OOGraph:
	
	def __init__(self, nodes):
		self.nodes = nodes


class Graph:
	
	def __init__(self, edges=None):
		self.graph = defaultdict(list)
		if edges:
			if isinstance(edges, dict):
				for u, v in edges.items():
					self.addEdge(u, v)
			else:
				for u, v in edges:
					self.addEdge(u, v)
	
	def addEdge(self, u, v):
		if isinstance(v, Sequence):
			for v_node in v:
				self.graph[u].append(v_node)
		else:
			self.graph[u].append(v)

	def BFS(self, start):
		visited = set()
		queue = [start]
		while queue:
			curr = queue.pop(0)
			if curr not in visited:
				print(curr, end=" ")
				visited.add(curr)
			for node in self.graph[curr]:
				if node not in visited:
					queue.append(node)
	
	def DFS(self, start):
		visited = set()
		stack = [start]
		while stack:
			curr = stack.pop()
			if curr not in visited:
				print(curr, end=" ")
				visited.add(curr)
			for node in self.graph[curr]:
				if node not in visited:
					stack.append(node)
	
	def bfs(self, queue, visited):
		if not queue:
			return
		node = queue.pop(0)
		print(node, end=" ")
		for nodes in self.graph[node]:
			if nodes not in visited:
				queue.append(nodes)
		self.bfs(queue, visited)

	def dfs(self, node, visited):
		print(node, end=" ")
		visited.add(node)
		for nodes in self.graph[node]:
			if nodes not in visited:
				self.dfs(nodes, visited)


if __name__ == "__main__":
	edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9), (5, 10), \
			 (4, 7), (4, 8), (7, 11), (7, 12)]
	g = Graph(edges)
	g.BFS(1)
	print()
	g.bfs([1], set())
	print()
	g.DFS(1)
	print()
	g.dfs(1, set())
	print()
