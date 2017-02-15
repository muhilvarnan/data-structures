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
		print self.vertex_list['s'].get_connections()
		visited, queue = [], [start]
		while queue:
			vertex = queue.pop(0)
			if vertex not in visited:
				visited.append(vertex)
				print vertex
				print self.vertex_list['s'].get_connections()
				conn = self.vertex_list['s'].get_connections()
				diff = [x for x in conn if x not in set(visited)]
				queue.extend(diff)
				print queue
		return visited

if __name__ == "__main__":
	graphHolder = GraphHolder()
	graphHolder.add_vertex("a")
	graphHolder.add_vertex("b")
	graphHolder.add_vertex("c")
	graphHolder.add_vertex("d")
	graphHolder.add_vertex("e")
	graphHolder.add_vertex("f")
	graphHolder.add_vertex("g")
	graphHolder.add_vertex("h")
	graphHolder.add_vertex("s")

	graphHolder.add_edge("a", "b", 3)
	graphHolder.add_edge("a", "s", 3)
	graphHolder.add_edge("s", "c", 3)
	graphHolder.add_edge("s", "g", 3)
	graphHolder.add_edge("c", "d", 3)
	graphHolder.add_edge("c", "e", 3)
	graphHolder.add_edge("c", "f", 3)
	graphHolder.add_edge("e", "h", 3)
	graphHolder.add_edge("g", "h", 3)

	print graphHolder.bfs('a')
