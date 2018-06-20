class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value, color, **pos):
        self.value = value
        self.color = color
        self.pos = pos
        self.edges = []


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        vertex_1 = Vertex('v1', color='red', x=40, y=40)
        vertex_2 = Vertex('v2', color='blue', x=140, y=140)
        vertex_3 = Vertex('v3', color='green', x=300, y=400)
        vertex_4 = Vertex('v4', color='yellow', x=400, y=200)
        vertex_5 = Vertex('v5', color='purple', x=100, y=400)

        vertex_1.edges.append(Edge(vertex_2))
        vertex_1.edges.append(Edge(vertex_3))

        vertex_2.edges.append(Edge(vertex_1))
        vertex_2.edges.append(Edge(vertex_4))

        vertex_4.edges.append(Edge(vertex_1))
        vertex_5.edges.append(Edge(vertex_4))

        vertex_list = [vertex_1, vertex_2, vertex_3, vertex_4, vertex_5]
        self.vertexes.extend(vertex_list)

