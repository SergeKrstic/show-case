import unittest

from HorizonCore.Graph.GraphEdge import GraphEdge
from HorizonCore.Graph.GraphNode import GraphNode
from HorizonCore.Graph.NodeType import NodeType
from HorizonCore.Graph.SparseGraph import SparseGraph
from HorizonCore.__specs__.TestHelpers.TestFactory import TestFactory


class SparseGraphSpecifications(unittest.TestCase):

    def test_SpecifyThatSparseGraphCanBeConstructed(self):
        sparseGraph = SparseGraph(isDigraph=True)

        self.assertEqual(0, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(0, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(0, sparseGraph.GetNextFreeNodeIndex(), "GetNextFreeNodeIndex")
        self.assertEqual(True, sparseGraph.IsDigraph, "IsDigraph")
        self.assertEqual(True, sparseGraph.IsEmpty, "IsEmpty")

    def test_SpecifyThatANodeCanBeAddedToTheGraph(self):
        sparseGraph = SparseGraph(isDigraph=False)
        node = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())

        sparseGraph.AddNode(node)

        self.assertEqual(1, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(1, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(0, len(sparseGraph._edgeListVector[0]), "_edgeListVector")
        self.assertEqual(1, sparseGraph._nextNodeIndex, "_nextNodeIndex")

    def test_SpecifyThatTwoNodesCanBeAddedToTheGraph(self):
        sparseGraph = SparseGraph(isDigraph=False)
        sparseGraph.AddNode(GraphNode(index=sparseGraph.GetNextFreeNodeIndex()))
        sparseGraph.AddNode(GraphNode(index=sparseGraph.GetNextFreeNodeIndex()))

        self.assertEqual(2, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(2, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(0, len(sparseGraph._edgeListVector[0]), "_edgeListVector")
        self.assertEqual(2, sparseGraph._nextNodeIndex, "_nextNodeIndex")

    def test_SpecifyThatANodeCanAddedInplaceOfACurrentlyDeactivatedNode(self):
        sparseGraph = SparseGraph(isDigraph=False)
        nodeIndex = sparseGraph.GetNextFreeNodeIndex()
        node = GraphNode(nodeIndex)

        sparseGraph.AddNode(node)

        self.assertEqual(1, len(sparseGraph._nodes), "_nodes 1")
        self.assertEqual(0, sparseGraph._nodes[nodeIndex].Index, "node.Index 1")

        # Deactivate the node
        node.Index = NodeType.InvalidNodeIndex
        self.assertEqual(NodeType.InvalidNodeIndex.value, sparseGraph._nodes[nodeIndex].Index, "node.Index 2")

        # Add a new node in place of a deactivate node in the graph
        newNode = GraphNode(nodeIndex)
        sparseGraph.AddNode(newNode)

        self.assertEqual(1, len(sparseGraph._nodes), "_nodes 3")
        self.assertEqual(0, sparseGraph._nodes[nodeIndex].Index, "node.Index 3")

    def test_SpecifyThatAnExceptionIsRaisedWhenAddingAThatDoesNotMatchTheGraphNextNodeIndex(self):
        sparseGraph = SparseGraph(isDigraph=False)
        node = GraphNode(index=999)

        self.assertRaises(Exception, sparseGraph.AddNode, node)

    def test_SpecifyThatAnExceptionIsRaiseWhenAddingANodeInplaceOfACurrentlyActivatedNode(self):
        sparseGraph = SparseGraph(isDigraph=False)
        nodeIndex = sparseGraph.GetNextFreeNodeIndex()
        node = GraphNode(nodeIndex)

        sparseGraph.AddNode(node)

        self.assertEqual(1, len(sparseGraph._nodes), "_nodes 1")
        self.assertEqual(0, sparseGraph._nodes[nodeIndex].Index, "node.Index 1")

        # Add a new node in place of a active node in the graph
        newNode = GraphNode(nodeIndex)

        self.assertRaises(Exception, sparseGraph.AddNode, newNode)

    def test_SpecifyThatANodeCanBeRetrievedFromTheGraph(self):
        sparseGraph = SparseGraph(isDigraph=False)
        node = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node)

        retrievedNode = sparseGraph.GetNode(0)

        self.assertEqual(node, retrievedNode)

    def test_SpecifyThatRetrievingAnInvalidNodeRaisesAnException(self):
        sparseGraph = SparseGraph(isDigraph=False)
        node = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node)

        self.assertRaises(Exception, sparseGraph.GetNode, -1)
        self.assertRaises(Exception, sparseGraph.GetNode, 1)

    def test_SpecifyThatAnEdgeCanBeAddedBetweenTwoNodesOnAnUndirectedGraph(self):
        sparseGraph = SparseGraph(isDigraph=False)

        node0 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node0)

        node1 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node1)

        edge = GraphEdge(fromNodeIndex=node0.Index, toNodeIndex=node1.Index)
        sparseGraph.AddEdge(edge)

        self.assertEqual(2, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(2, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(2, sparseGraph._nextNodeIndex, "_nextNodeIndex")

        self.assertEqual(1, len(sparseGraph._edgeListVector[0]), "_edgeListVector[0]")
        self.assertEqual(0, sparseGraph._edgeListVector[0][0].From, "_edgeListVector[0][0].From")
        self.assertEqual(1, sparseGraph._edgeListVector[0][0].To, "_edgeListVector[0][0].To")

        self.assertEqual(1, len(sparseGraph._edgeListVector[1]), "_edgeListVector[1]")
        self.assertEqual(1, sparseGraph._edgeListVector[1][0].From, "_edgeListVector[1][0].From")
        self.assertEqual(0, sparseGraph._edgeListVector[1][0].To, "_edgeListVector[1][0].To")
        # print(sparseGraph._edgeListVector[0][0])
        # print(sparseGraph._edgeListVector[1][0])

    def test_SpecifyThatAnEdgeCanBeAddedBetweenNodesOnADirectedGraph(self):
        sparseGraph = SparseGraph(isDigraph=True)

        node0 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node0)

        node1 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node1)

        edge = GraphEdge(fromNodeIndex=node0.Index, toNodeIndex=node1.Index)
        sparseGraph.AddEdge(edge)

        self.assertEqual(2, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(2, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(2, sparseGraph._nextNodeIndex, "_nextNodeIndex")

        self.assertEqual(1, len(sparseGraph._edgeListVector[0]), "_edgeListVector[0]")
        self.assertEqual(0, sparseGraph._edgeListVector[0][0].From, "_edgeListVector[0][0].From")
        self.assertEqual(1, sparseGraph._edgeListVector[0][0].To, "_edgeListVector[0][0].To")

        self.assertEqual(0, len(sparseGraph._edgeListVector[1]), "_edgeListVector[1]")

    def test_SpecifyThatNodeCanHaveEdgeOnToItselfOnAnUndirectedGraph(self):
        sparseGraph = SparseGraph(isDigraph=False)

        node0 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node0)

        edge = GraphEdge(fromNodeIndex=node0.Index, toNodeIndex=node0.Index)
        sparseGraph.AddEdge(edge)

        self.assertEqual(1, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(1, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(1, sparseGraph._nextNodeIndex, "_nextNodeIndex")

        self.assertEqual(1, len(sparseGraph._edgeListVector[0]), "_edgeListVector[0]")
        self.assertEqual(0, sparseGraph._edgeListVector[0][0].From, "_edgeListVector[0][0].From")
        self.assertEqual(0, sparseGraph._edgeListVector[0][0].To, "_edgeListVector[0][0].To")

    def test_SpecifyThatNodeCanHaveEdgeOnToItselfOnADirectedGraph(self):
        sparseGraph = SparseGraph(isDigraph=True)

        node0 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node0)

        edge = GraphEdge(fromNodeIndex=node0.Index, toNodeIndex=node0.Index)
        sparseGraph.AddEdge(edge)

        self.assertEqual(1, len(sparseGraph._nodes), "_nodes")
        self.assertEqual(1, len(sparseGraph._edgeListVector), "_edgeListVector")
        self.assertEqual(1, sparseGraph._nextNodeIndex, "_nextNodeIndex")

        self.assertEqual(1, len(sparseGraph._edgeListVector[0]), "_edgeListVector[0]")
        self.assertEqual(0, sparseGraph._edgeListVector[0][0].From, "_edgeListVector[0][0].From")
        self.assertEqual(0, sparseGraph._edgeListVector[0][0].To, "_edgeListVector[0][0].To")

    def test_SpecifyThatSparseGraphCanWriteOutItsContentsToConsole(self):
        self.assertTrue(str(TestFactory.CreateUniGraph()))

    def test_SpecifyThatTheNumberOfNodesCanBeRetrieved(self):
        self.assertEqual(7, TestFactory.CreateDigraph().NumberOfNodes(), "Digraph")
        self.assertEqual(7, TestFactory.CreateUniGraph().NumberOfNodes(), "UniGraph")

    def test_SpecifyThatTheNumberOfActiveNodesCanBeRetrieved(self):
        self.assertEqual(6, TestFactory.CreateDigraph().NumberOfActiveNodes(), "Digraph")
        self.assertEqual(6, TestFactory.CreateUniGraph().NumberOfActiveNodes(), "UniGraph")

    def test_SpecifyThatTheNumberOfEdgesCanBeRetrieved(self):
        self.assertEqual(8, TestFactory.CreateDigraph().NumberOfEdges(), "Digraph")
        self.assertEqual(16, TestFactory.CreateUniGraph().NumberOfEdges(), "UniGraph")

    def test_SpecifyThatANodeCanBeDetermineIfItIsPresentInTheGraph(self):
        graph = TestFactory.CreateUniGraph()

        self.assertEqual(False, graph.IsNodePresent(-5), "IsNodePresent 1")
        self.assertEqual(True, graph.IsNodePresent(6), "IsNodePresent 2")
        self.assertEqual(False, graph.IsNodePresent(0), "IsNodePresent 3")
        self.assertEqual(False, graph.IsNodePresent(10), "IsNodePresent 3")

    def test_SpecifyThatAnEdgeCanBeDeterminedIfItIsPresentInTheGraph(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(False, graph.IsEdgePresent(0, 1), "IsEdgePresent 1")
        self.assertEqual(True, graph.IsEdgePresent(1, 5), "IsEdgePresent 2")
        self.assertEqual(False, graph.IsEdgePresent(5, 1), "IsEdgePresent 3")

    def test_SpecifyThatGraphCanBeCleared(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")

        graph.Clear()

        self.assertEqual(0, len(graph._nodes), "_nodes 2")
        self.assertEqual(0, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(0, graph._nextNodeIndex, "_nextNodeIndex 2")

    def test_SpecifyThatAllEdgesCanBeRemoved(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")
        self.assertEqual(8, graph.NumberOfEdges(), "NumberOfEdges 1")

        graph.RemoveEdges()

        self.assertEqual(7, len(graph._nodes), "_nodes 2")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 2")
        self.assertEqual(0, graph.NumberOfEdges(), "NumberOfEdges 2")

    def test_SpecifyThatAnEdgeCanBeRetrieved(self):
        graph = TestFactory.CreateDigraph()

        edge = graph.GetEdge(1, 5)

        self.assertEqual(1, edge.From, "From")
        self.assertEqual(5, edge.To, "To")
        self.assertEqual(2.9, edge.Cost, "Cost")

    def test_SpecifyThatAnExceptionIsRaisedWhenRetrievingANonExistingEdge(self):
        graph = TestFactory.CreateDigraph()

        self.assertRaises(Exception, graph.GetEdge, 1, 3)

    def test_SpecifyThatAnExceptionIsRaisedWhenRetrievingAEdgeWithInvalidIndices(self):
        graph = TestFactory.CreateDigraph()

        self.assertRaises(Exception, graph.GetEdge, -99, 1)
        self.assertRaises(Exception, graph.GetEdge, 99, 1)
        self.assertRaises(Exception, graph.GetEdge, 1, -99)
        self.assertRaises(Exception, graph.GetEdge, 1, 99)

    def test_SpecifyThatAnEdgeCostCanBeModified(self):
        graph = TestFactory.CreateDigraph()

        edge = graph.GetEdge(1, 5)

        self.assertEqual(1, edge.From, "From 1")
        self.assertEqual(5, edge.To, "To 1")
        self.assertEqual(2.9, edge.Cost, "Cost 1")

        graph.SetEdgeCost(1, 5, 4.4)

        edge = graph.GetEdge(1, 5)

        self.assertEqual(1, edge.From, "From 2")
        self.assertEqual(5, edge.To, "To 2")
        self.assertEqual(4.4, edge.Cost, "Cost 2")

    def test_SpecifyThatANodeCanBeRemovedFromAUniGraph(self):
        graph = TestFactory.CreateUniGraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")
        self.assertEqual(16, graph.NumberOfEdges(), "NumberOfEdges 1")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 1")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 1")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 1")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 1")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 1")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 1")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 1")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 1")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 1")
        self.assertEqual(2, len(graph._edgeListVector[2]), "_edgeListVector[2] 1")
        self.assertEqual(3, len(graph._edgeListVector[3]), "_edgeListVector[3] 1")
        self.assertEqual(2, len(graph._edgeListVector[4]), "_edgeListVector[4] 1")
        self.assertEqual(4, len(graph._edgeListVector[5]), "_edgeListVector[5] 1")
        self.assertEqual(3, len(graph._edgeListVector[6]), "_edgeListVector[6] 1")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 1")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 1")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 1")
        self.assertEqual(5, graph._edgeListVector[2][1].To, "graph._edgeListVector[2][1].To 1")
        self.assertEqual(2, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 1")
        self.assertEqual(4, graph._edgeListVector[3][1].To, "graph._edgeListVector[3][1].To 1")
        self.assertEqual(5, graph._edgeListVector[3][2].To, "graph._edgeListVector[3][2].To 1")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 1")
        self.assertEqual(6, graph._edgeListVector[4][1].To, "graph._edgeListVector[4][1].To 1")
        self.assertEqual(1, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 1")
        self.assertEqual(2, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 1")
        self.assertEqual(3, graph._edgeListVector[5][2].To, "graph._edgeListVector[5][2].To 1")
        self.assertEqual(6, graph._edgeListVector[5][3].To, "graph._edgeListVector[5][3].To 1")
        self.assertEqual(1, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 1")
        self.assertEqual(4, graph._edgeListVector[6][1].To, "graph._edgeListVector[6][1].To 1")
        self.assertEqual(5, graph._edgeListVector[6][2].To, "graph._edgeListVector[6][2].To 1")

        graph.RemoveNode(5)

        self.assertEqual(7, len(graph._nodes), "_nodes 2")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 2")
        self.assertEqual(8, graph.NumberOfEdges(), "NumberOfEdges 2")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 2")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 2")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 2")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 2")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 2")
        self.assertEqual(-1, graph._nodes[5].Index, "_nodes[5].Index 2")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 2")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 2")
        self.assertEqual(1, len(graph._edgeListVector[1]), "_edgeListVector[1] 2")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 2")
        self.assertEqual(2, len(graph._edgeListVector[3]), "_edgeListVector[3] 2")
        self.assertEqual(2, len(graph._edgeListVector[4]), "_edgeListVector[4] 2")
        self.assertEqual(0, len(graph._edgeListVector[5]), "_edgeListVector[5] 2")
        self.assertEqual(2, len(graph._edgeListVector[6]), "_edgeListVector[6] 2")

        self.assertEqual(6, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 2")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 2")
        self.assertEqual(2, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 2")
        self.assertEqual(4, graph._edgeListVector[3][1].To, "graph._edgeListVector[3][1].To 2")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 2")
        self.assertEqual(6, graph._edgeListVector[4][1].To, "graph._edgeListVector[4][1].To 2")
        self.assertEqual(1, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 2")
        self.assertEqual(4, graph._edgeListVector[6][1].To, "graph._edgeListVector[6][1].To 2")

    def test_SpecifyThatANodeCanBeRemovedFromADigraph(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")
        self.assertEqual(8, graph.NumberOfEdges(), "NumberOfEdges 1")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 1")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 1")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 1")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 1")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 1")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 1")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 1")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 1")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 1")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 1")
        self.assertEqual(1, len(graph._edgeListVector[3]), "_edgeListVector[3] 1")
        self.assertEqual(1, len(graph._edgeListVector[4]), "_edgeListVector[4] 1")
        self.assertEqual(2, len(graph._edgeListVector[5]), "_edgeListVector[5] 1")
        self.assertEqual(1, len(graph._edgeListVector[6]), "_edgeListVector[6] 1")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 1")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 1")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 1")
        self.assertEqual(5, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 1")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 1")
        self.assertEqual(2, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 1")
        self.assertEqual(6, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 1")
        self.assertEqual(4, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 1")

        graph.RemoveNode(5)

        self.assertEqual(7, len(graph._nodes), "_nodes 2")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 2")
        self.assertEqual(4, graph.NumberOfEdges(), "NumberOfEdges 2")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 2")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 2")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 2")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 2")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 2")
        self.assertEqual(-1, graph._nodes[5].Index, "_nodes[5].Index 2")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 2")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 2")
        self.assertEqual(1, len(graph._edgeListVector[1]), "_edgeListVector[1] 2")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 2")
        self.assertEqual(0, len(graph._edgeListVector[3]), "_edgeListVector[3] 2")
        self.assertEqual(1, len(graph._edgeListVector[4]), "_edgeListVector[4] 2")
        self.assertEqual(0, len(graph._edgeListVector[5]), "_edgeListVector[5] 2")
        self.assertEqual(1, len(graph._edgeListVector[6]), "_edgeListVector[6] 2")

        self.assertEqual(6, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To")
        self.assertEqual(4, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To")

    def test_SpecifyThatAnEdgeCanBeRemovedFromAUniGraph(self):
        graph = TestFactory.CreateUniGraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")
        self.assertEqual(16, graph.NumberOfEdges(), "NumberOfEdges 1")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 1")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 1")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 1")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 1")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 1")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 1")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 1")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 1")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 1")
        self.assertEqual(2, len(graph._edgeListVector[2]), "_edgeListVector[2] 1")
        self.assertEqual(3, len(graph._edgeListVector[3]), "_edgeListVector[3] 1")
        self.assertEqual(2, len(graph._edgeListVector[4]), "_edgeListVector[4] 1")
        self.assertEqual(4, len(graph._edgeListVector[5]), "_edgeListVector[5] 1")
        self.assertEqual(3, len(graph._edgeListVector[6]), "_edgeListVector[6] 1")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 1")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 1")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 1")
        self.assertEqual(5, graph._edgeListVector[2][1].To, "graph._edgeListVector[2][1].To 1")
        self.assertEqual(2, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 1")
        self.assertEqual(4, graph._edgeListVector[3][1].To, "graph._edgeListVector[3][1].To 1")
        self.assertEqual(5, graph._edgeListVector[3][2].To, "graph._edgeListVector[3][2].To 1")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 1")
        self.assertEqual(6, graph._edgeListVector[4][1].To, "graph._edgeListVector[4][1].To 1")
        self.assertEqual(1, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 1")
        self.assertEqual(2, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 1")
        self.assertEqual(3, graph._edgeListVector[5][2].To, "graph._edgeListVector[5][2].To 1")
        self.assertEqual(6, graph._edgeListVector[5][3].To, "graph._edgeListVector[5][3].To 1")
        self.assertEqual(1, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 1")
        self.assertEqual(4, graph._edgeListVector[6][1].To, "graph._edgeListVector[6][1].To 1")
        self.assertEqual(5, graph._edgeListVector[6][2].To, "graph._edgeListVector[6][2].To 1")

        graph.RemoveEdge(5, 3)

        self.assertEqual(7, len(graph._nodes), "_nodes 2")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 2")
        self.assertEqual(14, graph.NumberOfEdges(), "NumberOfEdges 2")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 2")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 2")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 2")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 2")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 2")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 2")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 2")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 2")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 2")
        self.assertEqual(2, len(graph._edgeListVector[2]), "_edgeListVector[2] 2")
        self.assertEqual(2, len(graph._edgeListVector[3]), "_edgeListVector[3] 2")
        self.assertEqual(2, len(graph._edgeListVector[4]), "_edgeListVector[4] 2")
        self.assertEqual(3, len(graph._edgeListVector[5]), "_edgeListVector[5] 2")
        self.assertEqual(3, len(graph._edgeListVector[6]), "_edgeListVector[6] 2")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 2")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 2")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 2")
        self.assertEqual(5, graph._edgeListVector[2][1].To, "graph._edgeListVector[2][1].To 2")
        self.assertEqual(2, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 2")
        self.assertEqual(4, graph._edgeListVector[3][1].To, "graph._edgeListVector[3][1].To 2")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 2")
        self.assertEqual(6, graph._edgeListVector[4][1].To, "graph._edgeListVector[4][1].To 2")
        self.assertEqual(1, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 2")
        self.assertEqual(2, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 2")
        self.assertEqual(6, graph._edgeListVector[5][2].To, "graph._edgeListVector[5][2].To 2")
        self.assertEqual(1, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 2")
        self.assertEqual(4, graph._edgeListVector[6][1].To, "graph._edgeListVector[6][1].To 2")
        self.assertEqual(5, graph._edgeListVector[6][2].To, "graph._edgeListVector[6][2].To 2")

    def test_SpecifyThatAnEdgeCanBeRemovedFromADigraph(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")
        self.assertEqual(8, graph.NumberOfEdges(), "NumberOfEdges 1")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 1")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 1")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 1")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 1")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 1")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 1")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 1")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 1")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 1")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 1")
        self.assertEqual(1, len(graph._edgeListVector[3]), "_edgeListVector[3] 1")
        self.assertEqual(1, len(graph._edgeListVector[4]), "_edgeListVector[4] 1")
        self.assertEqual(2, len(graph._edgeListVector[5]), "_edgeListVector[5] 1")
        self.assertEqual(1, len(graph._edgeListVector[6]), "_edgeListVector[6] 1")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 1")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 1")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 1")
        self.assertEqual(5, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 1")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 1")
        self.assertEqual(2, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 1")
        self.assertEqual(6, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 1")
        self.assertEqual(4, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 1")

        graph.RemoveEdge(3, 5)

        self.assertEqual(7, len(graph._nodes), "_nodes 2")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 2")
        self.assertEqual(7, graph.NumberOfEdges(), "NumberOfEdges 2")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 2")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 2")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 2")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 2")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 2")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 2")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 2")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 2")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 2")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 2")
        self.assertEqual(0, len(graph._edgeListVector[3]), "_edgeListVector[3] 2")
        self.assertEqual(1, len(graph._edgeListVector[4]), "_edgeListVector[4] 2")
        self.assertEqual(2, len(graph._edgeListVector[5]), "_edgeListVector[5] 2")
        self.assertEqual(1, len(graph._edgeListVector[6]), "_edgeListVector[6] 2")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 2")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 2")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 2")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 2")
        self.assertEqual(2, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 2")
        self.assertEqual(6, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 2")
        self.assertEqual(4, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 2")

    def test_SpecifyThatAGraphCanBeSavedAndLoadedFromFile(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(7, len(graph._nodes), "_nodes 1")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 1")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 1")
        self.assertEqual(8, graph.NumberOfEdges(), "NumberOfEdges 1")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 1")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 1")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 1")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 1")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 1")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 1")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 1")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 1")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 1")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 1")
        self.assertEqual(1, len(graph._edgeListVector[3]), "_edgeListVector[3] 1")
        self.assertEqual(1, len(graph._edgeListVector[4]), "_edgeListVector[4] 1")
        self.assertEqual(2, len(graph._edgeListVector[5]), "_edgeListVector[5] 1")
        self.assertEqual(1, len(graph._edgeListVector[6]), "_edgeListVector[6] 1")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 1")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 1")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 1")
        self.assertEqual(5, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 1")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 1")
        self.assertEqual(2, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 1")
        self.assertEqual(6, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 1")
        self.assertEqual(4, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 1")

        graph.Save("testGraph.map")

        graph = SparseGraph(isDigraph=False)

        graph.Load("testGraph.map")

        self.assertEqual(7, len(graph._nodes), "_nodes 2")
        self.assertEqual(7, len(graph._edgeListVector), "_edgeListVector 2")
        self.assertEqual(7, graph._nextNodeIndex, "_nextNodeIndex 2")
        self.assertEqual(8, graph.NumberOfEdges(), "NumberOfEdges 2")

        self.assertEqual(-1, graph._nodes[0].Index, "_nodes[0].Index 2")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index 2")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index 2")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index 2")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index 2")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index 2")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index 2")

        self.assertEqual(0, len(graph._edgeListVector[0]), "_edgeListVector[0] 2")
        self.assertEqual(2, len(graph._edgeListVector[1]), "_edgeListVector[1] 2")
        self.assertEqual(1, len(graph._edgeListVector[2]), "_edgeListVector[2] 2")
        self.assertEqual(1, len(graph._edgeListVector[3]), "_edgeListVector[3] 2")
        self.assertEqual(1, len(graph._edgeListVector[4]), "_edgeListVector[4] 2")
        self.assertEqual(2, len(graph._edgeListVector[5]), "_edgeListVector[5] 2")
        self.assertEqual(1, len(graph._edgeListVector[6]), "_edgeListVector[6] 2")

        self.assertEqual(5, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To 2")
        self.assertEqual(6, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To 2")
        self.assertEqual(3, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To 2")
        self.assertEqual(5, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To 2")
        self.assertEqual(3, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To 2")
        self.assertEqual(2, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To 2")
        self.assertEqual(6, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To 2")
        self.assertEqual(4, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To 2")

    def test_SpecifyThatAnExceptionIsRaiseWhenSavingToAnInvalidFile(self):
        graph = TestFactory.CreateDigraph()

        self.assertRaises(Exception, graph.Save, "\/-invalid-file-name\/")

    def test_SpecifyThatAnExceptionIsRaiseWhenLoadingToAnInvalidFile(self):
        graph = TestFactory.CreateDigraph()

        self.assertRaises(Exception, graph.Load, "\/-invalid-file-name\/")


