# Graphs
Graphs are data structure consists of nodes, each nodes holds a value and might or might not be connected to other nodes in graph, the link between nodes is called an edge, and the linked nodes for a node are called its neighbors.

## Challenge
Create the class for the graph and methods to add nodes, edges, find size, and find neighbors

## Approach & Efficiency
Except for traversing, all methods have O(1) big o for time and space as the space and time consumed will be alwas the same, for traversing the big O might grow up to O (n*h) where n is the size of the graph and h is the max number of neighbors a node might have

## API

add_node:

    Input : Value

    What is doing : add node to the Graph

    Return : node
add_edge:

    Input: start_vertex, end_vertex , weight:optional

    What is doing: Creat an edge and append the edge to the value of

    start_vertex inside the adj_list

    Return: None

get_neighbors:

    Input : Vertex

    What is doing: Get all neighbors for a vertex

    Return: a list of edges

get_nodes

    Input : None

    What is doing : get all the nodes in the graph as a set or list

    Return : a list or set of the nodes

size

    Input: None

    What is doing: find the length of the adj_list

    Return: int The size(the length of adj_list)
