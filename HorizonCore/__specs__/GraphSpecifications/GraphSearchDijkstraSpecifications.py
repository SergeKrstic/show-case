import unittest

from HorizonCore.Graph.GraphSearchDijkstra import GraphSearchDijkstra
from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph


class GraphSearchDijkstraSpecifications(unittest.TestCase):
    def test_SpecifyThatAGraphCanBeSearchUsingDijkstraAlgorithm(self):
        graph = self.CreateGraphGrid()
        dijkstra = GraphSearchDijkstra(graph, sourceNodeIndex=0, targetNodeIndex=8)

        dijkstra.PrintStats("Result")

        self.assertEqual([0, 3, 7, 8], list(dijkstra.GetPathToTarget()), "GetPathToTarget")

        self.assertAlmostEqual(170.71, dijkstra.GetCostToTarget(), 1, "GetCostToTarget")
        self.assertAlmostEqual(100.00, dijkstra.GetCostToNode(0), 1, "GetCostToNode(0)")
        self.assertAlmostEqual(125.00, dijkstra.GetCostToNode(1), 1, "GetCostToNode(1)")
        self.assertAlmostEqual(250.00, dijkstra.GetCostToNode(2), 1, "GetCostToNode(2)")
        self.assertAlmostEqual(50.000, dijkstra.GetCostToNode(3), 1, "GetCostToNode(3)")
        self.assertAlmostEqual(175.00, dijkstra.GetCostToNode(4), 1, "GetCostToNode(4)")
        self.assertAlmostEqual(191.42, dijkstra.GetCostToNode(5), 1, "GetCostToNode(5)")
        self.assertAlmostEqual(175.00, dijkstra.GetCostToNode(6), 1, "GetCostToNode(6)")
        self.assertAlmostEqual(120.71, dijkstra.GetCostToNode(7), 1, "GetCostToNode(7)")
        self.assertAlmostEqual(170.71, dijkstra.GetCostToNode(8), 1, "GetCostToNode(8)")

        self.assertEqual(9, len(dijkstra._shortestPathTree), "len(_shortestPathTree)")
        self.assertEqual(3, dijkstra._shortestPathTree[0].From, "_shortestPathTree[0]")
        self.assertEqual(0, dijkstra._shortestPathTree[1].From, "_shortestPathTree[1]")
        self.assertEqual(None, dijkstra._shortestPathTree[2], "_shortestPathTree[2]")
        self.assertEqual(0, dijkstra._shortestPathTree[3].From, "_shortestPathTree[3]")
        self.assertEqual(None, dijkstra._shortestPathTree[4], "_shortestPathTree[4]")
        self.assertEqual(None, dijkstra._shortestPathTree[5], "_shortestPathTree[5]")
        self.assertEqual(None, dijkstra._shortestPathTree[6], "_shortestPathTree[6]")
        self.assertEqual(3, dijkstra._shortestPathTree[7].From, "_shortestPathTree[7]")
        self.assertEqual(7, dijkstra._shortestPathTree[8].From, "_shortestPathTree[8]")

        self.assertEqual(9, len(dijkstra._searchFrontier), "len(_searchFrontier)")
        self.assertEqual(3, dijkstra._searchFrontier[0].From, "_searchFrontier[0]")
        self.assertEqual(0, dijkstra._searchFrontier[1].From, "_searchFrontier[1]")
        self.assertEqual(1, dijkstra._searchFrontier[2].From, "_searchFrontier[2]")
        self.assertEqual(0, dijkstra._searchFrontier[3].From, "_searchFrontier[3]")
        self.assertEqual(3, dijkstra._searchFrontier[4].From, "_searchFrontier[4]")
        self.assertEqual(7, dijkstra._searchFrontier[5].From, "_searchFrontier[5]")
        self.assertEqual(3, dijkstra._searchFrontier[6].From, "_searchFrontier[6]")
        self.assertEqual(3, dijkstra._searchFrontier[7].From, "_searchFrontier[7]")
        self.assertEqual(7, dijkstra._searchFrontier[8].From, "_searchFrontier[8]")

    def test_SpecifyThatNoPathIsReturnedWhenTargetNotSupplied(self):
        graph = self.CreateGraphGrid()
        dijkstra = GraphSearchDijkstra(graph, sourceNodeIndex=0)

        self.assertEqual([], list(dijkstra.GetPathToTarget()), "GetPathToTarget")

    @staticmethod
    def CreateGraphGrid():
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)
        GraphTools.WeightNavGraphNodeEdges(graph, nodeIndex=1, weight=2.5)
        GraphTools.WeightNavGraphNodeEdges(graph, nodeIndex=4, weight=2.5)
        GraphTools.WeightNavGraphNodeEdges(graph, nodeIndex=6, weight=2.5)
        return graph
