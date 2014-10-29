class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def addEdge(self, nodeA, nodeB):
        if not nodeB in self.graph:
                self.graph[nodeB] = []
        if nodeA in self.graph:
            self.graph[nodeA].append(nodeB)
        else:
            self.graph[nodeA] = []
            self.graph[nodeA].append(nodeB)

    def getNeighborsFor(self, node):
        return self.graph[node]

    def pathBetween(self, nodeA, nodeB):
        visited = set()
        return self.pathExists(nodeA, nodeB, visited)

    def pathExists(self, nodeA, nodeB, visited):
        visited.add(nodeA)
        if nodeA == nodeB:
            return True
        for node in self.graph[nodeA]:
            if node not in visited:
                visited.add(node)
                return self.pathExists(node, nodeB, visited)
        return False

    def toString(self):
        stringified = ""
        for node in self.graph:
            stringified += "{} : {}\n".format(node, self.graph[node])
        return stringified