import numpy as np
import unittest

from mock import Mock

from HorizonCore.Graph.GraphTools import GraphTools
from HorizonCore.Graph.SparseGraph import SparseGraph
from HorizonCore.__specs__.TestHelpers.TestFactory import TestFactory


class GraphToolsSpecifications(unittest.TestCase):

    def test_SpecifyThatCostliestGraphEdgeCanBeFound(self):
        graph = TestFactory.CreateDigraph()

        self.assertEqual(3.7, GraphTools.GetCostliestGraphEdge(graph))

    def test_SpecifyThatCellIndicesCanBeValidated(self):
        self.assertEqual(False, GraphTools.IsValidNeighbour(xCellIndex=-1, yCellIndex=-1, numCellsX=5, numCellsY=5), "T1")
        self.assertEqual(True, GraphTools.IsValidNeighbour(xCellIndex=0, yCellIndex=0, numCellsX=5, numCellsY=5), "T2")
        self.assertEqual(False, GraphTools.IsValidNeighbour(xCellIndex=-1, yCellIndex=0, numCellsX=5, numCellsY=5), "T3")
        self.assertEqual(False, GraphTools.IsValidNeighbour(xCellIndex=0, yCellIndex=-1, numCellsX=5, numCellsY=5), "T4")
        self.assertEqual(True, GraphTools.IsValidNeighbour(xCellIndex=4, yCellIndex=4, numCellsX=5, numCellsY=5), "T5")
        self.assertEqual(False, GraphTools.IsValidNeighbour(xCellIndex=5, yCellIndex=4, numCellsX=5, numCellsY=5), "T6")
        self.assertEqual(False, GraphTools.IsValidNeighbour(xCellIndex=4, yCellIndex=5, numCellsX=5, numCellsY=5), "T7")
        self.assertEqual(False, GraphTools.IsValidNeighbour(xCellIndex=5, yCellIndex=5, numCellsX=5, numCellsY=5), "T7")

    def test_SpecifyThatAConnectedGridCanBeConstructedOnAUniGraph(self):
        graph = SparseGraph.CreateNavGraph(isDigraph=False)

        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)

        self.assertEqual(9, len(graph._nodes), "_nodes")
        self.assertEqual(9, len(graph._edgeListVector), "_edgeListVector")
        self.assertEqual(9, graph._nextNodeIndex, "_nextNodeIndex")
        self.assertEqual(40, graph.NumberOfEdges(), "NumberOfEdges")

        self.assertEqual(0, graph._nodes[0].Index, "_nodes[0].Index")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index")
        self.assertEqual(7, graph._nodes[7].Index, "_nodes[7].Index")
        self.assertEqual(8, graph._nodes[8].Index, "_nodes[8].Index")

        self.assertEqual(3, len(graph._edgeListVector[0]), "_edgeListVector[0]")
        self.assertEqual(5, len(graph._edgeListVector[1]), "_edgeListVector[1]")
        self.assertEqual(3, len(graph._edgeListVector[2]), "_edgeListVector[2]")
        self.assertEqual(5, len(graph._edgeListVector[3]), "_edgeListVector[3]")
        self.assertEqual(8, len(graph._edgeListVector[4]), "_edgeListVector[4]")
        self.assertEqual(5, len(graph._edgeListVector[5]), "_edgeListVector[5]")
        self.assertEqual(3, len(graph._edgeListVector[6]), "_edgeListVector[6]")
        self.assertEqual(5, len(graph._edgeListVector[7]), "_edgeListVector[6]")
        self.assertEqual(3, len(graph._edgeListVector[8]), "_edgeListVector[6]")

        self.assertEqual(1, graph._edgeListVector[0][0].To, "graph._edgeListVector[0][0].To")
        self.assertEqual(3, graph._edgeListVector[0][1].To, "graph._edgeListVector[0][1].To")
        self.assertEqual(4, graph._edgeListVector[0][2].To, "graph._edgeListVector[0][2].To")

        self.assertEqual(0, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To")
        self.assertEqual(2, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To")
        self.assertEqual(3, graph._edgeListVector[1][2].To, "graph._edgeListVector[1][2].To")
        self.assertEqual(4, graph._edgeListVector[1][3].To, "graph._edgeListVector[1][3].To")
        self.assertEqual(5, graph._edgeListVector[1][4].To, "graph._edgeListVector[1][4].To")

        self.assertEqual(1, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To")
        self.assertEqual(4, graph._edgeListVector[2][1].To, "graph._edgeListVector[2][1].To")
        self.assertEqual(5, graph._edgeListVector[2][2].To, "graph._edgeListVector[2][2].To")

        self.assertEqual(0, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To")
        self.assertEqual(1, graph._edgeListVector[3][1].To, "graph._edgeListVector[3][1].To")
        self.assertEqual(4, graph._edgeListVector[3][2].To, "graph._edgeListVector[3][2].To")
        self.assertEqual(6, graph._edgeListVector[3][3].To, "graph._edgeListVector[3][3].To")
        self.assertEqual(7, graph._edgeListVector[3][4].To, "graph._edgeListVector[3][4].To")

        self.assertEqual(0, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To")
        self.assertEqual(1, graph._edgeListVector[4][1].To, "graph._edgeListVector[4][1].To")
        self.assertEqual(2, graph._edgeListVector[4][2].To, "graph._edgeListVector[4][2].To")
        self.assertEqual(3, graph._edgeListVector[4][3].To, "graph._edgeListVector[4][3].To")
        self.assertEqual(5, graph._edgeListVector[4][4].To, "graph._edgeListVector[4][4].To")
        self.assertEqual(6, graph._edgeListVector[4][5].To, "graph._edgeListVector[4][5].To")
        self.assertEqual(7, graph._edgeListVector[4][6].To, "graph._edgeListVector[4][6].To")
        self.assertEqual(8, graph._edgeListVector[4][7].To, "graph._edgeListVector[4][7].To")

        self.assertEqual(1, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To")
        self.assertEqual(2, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To")
        self.assertEqual(4, graph._edgeListVector[5][2].To, "graph._edgeListVector[5][2].To")
        self.assertEqual(7, graph._edgeListVector[5][3].To, "graph._edgeListVector[5][3].To")
        self.assertEqual(8, graph._edgeListVector[5][4].To, "graph._edgeListVector[5][4].To")

        self.assertEqual(3, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To")
        self.assertEqual(4, graph._edgeListVector[6][1].To, "graph._edgeListVector[6][1].To")
        self.assertEqual(7, graph._edgeListVector[6][2].To, "graph._edgeListVector[6][2].To")

        self.assertEqual(3, graph._edgeListVector[7][0].To, "graph._edgeListVector[7][0].To")
        self.assertEqual(4, graph._edgeListVector[7][1].To, "graph._edgeListVector[7][1].To")
        self.assertEqual(5, graph._edgeListVector[7][2].To, "graph._edgeListVector[7][2].To")
        self.assertEqual(6, graph._edgeListVector[7][3].To, "graph._edgeListVector[7][3].To")
        self.assertEqual(8, graph._edgeListVector[7][4].To, "graph._edgeListVector[7][4].To")

        self.assertEqual(4, graph._edgeListVector[8][0].To, "graph._edgeListVector[8][0].To")
        self.assertEqual(5, graph._edgeListVector[8][1].To, "graph._edgeListVector[8][1].To")
        self.assertEqual(7, graph._edgeListVector[8][2].To, "graph._edgeListVector[8][2].To")

    def test_SpecifyThatAConnectedGridCanBeConstructedOnADigraph(self):
        graph = SparseGraph.CreateNavGraph(isDigraph=True)

        GraphTools.CreateGrid(graph, cxSize=50 * 3, cySize=50 * 3, numCellsX=3, numCellsY=3)

        self.assertEqual(9, len(graph._nodes), "_nodes")
        self.assertEqual(9, len(graph._edgeListVector), "_edgeListVector")
        self.assertEqual(9, graph._nextNodeIndex, "_nextNodeIndex")
        self.assertEqual(40, graph.NumberOfEdges(), "NumberOfEdges")

        self.assertEqual(0, graph._nodes[0].Index, "_nodes[0].Index")
        self.assertEqual(1, graph._nodes[1].Index, "_nodes[1].Index")
        self.assertEqual(2, graph._nodes[2].Index, "_nodes[2].Index")
        self.assertEqual(3, graph._nodes[3].Index, "_nodes[3].Index")
        self.assertEqual(4, graph._nodes[4].Index, "_nodes[4].Index")
        self.assertEqual(5, graph._nodes[5].Index, "_nodes[5].Index")
        self.assertEqual(6, graph._nodes[6].Index, "_nodes[6].Index")
        self.assertEqual(7, graph._nodes[7].Index, "_nodes[7].Index")
        self.assertEqual(8, graph._nodes[8].Index, "_nodes[8].Index")

        self.assertEqual(3, len(graph._edgeListVector[0]), "_edgeListVector[0]")
        self.assertEqual(5, len(graph._edgeListVector[1]), "_edgeListVector[1]")
        self.assertEqual(3, len(graph._edgeListVector[2]), "_edgeListVector[2]")
        self.assertEqual(5, len(graph._edgeListVector[3]), "_edgeListVector[3]")
        self.assertEqual(8, len(graph._edgeListVector[4]), "_edgeListVector[4]")
        self.assertEqual(5, len(graph._edgeListVector[5]), "_edgeListVector[5]")
        self.assertEqual(3, len(graph._edgeListVector[6]), "_edgeListVector[6]")
        self.assertEqual(5, len(graph._edgeListVector[7]), "_edgeListVector[6]")
        self.assertEqual(3, len(graph._edgeListVector[8]), "_edgeListVector[6]")

        self.assertEqual(1, graph._edgeListVector[0][0].To, "graph._edgeListVector[0][0].To")
        self.assertEqual(3, graph._edgeListVector[0][1].To, "graph._edgeListVector[0][1].To")
        self.assertEqual(4, graph._edgeListVector[0][2].To, "graph._edgeListVector[0][2].To")

        self.assertEqual(0, graph._edgeListVector[1][0].To, "graph._edgeListVector[1][0].To")
        self.assertEqual(2, graph._edgeListVector[1][1].To, "graph._edgeListVector[1][1].To")
        self.assertEqual(3, graph._edgeListVector[1][2].To, "graph._edgeListVector[1][2].To")
        self.assertEqual(4, graph._edgeListVector[1][3].To, "graph._edgeListVector[1][3].To")
        self.assertEqual(5, graph._edgeListVector[1][4].To, "graph._edgeListVector[1][4].To")

        self.assertEqual(1, graph._edgeListVector[2][0].To, "graph._edgeListVector[2][0].To")
        self.assertEqual(4, graph._edgeListVector[2][1].To, "graph._edgeListVector[2][1].To")
        self.assertEqual(5, graph._edgeListVector[2][2].To, "graph._edgeListVector[2][2].To")

        self.assertEqual(0, graph._edgeListVector[3][0].To, "graph._edgeListVector[3][0].To")
        self.assertEqual(1, graph._edgeListVector[3][1].To, "graph._edgeListVector[3][1].To")
        self.assertEqual(4, graph._edgeListVector[3][2].To, "graph._edgeListVector[3][2].To")
        self.assertEqual(6, graph._edgeListVector[3][3].To, "graph._edgeListVector[3][3].To")
        self.assertEqual(7, graph._edgeListVector[3][4].To, "graph._edgeListVector[3][4].To")

        self.assertEqual(0, graph._edgeListVector[4][0].To, "graph._edgeListVector[4][0].To")
        self.assertEqual(1, graph._edgeListVector[4][1].To, "graph._edgeListVector[4][1].To")
        self.assertEqual(2, graph._edgeListVector[4][2].To, "graph._edgeListVector[4][2].To")
        self.assertEqual(3, graph._edgeListVector[4][3].To, "graph._edgeListVector[4][3].To")
        self.assertEqual(5, graph._edgeListVector[4][4].To, "graph._edgeListVector[4][4].To")
        self.assertEqual(6, graph._edgeListVector[4][5].To, "graph._edgeListVector[4][5].To")
        self.assertEqual(7, graph._edgeListVector[4][6].To, "graph._edgeListVector[4][6].To")
        self.assertEqual(8, graph._edgeListVector[4][7].To, "graph._edgeListVector[4][7].To")

        self.assertEqual(1, graph._edgeListVector[5][0].To, "graph._edgeListVector[5][0].To")
        self.assertEqual(2, graph._edgeListVector[5][1].To, "graph._edgeListVector[5][1].To")
        self.assertEqual(4, graph._edgeListVector[5][2].To, "graph._edgeListVector[5][2].To")
        self.assertEqual(7, graph._edgeListVector[5][3].To, "graph._edgeListVector[5][3].To")
        self.assertEqual(8, graph._edgeListVector[5][4].To, "graph._edgeListVector[5][4].To")

        self.assertEqual(3, graph._edgeListVector[6][0].To, "graph._edgeListVector[6][0].To")
        self.assertEqual(4, graph._edgeListVector[6][1].To, "graph._edgeListVector[6][1].To")
        self.assertEqual(7, graph._edgeListVector[6][2].To, "graph._edgeListVector[6][2].To")

        self.assertEqual(3, graph._edgeListVector[7][0].To, "graph._edgeListVector[7][0].To")
        self.assertEqual(4, graph._edgeListVector[7][1].To, "graph._edgeListVector[7][1].To")
        self.assertEqual(5, graph._edgeListVector[7][2].To, "graph._edgeListVector[7][2].To")
        self.assertEqual(6, graph._edgeListVector[7][3].To, "graph._edgeListVector[7][3].To")
        self.assertEqual(8, graph._edgeListVector[7][4].To, "graph._edgeListVector[7][4].To")

        self.assertEqual(4, graph._edgeListVector[8][0].To, "graph._edgeListVector[8][0].To")
        self.assertEqual(5, graph._edgeListVector[8][1].To, "graph._edgeListVector[8][1].To")
        self.assertEqual(7, graph._edgeListVector[8][2].To, "graph._edgeListVector[8][2].To")

    def test_SpecifyThatAverageGraphEdgeLengthCanBeCalculated(self):
        graph = self.CreateGraphGrid()

        self.assertAlmostEqual(58.284, GraphTools.CalculateAverageGraphEdgeLength(graph), 2)

    def test_SpecifyThatNavGraphNodeEdgesCanBeModifiedWithAWeighting(self):
        graph = self.CreateGraphGrid()

        self.assertAlmostEqual(50.0, graph._edgeListVector[0][0].Cost, 1, "graph._edgeListVector[0][0].Cost 1")
        self.assertAlmostEqual(50.0, graph._edgeListVector[0][1].Cost, 1, "graph._edgeListVector[0][1].Cost 1")
        self.assertAlmostEqual(70.7, graph._edgeListVector[0][2].Cost, 1, "graph._edgeListVector[0][2].Cost 1")

        GraphTools.WeightNavGraphNodeEdges(graph, 0, 2)

        self.assertAlmostEqual(100.0, graph._edgeListVector[0][0].Cost, 1, "graph._edgeListVector[0][0].Cost 2")
        self.assertAlmostEqual(100.0, graph._edgeListVector[0][1].Cost, 1, "graph._edgeListVector[0][1].Cost 2")
        self.assertAlmostEqual(141.4, graph._edgeListVector[0][2].Cost, 1, "graph._edgeListVector[0][2].Cost 2")

    def test_SpecifyThatAnExceptionIsRaisedWhenModifiedAInvalidNodeWeighting(self):
        graph = self.CreateGraphGrid()

        self.assertRaises(Exception, GraphTools.WeightNavGraphNodeEdges, graph, 999, 2)

    def test_SpecifyThatAllPairsTableCanBeCalculated(self):
        graph = self.CreateGraphGrid()

        pairsTable = GraphTools.CreateAllPairsTable(graph)

        self.assertEqual(9, len(pairsTable))
        self.assertEqual(9, len(pairsTable[0]))
        self.assertEqual([0, 1, 1, 3, 4, 1, 3, 3, 4], pairsTable[0])
        self.assertEqual([0, 1, 2, 3, 4, 5, 4, 4, 4], pairsTable[1])
        self.assertEqual([1, 1, 2, 1, 4, 5, 4, 5, 5], pairsTable[2])
        self.assertEqual([0, 1, 4, 3, 4, 4, 6, 7, 4], pairsTable[3])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], pairsTable[4])
        self.assertEqual([4, 1, 2, 4, 4, 5, 4, 7, 8], pairsTable[5])
        self.assertEqual([3, 3, 4, 3, 4, 7, 6, 7, 7], pairsTable[6])
        self.assertEqual([4, 4, 4, 3, 4, 5, 6, 7, 8], pairsTable[7])
        self.assertEqual([4, 5, 5, 7, 4, 5, 7, 7, 8], pairsTable[8])

    def test_SpecifyThatAllPairsCostsTableCanBeCalculated(self):
        graph = self.CreateGraphGrid()

        costsTable = GraphTools.CreateAllPairsCostsTable(graph)

        np.testing.assert_almost_equal([0.0, 50.0, 100.0, 50.0, 70.7, 120.7, 100.0, 120.7, 141.4], costsTable[0], 1, "costsTable[0]")
        np.testing.assert_almost_equal([50.0, 0.0, 50.0, 70.7, 50.0, 70.7, 120.7, 100.0, 120.7], costsTable[1], 1, "costsTable[0]")
        np.testing.assert_almost_equal([100.0, 50.0, 0.0, 120.7, 70.7, 50.0, 141.4, 120.7, 100.0], costsTable[2], 1, "costsTable[2]")
        np.testing.assert_almost_equal([50.0, 70.7, 120.7, 0.0, 50.0, 100.0, 50.0, 70.7, 120.7], costsTable[3], 1, "costsTable[3]")
        np.testing.assert_almost_equal([70.7, 50.0, 70.7, 50.0, 0.0, 50.0, 70.7, 50.0, 70.7], costsTable[4], 1, "costsTable[4]")
        np.testing.assert_almost_equal([120.7, 70.7, 50.0, 100.0, 50.0, 0.0, 120.7, 70.7, 50.0], costsTable[5], 1, "costsTable[5]")
        np.testing.assert_almost_equal([100.0, 120.7, 141.4, 50.0, 70.7, 120.7, 0.0, 50.0, 100.0], costsTable[6], 1, "costsTable[6]")
        np.testing.assert_almost_equal([120.7, 100.0, 120.7, 70.7, 50.0, 70.7, 50.0, 0.0, 50.0], costsTable[7], 1, "costsTable[7]")
        np.testing.assert_almost_equal([141.4, 120.7, 100.0, 120.7, 70.7, 50.0, 100.0, 50.0, 0.0], costsTable[8], 1, "costsTable[8]")

    def test_SpecifyThatGraphIsNotDrawnToCanvasWhenItHasNoNodes(self):
        graph = self.CreateGraphGrid(size=0)
        canvas = Mock()
        GraphTools.DrawGraph(canvas, graph, color="red", cellWidth=50, offset=0, drawNodeIds=True)
        canvas.assert_not_called()

    def test_SpecifyThatGraphCanBeDrawnToCanvas(self):
        graph = self.CreateGraphGrid()
        canvas = Mock()
        GraphTools.DrawGraph(canvas, graph, color="red", cellWidth=50, offset=0, drawNodeIds=True)

        self.assertEqual(9, len(canvas.create_oval.mock_calls), "len(create_oval)")
        self.assertEqual("call(24.0, 24.0, 26.0, 26.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[0]), "create_oval[0]")
        self.assertEqual("call(74.0, 24.0, 76.0, 26.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[1]), "create_oval[1]")
        self.assertEqual("call(124.0, 24.0, 126.0, 26.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[2]), "create_oval[2]")
        self.assertEqual("call(24.0, 74.0, 26.0, 76.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[3]), "create_oval[3]")
        self.assertEqual("call(74.0, 74.0, 76.0, 76.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[4]), "create_oval[4]")
        self.assertEqual("call(124.0, 74.0, 126.0, 76.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[5]), "create_oval[5]")
        self.assertEqual("call(24.0, 124.0, 26.0, 126.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[6]), "create_oval[6]")
        self.assertEqual("call(74.0, 124.0, 76.0, 126.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[7]), "create_oval[7]")
        self.assertEqual("call(124.0, 124.0, 126.0, 126.0, fill='red', outline='red', tags='')", str(canvas.create_oval.mock_calls[8]), "create_oval[8]")

        self.assertEqual(40, len(canvas.create_line.mock_calls), "len(create_line)")
        self.assertEqual("call(25.0, 25.0, 75.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[0]), "create_line[0]")
        self.assertEqual("call(25.0, 25.0, 25.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[1]), "create_line[1]")
        self.assertEqual("call(25.0, 25.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[2]), "create_line[2]")
        self.assertEqual("call(75.0, 25.0, 25.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[3]), "create_line[3]")
        self.assertEqual("call(75.0, 25.0, 125.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[4]), "create_line[4]")
        self.assertEqual("call(75.0, 25.0, 25.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[5]), "create_line[5]")
        self.assertEqual("call(75.0, 25.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[6]), "create_line[6]")
        self.assertEqual("call(75.0, 25.0, 125.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[7]), "create_line[7]")
        self.assertEqual("call(125.0, 25.0, 75.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[8]), "create_line[8]")
        self.assertEqual("call(125.0, 25.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[9]), "create_line[9]")
        self.assertEqual("call(125.0, 25.0, 125.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[10]), "create_line[10]")
        self.assertEqual("call(25.0, 75.0, 25.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[11]), "create_line[11]")
        self.assertEqual("call(25.0, 75.0, 75.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[12]), "create_line[12]")
        self.assertEqual("call(25.0, 75.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[13]), "create_line[13]")
        self.assertEqual("call(25.0, 75.0, 25.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[14]), "create_line[14]")
        self.assertEqual("call(25.0, 75.0, 75.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[15]), "create_line[15]")
        self.assertEqual("call(75.0, 75.0, 25.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[16]), "create_line[16]")
        self.assertEqual("call(75.0, 75.0, 75.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[17]), "create_line[17]")
        self.assertEqual("call(75.0, 75.0, 125.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[18]), "create_line[18]")
        self.assertEqual("call(75.0, 75.0, 25.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[19]), "create_line[19]")
        self.assertEqual("call(75.0, 75.0, 125.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[20]), "create_line[20]")
        self.assertEqual("call(75.0, 75.0, 25.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[21]), "create_line[21]")
        self.assertEqual("call(75.0, 75.0, 75.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[22]), "create_line[22]")
        self.assertEqual("call(75.0, 75.0, 125.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[23]), "create_line[23]")
        self.assertEqual("call(125.0, 75.0, 75.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[24]), "create_line[24]")
        self.assertEqual("call(125.0, 75.0, 125.0, 25.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[25]), "create_line[25]")
        self.assertEqual("call(125.0, 75.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[26]), "create_line[26]")
        self.assertEqual("call(125.0, 75.0, 75.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[27]), "create_line[27]")
        self.assertEqual("call(125.0, 75.0, 125.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[28]), "create_line[28]")
        self.assertEqual("call(25.0, 125.0, 25.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[29]), "create_line[29]")
        self.assertEqual("call(25.0, 125.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[30]), "create_line[30]")
        self.assertEqual("call(25.0, 125.0, 75.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[31]), "create_line[31]")
        self.assertEqual("call(75.0, 125.0, 25.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[32]), "create_line[32]")
        self.assertEqual("call(75.0, 125.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[33]), "create_line[33]")
        self.assertEqual("call(75.0, 125.0, 125.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[34]), "create_line[34]")
        self.assertEqual("call(75.0, 125.0, 25.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[35]), "create_line[35]")
        self.assertEqual("call(75.0, 125.0, 125.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[36]), "create_line[36]")
        self.assertEqual("call(125.0, 125.0, 75.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[37]), "create_line[37]")
        self.assertEqual("call(125.0, 125.0, 125.0, 75.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[38]), "create_line[38]")
        self.assertEqual("call(125.0, 125.0, 75.0, 125.0, dash='-', fill='red', tags='')", str(canvas.create_line.mock_calls[39]), "create_line[39]")

        self.assertEqual(9, len(canvas.create_text.mock_calls), "len(create_text)")
        self.assertEqual("call(10.0, 10.0, fill='grey38', font='helvetica 8', tags='', text='0')", str(canvas.create_text.mock_calls[0]), "create_text[0]")
        self.assertEqual("call(60.0, 10.0, fill='grey38', font='helvetica 8', tags='', text='1')", str(canvas.create_text.mock_calls[1]), "create_text[1]")
        self.assertEqual("call(110.0, 10.0, fill='grey38', font='helvetica 8', tags='', text='2')", str(canvas.create_text.mock_calls[2]), "create_text[2]")
        self.assertEqual("call(10.0, 60.0, fill='grey38', font='helvetica 8', tags='', text='3')", str(canvas.create_text.mock_calls[3]), "create_text[3]")
        self.assertEqual("call(60.0, 60.0, fill='grey38', font='helvetica 8', tags='', text='4')", str(canvas.create_text.mock_calls[4]), "create_text[4]")
        self.assertEqual("call(110.0, 60.0, fill='grey38', font='helvetica 8', tags='', text='5')", str(canvas.create_text.mock_calls[5]), "create_text[5]")
        self.assertEqual("call(10.0, 110.0, fill='grey38', font='helvetica 8', tags='', text='6')", str(canvas.create_text.mock_calls[6]), "create_text[6]")
        self.assertEqual("call(60.0, 110.0, fill='grey38', font='helvetica 8', tags='', text='7')", str(canvas.create_text.mock_calls[7]), "create_text[7]")
        self.assertEqual("call(110.0, 110.0, fill='grey38', font='helvetica 8', tags='', text='8')", str(canvas.create_text.mock_calls[8]), "create_text[8]")

    # Creation methods
    # ==================================================================================================================

    @staticmethod
    def CreateGraphGrid(size=3):
        graph = SparseGraph.CreateNavGraph(isDigraph=False)
        GraphTools.CreateGrid(graph, cxSize=50 * size, cySize=50 * size, numCellsX=size, numCellsY=size)
        return graph
