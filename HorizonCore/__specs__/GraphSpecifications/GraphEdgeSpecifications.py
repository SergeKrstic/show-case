import unittest

from HorizonCore.Graph.GraphEdge import GraphEdge
from HorizonCore.Graph.NodeType import NodeType


class GraphEdgeSpecifications(unittest.TestCase):

    def test_SpecifyThatDefaultGraphEdgeCanBeConstructed(self):
        graphEdge = GraphEdge()

        self.assertEqual(NodeType.InvalidNodeIndex.value, graphEdge.From, "From")
        self.assertEqual(NodeType.InvalidNodeIndex.value, graphEdge.To, "To")
        self.assertEqual(1.0, graphEdge.Cost, "Cost")

    def test_SpecifyThatGraphEdgeCanBeConstructed(self):
        graphEdge = GraphEdge(fromNodeIndex=10, toNodeIndex=20, cost=30)

        self.assertEqual(10, graphEdge.From, "From")
        self.assertEqual(20, graphEdge.To, "To")
        self.assertEqual(30, graphEdge.Cost, "Cost")

    def test_SpecifyThatGraphEdgePropertiesCanBeModified(self):
        graphEdge = GraphEdge()

        graphEdge.From = 100
        graphEdge.To = 200
        graphEdge.Cost = 300

        self.assertEqual(100, graphEdge.From, "From")
        self.assertEqual(200, graphEdge.To, "To")
        self.assertEqual(300, graphEdge.Cost, "Cost")

    def test_SpecifyThatTwoGraphEdgesCanBeCompared(self):
        edge1 = GraphEdge(fromNodeIndex=10, toNodeIndex=20, cost=30)
        edge2 = GraphEdge(fromNodeIndex=10, toNodeIndex=20, cost=30)
        edge3 = GraphEdge(fromNodeIndex=70, toNodeIndex=80, cost=90)

        self.assertTrue(edge1 == edge2, "comp 1")
        self.assertTrue(edge1 == edge1, "comp 2")
        self.assertTrue(edge1 != edge3, "comp 3")

    def test_SpecifyThatGraphEdgeCanWriteOutItsContentsToConsole(self):
        graphEdge = GraphEdge(fromNodeIndex=10, toNodeIndex=20, cost=30)
        stringOutput = str(graphEdge)

        self.assertEqual(stringOutput, "From: 10 | To: 20 | Cost: 30")
