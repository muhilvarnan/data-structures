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
		self.start_node = None

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

	def set_start_node(self, node):
		"""
		set start node
		"""
		self.start_node = node

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

class InputData(object):
	"""
	Input Data fetch
	"""
	def __init__(self):
		try:
			self.queries = raw_input()
			self.edge_weight = 6
			self.graphs = []
			for i in range(0, int(self.queries)):
				graphHolder = GraphHolder()
				nodes, edges = raw_input().split(' ')
				for node in range(1, int(nodes)+1):
					graphHolder.add_vertex(node)
				for edge in range(0, int(edges)):
					start, end = raw_input().split(' ')
					graphHolder.add_edge(int(start), int(end), self.edge_weight)
                		start_node = raw_input()
				graphHolder.set_start_node(int(start_node))
				self.graphs.append(graphHolder)
		except Exception, e:
			print e

	def process(self):
		"""
		process Data
		"""
		try:
			for graph in self.graphs:
				costs = []
				for vertex in range(1, graph.vertex_count+1):
					if vertex != graph.start_node:
						try:
							bfs_path = next(graph.bfs_path(graph.start_node, vertex))
						except StopIteration, e:
							bfs_path = None
						if bfs_path:
							cost = str((len(bfs_path)-1)*self.edge_weight)
						else:
							cost = str(-1)
						costs.append(cost)
				print ' '.join(costs)
		except Exception, e:
			print e

inputObj = InputData()
inputObj.process()