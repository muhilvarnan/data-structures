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

    def __init__(self, node):
        self.id = node
        self.adjacent_vertices = {}


    def add_adjacent(self, node, weight=0):
        key =node.get_id()
        self.adjacent_vertices[key] = weight

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

    def dfs(self, start, visited=None):
        if visited == None:
            visited = []
        visited.append(start)
        diff = [x for x in self.vertices[start].get_connections() if x not in set(visited)]
        for next in diff:
            self.dfs(next, visited)
        return visited

    def dfs_paths(self, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in set(self.vertices[start].get_connections()) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))


if __name__ == '__main__':

    graphHolder = GraphHolder()
    graphHolder.add_vertex('a')
    graphHolder.add_vertex('b')
    graphHolder.add_vertex('c')
    graphHolder.add_vertex('d')
    graphHolder.add_vertex('e')
    graphHolder.add_vertex('f')

    graphHolder.add_edge('a', 'b', 0)
    graphHolder.add_edge('a', 'c', 0)
    graphHolder.add_edge('b', 'd', 0)
    graphHolder.add_edge('b', 'e', 0)
    graphHolder.add_edge('c', 'f', 0)
    graphHolder.add_edge('e', 'f', 0)

    for vertex in graphHolder:
        for w in vertex.get_connections():
            print '%s %s %d' % (vertex.get_id(), graphHolder.vertices[w].get_id(), vertex.get_weight(graphHolder.vertices[w].get_id()))
    for vertex in graphHolder:
            print graphHolder.vertices[vertex.get_id()].get_id()

    print graphHolder.dfs('c')
    print list(graphHolder.dfs_paths('a','f'))