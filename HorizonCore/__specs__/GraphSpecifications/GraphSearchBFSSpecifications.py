import unittest

from HorizonCore.Graph.GraphSearchBFS import GraphSearchBFS
from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph


class GraphSearchBFSSpecifications(unittest.TestCase):
    def test_SpecifyThatAGraphCanBeSearchUsingDepthFirstSearchAlgorithm(self):
        graph = self.CreateGraphGrid()
        bfs = GraphSearchBFS(graph, sourceNodeIndex=0, targetNodeIndex=8)

        bfs.PrintStats("Result")

        self.assertEqual(True, bfs.Found(), "Found")
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1, 1], bfs._visited, "_visited")
        self.assertEqual([0, 0, 1, 0, 0, 1, 3, 3, 4], bfs._routeNodeToParent, "_routeNodeToParent")
        self.assertEqual([0, 4, 8], list(bfs.GetPathToTarget()), "GetPathToTarget")

        self.assertEqual(8, len(bfs._spanningTree), "len(_spanningTree)")
        self.assertEqual(1, bfs._spanningTree[0].To, "_spanningTree[0]")
        self.assertEqual(3, bfs._spanningTree[1].To, "_spanningTree[1]")
        self.assertEqual(4, bfs._spanningTree[2].To, "_spanningTree[2]")
        self.assertEqual(2, bfs._spanningTree[3].To, "_spanningTree[3]")
        self.assertEqual(5, bfs._spanningTree[4].To, "_spanningTree[4]")
        self.assertEqual(6, bfs._spanningTree[5].To, "_spanningTree[5]")
        self.assertEqual(7, bfs._spanningTree[6].To, "_spanningTree[6]")
        self.assertEqual(8, bfs._spanningTree[7].To, "_spanningTree[7]")

    def test_SpecifyThatTargetFoundCanBeDetermined(self):
        graph = self.CreateGraphGrid()

        dfs = GraphSearchBFS(graph, sourceNodeIndex=0, targetNodeIndex=8)
        self.assertEqual(True, dfs.Found(), "Found 1")
        self.assertEqual([0, 4, 8], list(dfs.GetPathToTarget()), "GetPathToTarget 1")

        dfs = GraphSearchBFS(graph, sourceNodeIndex=0, targetNodeIndex=-1)
        self.assertEqual(False, dfs.Found(), "Found 2")
        self.assertEqual([], list(dfs.GetPathToTarget()), "GetPathToTarget 2")

    @staticmethod
    def CreateGraphGrid():
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)
        return graph
