class Node:

    def __init__(self, value):
        self.neighbours = set()

        self.value = value

    def getNeighbours(self):
        return self.neighbours

    def getNodeValue(self):
        return self.value

    def addNeighbours(self, nodes):
        if isinstance(nodes, list):
            self.neighbours.update(nodes)
            for node in nodes:
                node.neighbours.add(self)
        else:
            self.neighbours.add(nodes)
            nodes.neighbours.add(self)

    def isNeighbours(self, node):
        return self.exist(node, self.neighbours)

    def hasNeighbours(self):
        return len(self.neighbours) != 0

    @staticmethod
    def exist(elem, items):
        exist = False
        for item in items:
            if item == elem:
                exist = True
                break
        return exist

    def __str__(self):
        return "Node({})".format(self.value)

    def __repr__(self):
        return "Node({})".format(self.value)


if __name__ == '__main__':
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n0.addNeighbours([n2, n3])
    n1.addNeighbours(n0)
    n2.addNeighbours(n1)
    n3.addNeighbours(n4)
    n4.addNeighbours(n0)

    print("{} neighbours : {}".format(n0, n0.getNeighbours()))
