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
		self.adjecent_vertices = {}

	def add_adjacent(self, node, weight):
		"""
		add ajacent 
		"""
		key = node.getID()
		self.adjecent_vertices[key] = weight

	def getID(self):
		"""
		get id
		"""
		return self.id

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

if __name__ == "__main__":
	graphHolder = GraphHolder()
	graphHolder.add_vertex("a")
	graphHolder.add_vertex("b")
	graphHolder.add_vertex("c")
	graphHolder.add_vertex("d")
	graphHolder.add_vertex("e")
	graphHolder.add_vertex("f")

	graphHolder.add_edge("a", "b", 3)