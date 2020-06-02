import unittest

from HorizonCore.Graph.GraphSearchDFS import GraphSearchDFS
from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph


class GraphSearchDFSSpecifications(unittest.TestCase):
    def test_SpecifyThatAGraphCanBeSearchUsingDepthFirstSearchAlgorithm(self):
        graph = self.CreateGraphGrid()
        dfs = GraphSearchDFS(graph, sourceNodeIndex=0, targetNodeIndex=2)

        dfs.PrintStats("Result")

        self.assertEqual(True, dfs.Found(), "Found")
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1, 1], dfs._visited, "_visited")
        self.assertEqual([0, 3, 5, 6, 0, 1, 7, 8, 4], dfs._routeNodeToParent, "_routeNodeToParent")
        self.assertEqual([0, 4, 8, 7, 6, 3, 1, 5, 2], list(dfs.GetPathToTarget()), "GetPathToTarget")

        self.assertEqual(8, len(dfs._spanningTree), "len(_spanningTree)")
        self.assertEqual(4, dfs._spanningTree[0].To, "_spanningTree[0]")
        self.assertEqual(8, dfs._spanningTree[1].To, "_spanningTree[1]")
        self.assertEqual(7, dfs._spanningTree[2].To, "_spanningTree[2]")
        self.assertEqual(6, dfs._spanningTree[3].To, "_spanningTree[3]")
        self.assertEqual(3, dfs._spanningTree[4].To, "_spanningTree[4]")
        self.assertEqual(1, dfs._spanningTree[5].To, "_spanningTree[5]")
        self.assertEqual(5, dfs._spanningTree[6].To, "_spanningTree[6]")
        self.assertEqual(2, dfs._spanningTree[7].To, "_spanningTree[7]")

    def test_SpecifyThatTargetFoundCanBeDetermined(self):
        graph = self.CreateGraphGrid()

        dfs = GraphSearchDFS(graph, sourceNodeIndex=0, targetNodeIndex=2)
        self.assertEqual(True, dfs.Found(), "Found 1")
        self.assertEqual([0, 4, 8, 7, 6, 3, 1, 5, 2], list(dfs.GetPathToTarget()), "GetPathToTarget 1")

        dfs = GraphSearchDFS(graph, sourceNodeIndex=0, targetNodeIndex=-1)
        self.assertEqual(False, dfs.Found(), "Found 2")
        self.assertEqual([], list(dfs.GetPathToTarget()), "GetPathToTarget 2")

    @staticmethod
    def CreateGraphGrid():
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)
        return graph
