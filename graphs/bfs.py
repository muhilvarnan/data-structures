"""
Graphs Implementations

Graph structure

graphHolder = {
  "a": Vertex("a", {b, c}),
  "b": Vertex("b", {a, c})
  "c": Vertex("c")
}

Depth first search algorithm
"""

class Vertex(object):
	"""
	Graph Vertex
	"""

	def __init__(self, node):
		"""
		constructor for vertex
		"""
		self.id = node
		self.adjacent_vertices = {}

	def add_adjacent(self, node, weight):
		"""
		add ajacent 
		"""
		key = node.getID()
		self.adjacent_vertices[key] = weight

	def getID(self):
		"""
		get id
		"""
		return self.id

	def get_connections(self):
	        return self.adjacent_vertices.keys()

class GraphHolder(object):
	"""
	Graph Holder
	"""
	def __init__(self, ):
		"""
		constructor for vertex
		"""
		self.vertex_count = 0
		self.vertex_list = {}

	def add_vertex(self, node):
		"""
		Add Vertex
		"""
		self.vertex_count = self.vertex_count + 1
		self.vertex_list[node] = Vertex(node)
		return self.vertex_list[node]

	def add_edge(self, start, end, weight):
		"""
		Add edge
		"""
		self.vertex_list[start].add_adjacent(self.vertex_list[end], weight)
		self.vertex_list[end].add_adjacent(self.vertex_list[start], weight)

	def bfs(self, start):
		visited, queue = [], [start]
		while queue:
			vertex = queue.pop(0)
			if vertex not in visited:
				visited.append(vertex)
				conn = self.vertex_list[vertex].get_connections()
				diff = [x for x in conn if x not in set(visited)]
				queue.extend(diff)
		return visited

	def bfs_path(self, start, goal):
		queue = [(start, [start])]
		while queue:
			(vertex, path) = queue.pop(0)
			conn = self.vertex_list[vertex].get_connections()
			diff = [x for x in conn if x not in set(path)]
			for next in diff:
				if next == goal:
					yield path + [next]
				else:
					queue.append((next, path + [next]))

if __name__ == "__main__":
	graphHolder = GraphHolder()
	graphHolder.add_vertex("a")
	graphHolder.add_vertex("b")
	graphHolder.add_vertex("c")
	graphHolder.add_vertex("d")
	graphHolder.add_vertex("e")
	graphHolder.add_vertex("f")

	graphHolder.add_edge("a", "b", 3)
	graphHolder.add_edge("a", "c", 3)
	graphHolder.add_edge("b", "d", 3)
	graphHolder.add_edge("b", "e", 3)
	graphHolder.add_edge("c", "f", 3)
	graphHolder.add_edge("e", "f", 3)

	print graphHolder.bfs('a')
	print list(graphHolder.bfs_path('a', 'f'))
