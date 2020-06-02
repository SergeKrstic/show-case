import numpy as np
import unittest

from HorizonCore.Graph.GraphSearchMinSpanningTree import GraphSearchMinSpanningTree
from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph


class GraphSearchMinSpanningTreeSpecifications(unittest.TestCase):
    def test_SpecifyThatAGraphCanBeSearchUsingMinSpanningTreeAlgorithm(self):
        graph = self.CreateGraphGrid()
        aStar = GraphSearchMinSpanningTree(graph, sourceNodeIndex=4)

        aStar.PrintStats("Result")

        np.testing.assert_almost_equal([50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0], aStar._costToThisNode, 1, "_costToThisNode")

        self.assertEqual(9, len(aStar._spanningTree), "len(_spanningTree)")
        self.assertEqual(1, aStar._spanningTree[0].From, "_spanningTree[0]")
        self.assertEqual(4, aStar._spanningTree[1].From, "_spanningTree[1]")
        self.assertEqual(1, aStar._spanningTree[2].From, "_spanningTree[2]")
        self.assertEqual(4, aStar._spanningTree[3].From, "_spanningTree[3]")
        self.assertEqual(1, aStar._spanningTree[4].From, "_spanningTree[4]")
        self.assertEqual(4, aStar._spanningTree[5].From, "_spanningTree[5]")
        self.assertEqual(3, aStar._spanningTree[6].From, "_spanningTree[6]")
        self.assertEqual(4, aStar._spanningTree[7].From, "_spanningTree[7]")
        self.assertEqual(5, aStar._spanningTree[8].From, "_spanningTree[8]")

        self.assertEqual(9, len(aStar._fringe), "len(_fringe)")
        self.assertEqual(1, aStar._fringe[0].From, "_fringe[0]")
        self.assertEqual(4, aStar._fringe[1].From, "_fringe[1]")
        self.assertEqual(1, aStar._fringe[2].From, "_fringe[2]")
        self.assertEqual(4, aStar._fringe[3].From, "_fringe[3]")
        self.assertEqual(1, aStar._fringe[4].From, "_fringe[4]")
        self.assertEqual(4, aStar._fringe[5].From, "_fringe[5]")
        self.assertEqual(3, aStar._fringe[6].From, "_fringe[6]")
        self.assertEqual(4, aStar._fringe[7].From, "_fringe[7]")
        self.assertEqual(5, aStar._fringe[8].From, "_fringe[8]")

    def test_SpecifyThatMinSpanningTreeAlgorithmReturnsAForestWhenNoSourceNodeIndexIsSupplied(self):
        graph = self.CreateGraphGrid()
        aStar = GraphSearchMinSpanningTree(graph, sourceNodeIndex=-1)

        # aStar.PrintStats("Result")
        
        np.testing.assert_almost_equal([50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0], aStar._costToThisNode, 1, "_costToThisNode")
        
        self.assertEqual(9, len(aStar._spanningTree), "len(_spanningTree)")
        self.assertEqual(1, aStar._spanningTree[0].From, "_spanningTree[0]")
        self.assertEqual(0, aStar._spanningTree[1].From, "_spanningTree[1]")
        self.assertEqual(1, aStar._spanningTree[2].From, "_spanningTree[2]")
        self.assertEqual(0, aStar._spanningTree[3].From, "_spanningTree[3]")
        self.assertEqual(1, aStar._spanningTree[4].From, "_spanningTree[4]")
        self.assertEqual(2, aStar._spanningTree[5].From, "_spanningTree[5]")
        self.assertEqual(3, aStar._spanningTree[6].From, "_spanningTree[6]")
        self.assertEqual(4, aStar._spanningTree[7].From, "_spanningTree[7]")
        self.assertEqual(5, aStar._spanningTree[8].From, "_spanningTree[8]")
        
        self.assertEqual(9, len(aStar._fringe), "len(_fringe)")
        self.assertEqual(1, aStar._fringe[0].From, "_fringe[0]")
        self.assertEqual(0, aStar._fringe[1].From, "_fringe[1]")
        self.assertEqual(1, aStar._fringe[2].From, "_fringe[2]")
        self.assertEqual(0, aStar._fringe[3].From, "_fringe[3]")
        self.assertEqual(1, aStar._fringe[4].From, "_fringe[4]")
        self.assertEqual(2, aStar._fringe[5].From, "_fringe[5]")
        self.assertEqual(3, aStar._fringe[6].From, "_fringe[6]")
        self.assertEqual(4, aStar._fringe[7].From, "_fringe[7]")
        self.assertEqual(5, aStar._fringe[8].From, "_fringe[8]")

    @staticmethod
    def CreateGraphGrid():
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)
        return graph
