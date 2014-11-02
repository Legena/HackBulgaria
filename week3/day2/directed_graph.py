class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, nodeA, nodeB):
        if not nodeB in self.graph:
                self.graph[nodeB] = []
        if nodeA in self.graph:
            self.graph[nodeA].append(nodeB)
        else:
            self.graph[nodeA] = []
            self.graph[nodeA].append(nodeB)

    def get_neighborsFor(self, node):
        return self.graph[node]

    def path_between(self, nodeA, nodeB):
        visited = set()
        return self.path_exists(nodeA, nodeB, visited)

    def steps_between(self, nodeA, nodeB):
        visited = set()
        self.path_exists(nodeA, nodeB, visited)
        return len(visited) - 1

    def path_exists(self, nodeA, nodeB, visited):
        visited.add(nodeA)
        if nodeA == nodeB:
            return True
        for node in self.graph[nodeA]:
            if node not in visited:
                visited.add(node)
                return self.path_exists(node, nodeB, visited)
        return False

    def __str__(self):
        stringified = ""
        for node in self.graph:
            stringified += "{} : {}\n".format(node, self.graph[node])
        return stringified