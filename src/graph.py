import random

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
        vertex_1 = Vertex('v1', color='rgb(255, 0, 0)', x=40, y=40)
        vertex_2 = Vertex('v2', color='blue', x=140, y=140)
        vertex_3 = Vertex('v3', color='green', x=300, y=400)
        vertex_4 = Vertex('v4', color='gold', x=400, y=200)
        vertex_5 = Vertex('v5', color='purple', x=100, y=400)

        vertex_1.edges.append(Edge(vertex_2))
        vertex_1.edges.append(Edge(vertex_3))

        vertex_2.edges.append(Edge(vertex_1))
        vertex_2.edges.append(Edge(vertex_4))

        vertex_4.edges.append(Edge(vertex_1))
        vertex_5.edges.append(Edge(vertex_4))

        vertex_list = [vertex_1, vertex_2, vertex_3, vertex_4, vertex_5]
        self.vertexes.extend(vertex_list)

    def bfs(self, start):
        random_color = f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0)

        return found

