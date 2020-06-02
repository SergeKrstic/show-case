import numpy
import unittest

from HorizonCore.Graph.AStarHeuristicPolicies import Heuristic, HeuristicEuclidean, HeuristicNoisyEuclidean, \
    HeuristicDijkstra, HeuristicManhattan, HeuristicEuclideanSquared, HeuristicNoisyEuclideanSquared
from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph


class GraphSearchBFSSpecifications(unittest.TestCase):
    def test_SpecifyThatCallingCalculateOnAbstractHeuristicRaisesAnException(self):
        graph = self.CreateGraphGrid()
        self.assertRaises(NotImplementedError, Heuristic.Calculate, graph, 1, 2)

    def test_SpecifyThatEuclideanHeuristicCanBeCalculated(self):
        graph = self.CreateGraphGrid()
        self.assertAlmostEqual(50.00, HeuristicEuclidean.Calculate(graph, 1, 2), 2, "heuristic 1")
        self.assertAlmostEqual(70.71, HeuristicEuclidean.Calculate(graph, 1, 5), 2, "heuristic 1")

    def test_SpecifyThatNoisyEuclideanHeuristicCanBeCalculated(self):
        graph = self.CreateGraphGrid()
        numpy.random.seed(0)
        self.assertAlmostEqual(50.488, HeuristicNoisyEuclidean.Calculate(graph, 1, 2), 2, "heuristic 1")
        self.assertAlmostEqual(73.753, HeuristicNoisyEuclidean.Calculate(graph, 1, 5), 2, "heuristic 2")

    def test_SpecifyThatDijkstraHeuristicCanBeCalculated(self):
        graph = self.CreateGraphGrid()
        self.assertAlmostEqual(0, HeuristicDijkstra.Calculate(graph, 1, 2), 2, "heuristic 1")
        self.assertAlmostEqual(0, HeuristicDijkstra.Calculate(graph, 1, 5), 2, "heuristic 2")

    def test_SpecifyThatManhattanHeuristicCanBeCalculated(self):
        graph = self.CreateGraphGrid()
        self.assertAlmostEqual(50, HeuristicManhattan.Calculate(graph, 1, 2), 2, "heuristic 1")
        self.assertAlmostEqual(100, HeuristicManhattan.Calculate(graph, 1, 5), 2, "heuristic 2")

    def test_SpecifyThatEuclideanSquaredHeuristicCanBeCalculated(self):
        graph = self.CreateGraphGrid()
        self.assertAlmostEqual(2500.0, HeuristicEuclideanSquared.Calculate(graph, 1, 2), 2, "heuristic 1")
        self.assertAlmostEqual(5000.0, HeuristicEuclideanSquared.Calculate(graph, 1, 5), 2, "heuristic 2")

    def test_SpecifyThatNoisyEuclideanSquaredHeuristicCanBeCalculated(self):
        graph = self.CreateGraphGrid()
        numpy.random.seed(0)
        self.assertAlmostEqual(2524.406, HeuristicNoisyEuclideanSquared.Calculate(graph, 1, 2), 2, "heuristic 1")
        self.assertAlmostEqual(5215.189, HeuristicNoisyEuclideanSquared.Calculate(graph, 1, 5), 2, "heuristic 2")

    @staticmethod
    def CreateGraphGrid():
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)
        return graph
