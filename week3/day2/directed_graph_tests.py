import unittest

from directed_graph import DirectedGraph


class DirectedGraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.add_edge("Pesho", "Ivo")
        self.graph.add_edge("Ivan", "Ivo")
        self.graph.add_edge("Gosho", "Ivo")
        self.graph.add_edge("Ivan", "Pesho")
        self.graph.add_edge("Ivo", "Ivan")

    def test_add_edge(self):
        self.assertEqual(len(self.graph.graph), 4)

    def test_get_neighbors(self):
        self.assertEqual(len(self.graph.graph['Ivan']), 2)

    def test_path_between(self):
        self.assertTrue(self.graph.path_between("Pesho", "Ivo"))
        self.assertTrue(self.graph.path_between("Ivo", "Pesho"))
        self.assertFalse(self.graph.path_between("Ivan", "Gosho"))

    def test_steps_between(self):
        self.assertEqual(self.graph.steps_between("Pesho", "Pesho"), 0)
        self.assertEqual(self.graph.steps_between("Ivan", "Pesho"), 1)
        self.assertEqual(self.graph.steps_between("Pesho", "Ivan"), 2)
        self.assertEqual(self.graph.steps_between("Gosho", "Pesho"), 3)

    def test_to_string(self):
        test_string = str(self.graph)
        self.assertEqual(len(test_string), 71)

if __name__ == '__main__':
    unittest.main()