import unittest

from HorizonCore.Framework.Vector2D import Vector2D
from HorizonCore.Graph.GraphNodeNav import GraphNodeNav


class GraphNodeNavSpecifications(unittest.TestCase):

    def test_SpecifyThatGraphNodeNavCanBeConstructed(self):
        graphNode = GraphNodeNav(index=10, position=Vector2D(20, 30))

        self.assertEqual(10, graphNode.Index, "Index")
        self.assertEqual(20, graphNode.Position.X, "Position.X")
        self.assertEqual(30, graphNode.Position.Y, "Position.Y")
        self.assertEqual(None, graphNode.ExtraInfo, "ExtraInfo")

    def test_SpecifyThatGraphNodeNavCanBeModified(self):
        graphNode = GraphNodeNav(index=10, position=Vector2D(20, 30))

        graphNode.Index = 40
        graphNode.Position = Vector2D(50, 60)
        graphNode.ExtraInfo = "Extra Node Info"

        self.assertEqual(40, graphNode.Index, "Index")
        self.assertEqual(50, graphNode.Position.X, "Position.X")
        self.assertEqual(60, graphNode.Position.Y, "Position.Y")
        self.assertEqual("Extra Node Info", graphNode.ExtraInfo, "ExtraInfo")

    def test_SpecifyThatGraphNodeCanWriteOutItsContentsToConsole(self):
        graphNode = GraphNodeNav(index=10, position=Vector2D(20, 30), extraInfo="node info")
        stringOutput = str(graphNode)

        self.assertEqual(stringOutput, "Index: 10 | Position: (20.00, 30.00) | ExtraInfo: 'node info'")
