from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

    def count(self):
        return self.dq.count()

class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.__adj_list = {}
        self.adjacent_list = self.__adj_list

    def add_node(self, value):
        node = Vertex(value)
        self.__adj_list[node] = []
        return node

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start Vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End Vertex is not found")
        edge = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge)

    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])

    def get_nodes(self):
        if len(self.__adj_list.keys()) < 1:
            return None
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def bfs(self, start_vertex):
        queue = Queue()
        result = []
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)

        while len(queue):
            current_vertex = queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)

        return result

    # Continue challenge 36
    def bfs(self, start_vertex):
        queue = Queue()
        result = []
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        result.append(start_vertex.value)

        while len(queue):
            current_vertex = queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor.value)

        return result

# Continue challenge 37
    def graph_trip_cost(self, graph, cities):

        self.graph = graph

        trip = False
        next_trip = False
        cost = 0


        for city_index in range(len(cities) - 1):
            neighbors = self.__adj_list[cities[city_index]]
            next_trip = False

            for neighbor in neighbors:
                if cities[city_index + 1] == neighbor.vertex:
                    cost += neighbor.weight
                    trip = True
                    next_trip = True

        trip = trip and next_trip

        if not trip:
            cost = 0
            
        result = f'{trip}, ${cost}'
        return result




if __name__ == "__main__":
    graph = Graph()

    pan = graph.add_node('Pandora')
    nab = graph.add_node('Naboo')
    nar = graph.add_node('Narnia')
    mon = graph.add_node('Monstroplolis')
    are = graph.add_node('Arendelle')
    met = graph.add_node('Metroville')

    graph.add_edge(pan, are, 150)
    graph.add_edge(pan, met, 82)
    graph.add_edge(are, pan, 150)
    graph.add_edge(are, met, 99)
    graph.add_edge(are, mon, 42)
    graph.add_edge(met, pan, 82)
    graph.add_edge(met, are, 99)
    graph.add_edge(met, mon, 105)
    graph.add_edge(met, nab, 26)
    graph.add_edge(met, nar, 37)
    graph.add_edge(mon, are, 42)
    graph.add_edge(mon, met, 105)
    graph.add_edge(mon, nab, 73)
    graph.add_edge(nab, mon, 73)
    graph.add_edge(nab, met, 26)
    graph.add_edge(nab, nar, 250)
    graph.add_edge(nar, met, 37)
    graph.add_edge(nar, nab, 250)

    print(graph.graph_trip_cost(graph, [met, nab, nar]))

# graph = Graph()
# vertex1 = graph.add_node('Pandora')
# vertex2 = graph.add_node('Arendelle')
# vertex3 = graph.add_node('Metroville')
# vertex4 = graph.add_node('Monstroplolis')
# vertex5 = graph.add_node('Narnia')
# vertex6 = graph.add_node('Naboo')
# graph.add_edge(vertex1, vertex2)
# graph.add_edge(vertex2, vertex3)
# graph.add_edge(vertex2, vertex4)
# graph.add_edge(vertex3, vertex4)
# graph.add_edge(vertex3, vertex5)
# graph.add_edge(vertex4, vertex5)
# graph.add_edge(vertex4, vertex6)

# # ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
# print(graph.bfs(vertex1))
