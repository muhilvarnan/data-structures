"""
Graphs Implementations

Graph structure

graphHolder = {
  "a": Vertex("a", {b, c}),
  "b": Vertex("b", {a, c})
  "c": Vertex("c")
}
"""

class Vertex(object):

    def __init__(self, node):
        self.id = node
        self.adjacent_vertices = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' +  str([x.id for x in self.adjacent_vertices])

    def add_adjacent(self, node, weight=0):
        self.adjacent_vertices[node] = weight

    def get_connections(self):
        return self.adjacent_vertices.keys()

    def get_id(self):
        return self.id

    def get_weight(self, node):
        return self.adjacent_vertices[node]
class GraphHolder(object):

    def __init__(self,):
        self.vertices = {}
        self.vertex_count = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.vertex_count = self.vertex_count + 1
        self.vertices[node] = Vertex(node)
        return self.vertices[node]

    def add_edge(self, start, end, weight):
        self.vertices[start].add_adjacent(self.vertices[end], weight)

        self.vertices[end].add_adjacent(self.vertices[start], weight)

if __name__ == '__main__':

    graphHolder = GraphHolder()
    graphHolder.add_vertex('a')
    graphHolder.add_vertex('b')
    graphHolder.add_vertex('c')
    graphHolder.add_edge('a', 'b', 10)
    graphHolder.add_edge('b', 'c', 10)
    for vertex in graphHolder:
        for w in vertex.get_connections():
            print '%s %s %d' % (vertex.get_id(), w.get_id(), vertex.get_weight(graphHolder.vertices[w.get_id()]))
    for vertex in graphHolder:
            print graphHolder.vertices[vertex.get_id()]
