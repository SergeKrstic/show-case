import numpy as np
import unittest

from HorizonCore.Graph.AStarHeuristicPolicies import HeuristicEuclidean
from HorizonCore.Graph.GraphSearchAStar import GraphSearchAStar
from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph


class GraphSearchAStarSpecifications(unittest.TestCase):
    def test_SpecifyThatAGraphCanBeSearchUsingAStarAlgorithm(self):
        graph = self.CreateGraphGrid()
        aStar = GraphSearchAStar(graph, sourceNodeIndex=0, targetNodeIndex=8, heuristic=HeuristicEuclidean)

        aStar.PrintStats("Result")

        self.assertEqual([0, 3, 7, 8], list(aStar.GetPathToTarget()), "GetPathToTarget")

        np.testing.assert_almost_equal(170.71, aStar.GetCostToTarget(), 1, "GetCostToNode")
        np.testing.assert_almost_equal([100.0, 125.0, 0, 50.0, 175.0, 191.4, 175.0, 120.7, 170.7], aStar._gCosts, 1, "_gCosts")
        np.testing.assert_almost_equal([241.4, 236.8, 0, 161.8, 245.7, 241.4, 275.0, 170.7, 170.7], aStar._fCosts, 1, "_fCosts")

        self.assertEqual(9, len(aStar._shortestPathTree), "len(_shortestPathTree)")
        self.assertEqual(None, aStar._shortestPathTree[0], "_shortestPathTree[0]")
        self.assertEqual(None, aStar._shortestPathTree[1], "_shortestPathTree[1]")
        self.assertEqual(None, aStar._shortestPathTree[2], "_shortestPathTree[2]")
        self.assertEqual(0, aStar._shortestPathTree[3].From, "_shortestPathTree[3]")
        self.assertEqual(None, aStar._shortestPathTree[4], "_shortestPathTree[4]")
        self.assertEqual(None, aStar._shortestPathTree[5], "_shortestPathTree[5]")
        self.assertEqual(None, aStar._shortestPathTree[6], "_shortestPathTree[6]")
        self.assertEqual(3, aStar._shortestPathTree[7].From, "_shortestPathTree[7]")
        self.assertEqual(7, aStar._shortestPathTree[8].From, "_shortestPathTree[8]")

        self.assertEqual(9, len(aStar._searchFrontier), "len(_searchFrontier)")
        self.assertEqual(3, aStar._searchFrontier[0].From, "_searchFrontier[0]")
        self.assertEqual(0, aStar._searchFrontier[1].From, "_searchFrontier[1]")
        self.assertEqual(None, aStar._searchFrontier[2], "_searchFrontier[2]")
        self.assertEqual(0, aStar._searchFrontier[3].From, "_searchFrontier[3]")
        self.assertEqual(3, aStar._searchFrontier[4].From, "_searchFrontier[4]")
        self.assertEqual(7, aStar._searchFrontier[5].From, "_searchFrontier[5]")
        self.assertEqual(3, aStar._searchFrontier[6].From, "_searchFrontier[6]")
        self.assertEqual(3, aStar._searchFrontier[7].From, "_searchFrontier[7]")
        self.assertEqual(7, aStar._searchFrontier[8].From, "_searchFrontier[8]")

    def test_SpecifyThatNoPathIsReturnedWhenTargetNotSupplied(self):
        graph = self.CreateGraphGrid()
        aStar = GraphSearchAStar(graph, sourceNodeIndex=0, targetNodeIndex=-1, heuristic=HeuristicEuclidean)

        self.assertEqual([], list(aStar.GetPathToTarget()), "GetPathToTarget")

    @staticmethod
    def CreateGraphGrid():
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)
        GraphTools.WeightNavGraphNodeEdges(graph, nodeIndex=1, weight=2.5)
        GraphTools.WeightNavGraphNodeEdges(graph, nodeIndex=4, weight=2.5)
        GraphTools.WeightNavGraphNodeEdges(graph, nodeIndex=6, weight=2.5)
        return graph
