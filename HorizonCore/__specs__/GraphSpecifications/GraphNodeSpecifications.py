import unittest

from HorizonCore.Graph.GraphNode import GraphNode
from HorizonCore.Graph.NodeType import NodeType


class GraphNodeSpecifications(unittest.TestCase):

    def test_SpecifyThatDefaultGraphNodeCanBeConstructed(self):
        graphNode = GraphNode()

        self.assertEqual(NodeType.InvalidNodeIndex.value, graphNode.Index, "Index")

    def test_SpecifyThatGraphNodeCanBeModified(self):
        graphNode = GraphNode(index=10)

        self.assertEqual(10, graphNode.Index, "Index 1")

        graphNode.Index = 20

        self.assertEqual(20, graphNode.Index, "Index 2")

    def test_SpecifyThatGraphNodeCanWriteOutItsContentsToConsole(self):
        graphNode = GraphNode(index=10)
        stringOutput = str(graphNode)

        self.assertEqual(stringOutput, "Index: 10")
