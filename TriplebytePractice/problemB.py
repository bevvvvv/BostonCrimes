# input
# row and column
params = input().split()
rows = int(params[0])
cols = int(params[1])

# Graph Data Structure
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        #self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


# Create graph from input
# Node names are row col pair: r1c2
# Incoming edges weights are value of mud height
grid = []
for i in range(rows):
    values = input().split()
    values = list(map(int, values))
    grid.append(values)
g = Graph()
for r in range(rows):
    for c in range(cols):
        # create vertex
        node_name = 'r'+str(r)+'c'+str(c)
        g.add_vertex(node_name)

for r in range(rows):
    for c in range(cols):
        # create incoming edges
        node_name = 'r'+str(r)+'c'+str(c)
        # North
        if r > 0:
            source = 'r'+str(r-1)+'c'+str(c)
            g.add_edge(source, node_name, grid[r][c])
        # South
        if r < rows - 1:
            source = 'r'+str(r+1)+'c'+str(c)
            g.add_edge(source, node_name, grid[r][c])
        # East 
        if c < cols - 1:
            source = 'r'+str(r)+'c'+str(c+1)
            g.add_edge(source, node_name, grid[r][c])
        # West
        if c > 0:
            source = 'r'+str(r)+'c'+str(c-1)
            g.add_edge(source, node_name, grid[r][c])

import pdb
pdb.set_trace()

