from node import Node
from queue import Queue
from collections import deque


class Graph:
    adj_list = None

    def __init__(self, adj_list):
        self.adj_list = adj_list

    @staticmethod
    def bread_first_search(start):
        node_q = Queue()
        node_q.put(start)
        visited = set()

        while not node_q.empty():
            node = node_q.get()
            if node not in visited:
                yield node
                visited.add(node)
                node_q.queue.extend(node.getNeighbours() - visited)

    @staticmethod
    def bread_first_search_path(start, end):
        node_q = Queue()
        node_q.put((start, [start]))
        visited = {start}

        while not node_q.empty():
            parent, path = node_q.get()
            for child in parent.getNeighbours():
                if child not in visited:
                    if child == end:
                        yield path + [child]
                    else:
                        visited.add(child)
                        node_q.put((child, path + [child]))

    @staticmethod
    def depth_first_search(start, visited=None):
        node_s = deque()
        node_s.append(start)
        if visited is None:
            visited = set()
        while node_s:
            node = node_s.pop()
            if node not in visited:
                yield node
                visited.add(node)
                node_s.extend(node.getNeighbours() - visited)

    def connected_component(self):
        count = 0
        visited = set()
        connected_component = []
        for node in self.adj_list:
            if node not in visited:
                count += 1
                nodes = list(self.bread_first_search(node))
                for n in nodes:
                    visited.add(n)
                connected_component.append(nodes)
        return count, connected_component


if __name__ == "__main__":
    nA = Node('A')
    nB = Node('B')
    nC = Node('C')
    nD = Node('D')
    nE = Node('E')
    nF = Node('F')
    nG = Node('G')

    nA.addNeighbours([nB, nC])
    nB.addNeighbours([nA, nD, nE])
    nC.addNeighbours([nA, nF])
    nD.addNeighbours(nB)
    nE.addNeighbours([nB, nF, nG])
    nF.addNeighbours([nC, nE])
    graph = Graph([nA, nB, nC, nD, nE, nF])
    bfs_nodes = list(graph.bread_first_search(nA))
    print("Bread First Search : ", bfs_nodes)
    bfs_nodes_path = list(graph.bread_first_search_path(nB, nF))
    print("Path from {} to {} :{}".format(nB, nF, bfs_nodes_path))
    dfs_nodes = list(graph.depth_first_search(nA))
    print("Depth First Search : ", dfs_nodes)
    size, components = graph.connected_component()
    print("number of connected components :", size)
    for c in components:
        print(c)
