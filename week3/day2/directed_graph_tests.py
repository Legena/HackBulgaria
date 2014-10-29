import unittest

from directed_graph import DirectedGraph


class DirectedGraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.addEdge("Pesho", "Ivo")
        self.graph.addEdge("Ivan", "Ivo")
        self.graph.addEdge("Gosho", "Ivo")
        self.graph.addEdge("Ivan", "Pesho")
        self.graph.addEdge("Ivo", "Ivan")

    def test_add_edge(self):
        self.assertEqual(len(self.graph.graph), 4)

    def test_get_neighbors(self):
        self.assertEqual(len(self.graph.graph['Ivan']), 2)

    def test_path_between(self):
        self.assertTrue(self.graph.pathBetween("Pesho", "Ivo"))
        self.assertTrue(self.graph.pathBetween("Ivo", "Pesho"))
        self.assertFalse(self.graph.pathBetween("Ivan", "Gosho"))

    def test_to_string(self):
        test_string = self.graph.toString()
        self.assertEqual(len(test_string), 71)

if __name__ == '__main__':
    unittest.main()