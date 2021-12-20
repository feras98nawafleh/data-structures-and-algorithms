from graphs import __version__
from graphs.graphs import Graph
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_add_node():
    graph = Graph()
    expected = 1
    actual = graph.add_node(1).value
    assert expected == actual

def test_add_edge():
    graph = Graph()
    vertex1 = graph.add_node(1)
    vertex2 = graph.add_node(2)
    graph.add_edge(vertex1, vertex2)

    expected = 2
    actual =(graph.get_neighbors(vertex1))[0].vertex.value
    assert expected == actual


def test_collection_of_nodes(graph):
    expected = [1, 2, 3, 4]
    actual = graph.bfs(vertex1)
    assert expected ==  actual

def test_get_neighbors():
    graph = Graph()
    vertex1 = graph.add_node(1)
    vertex2 = graph.add_node(2)
    vertex3 = graph.add_node(3)
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex1, vertex3)

    expected = [2, 3]
    actual = [graph.adjacent_list[vertex1][0].vertex.value, graph.adjacent_list[vertex1][1].vertex.value]
    assert expected ==  actual

def test_get_neighbors_weight():
    graph = Graph()
    vertex1 = graph.add_node(1)
    vertex2 = graph.add_node(2)
    vertex3 = graph.add_node(3)
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex1, vertex3)

    expected = [0, 0]
    actual = [graph.adjacent_list[vertex1][0].weight, graph.adjacent_list[vertex1][1].weight]
    assert expected ==  actual

def test_size(graph):
    expected = 4
    actual = graph.size()
    assert expected == actual

def test_graph_with_one_node_and_edge():
    graph = Graph()
    vertex1 = graph.add_node(1)
    graph.add_edge(vertex1, vertex1)
    expected = 1
    actual = graph.adjacent_list[vertex1][0].vertex.value
    assert actual ==  expected

def test_empty_graph():
    graph = Graph()
    expected = None
    actual = graph.get_nodes()
    assert expected == actual

@pytest.fixture
def graph():
    graph = Graph()
    global vertex1
    vertex1 = graph.add_node(1)
    vertex2 = graph.add_node(2)
    vertex3 = graph.add_node(3)
    vertex4 = graph.add_node(4)
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex1, vertex3)
    graph.add_edge(vertex1, vertex4)
    return graph

def test_one_true_trip(trip):

    actual = graph_trip_cost(trip[0], [trip[1],trip[2]])
    expected = "True, $150"
    assert actual == expected

def test_false_trip(trip):

    actual = graph_trip_cost(trip[0], [trip[1],trip[2],trip[3]])
    expected = 'False, $0'
    assert actual == expected

def test_more_than_one_trip(trip):

    actual = graph_trip_cost(trip[0], [trip[1],trip[2],trip[4]])
    expected = 'True, $192'
    assert actual == expected


@pytest.fixture
def trip():
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

    return graph , pan, are, nab ,mon
