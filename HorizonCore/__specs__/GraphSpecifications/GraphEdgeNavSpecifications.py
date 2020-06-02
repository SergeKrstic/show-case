import unittest

from HorizonCore.Graph.NodeType import NodeType
from HorizonCore.Graph.GraphEdgeNav import GraphEdgeNav, Flags


class GraphEdgeNavSpecifications(unittest.TestCase):
    def test_SpecifyThatDefaultGraphEdgeNavCanBeConstructed(self):
        graphEdge = GraphEdgeNav(fromNodeIndex=10, toNodeIndex=20, cost=30)

        self.assertEqual(10, graphEdge.From, "From")
        self.assertEqual(20, graphEdge.To, "To")
        self.assertEqual(30, graphEdge.Cost, "Cost")
        self.assertEqual(0, graphEdge.Flags, "Flags")
        self.assertEqual(NodeType.InvalidNodeIndex.value, graphEdge.IdOfIntersectingEntity, "IdOfIntersectingEntity")

    def test_SpecifyThatGraphEdgeNavCanBeConstructed(self):
        graphEdge = self.CreateGraphNodeNav()

        self.assertEqual(10, graphEdge.From, "From")
        self.assertEqual(20, graphEdge.To, "To")
        self.assertEqual(30, graphEdge.Cost, "Cost")
        self.assertEqual(Flags.Crawl.value, graphEdge.Flags, "Flags")
        self.assertEqual(40, graphEdge.IdOfIntersectingEntity, "IdOfIntersectingEntity")

    def test_SpecifyThatGraphEdgeNavPropertiesCanBeModified(self):
        graphEdge = self.CreateGraphNodeNav()

        graphEdge.From = 100
        graphEdge.To = 200
        graphEdge.Cost = 300
        graphEdge.Flags = 400
        graphEdge.IdOfIntersectingEntity = 500

        self.assertEqual(100, graphEdge.From, "From")
        self.assertEqual(200, graphEdge.To, "To")
        self.assertEqual(300, graphEdge.Cost, "Cost")
        self.assertEqual(400, graphEdge.Flags, "Flags")
        self.assertEqual(500, graphEdge.IdOfIntersectingEntity, "IdOfIntersectingEntity")

    def test_SpecifyThatGraphEdgeNavCanWriteOutItsContentsToConsole(self):
        graphEdge = self.CreateGraphNodeNav()
        stringOutput = str(graphEdge)

        self.assertEqual(stringOutput, "From: 10 | To: 20 | Cost: 30.00 | Flags: 2 | IdOfIntersectingEntity: 40")

    @staticmethod
    def CreateGraphNodeNav():
        return GraphEdgeNav(fromNodeIndex=10,
                            toNodeIndex=20,
                            cost=30,
                            flags=Flags.Crawl,
                            idOfIntersectingEntity=40)
