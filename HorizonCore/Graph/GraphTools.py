import math

from HorizonCore.Framework.Vector2D import Vector2D
from HorizonCore.Graph.GraphEdgeNav import GraphEdgeNav
from HorizonCore.Graph.GraphNodeNav import GraphNodeNav
from HorizonCore.Graph.GraphSearchDijkstra import GraphSearchDijkstra


class GraphTools:
    """
        As the name implies, some useful functions you can use with your graphs.

        For the function templates, make sure your graph interface complies
        with the SparseGraph class
    """

    @staticmethod
    def IsValidNeighbour(xCellIndex, yCellIndex, numCellsX, numCellsY):
        """
        :return: returns true if x,y is a valid position in the map

        """
        return not ((xCellIndex < 0) or (xCellIndex >= numCellsX) or (yCellIndex < 0) or (yCellIndex >= numCellsY))

    @staticmethod
    def AddAllNeighboursToGridNode(graph, rowIndex, colIndex, numCellsX, numCellsY):
        """
        Use to add he eight neighboring edges of a graph node that
        is positioned in a grid layout

        :param graph:
        :param rowIndex:
        :param colIndex:
        :param numCellsX:
        :param numCellsY:
        :return:
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbourNodeX = colIndex + j
                neighbourNodeY = rowIndex + i

                # Skip if equal to this node
                if (i == 0) and (j == 0):
                    continue

                # Check to see if this is a valid neighbour
                if GraphTools.IsValidNeighbour(neighbourNodeX, neighbourNodeY, numCellsX, numCellsY):
                    # Calculate the distance to this node
                    posNode = graph.GetNode(rowIndex * numCellsX + colIndex).Position
                    posNeighbour = graph.GetNode(neighbourNodeY * numCellsX + neighbourNodeX).Position

                    distanceToNeighbourNode = posNode.Distance(posNeighbour)

                    # This neighbour is okay so it can be added
                    newEdge = GraphEdgeNav(
                        rowIndex * numCellsX + colIndex,
                        neighbourNodeY * numCellsX + neighbourNodeX,
                        distanceToNeighbourNode)
                    graph.AddEdge(newEdge)

                    # If graph is not a digraph then an edge needs to be added going
                    # in the other direction
                    if not graph.IsDigraph:
                        newEdge = GraphEdgeNav(
                            neighbourNodeY * numCellsX + neighbourNodeX,
                            rowIndex * numCellsX + colIndex,
                            distanceToNeighbourNode)
                        graph.AddEdge(newEdge)

    @staticmethod
    def CreateGrid(graph, cxSize, cySize, numCellsX, numCellsY):
        """
        creates a graph based on a grid layout. This function requires the dimensions
        of the environment and the number of cells required horizontally and vertically
        :param graph:
        :param cxSize:
        :param cySize:
        :param numCellsX:
        :param numCellsY:
        :return:
        """
        if numCellsX == 0 or numCellsY == 0:
            return

        # Need some temporaries to help calculate each node center
        cellWidth = cySize / numCellsX
        cellHeight = cxSize / numCellsY

        midX = cellWidth / 2
        midY = cellHeight / 2

        # First create all the nodes
        for rowIndex in range(numCellsY):
            for colIndex in range(numCellsX):
                nodePosition = Vector2D(midX + (colIndex * cellWidth), midY + (rowIndex * cellHeight))
                node = GraphNodeNav(graph.GetNextFreeNodeIndex(), nodePosition)
                graph.AddNode(node)

        # Now to calculate the edges. (A position in a 2d array [x][y] is the same
        # as [y*NumCellsX + x] in a 1d array). Each cell has up to eight neighbours.
        for rowIndex in range(numCellsY):
            for colIndex in range(numCellsX):
                GraphTools.AddAllNeighboursToGridNode(graph, rowIndex, colIndex, numCellsX, numCellsY)

    @staticmethod
    def DrawGraph(canvas, graph, color, cellWidth, offset=0, drawGraph=True, drawNodeIds=False, graphTag="", nodeTag=""):
        """
        draws a graph using the GDI
        :param canvas:
        :param graph:
        :param color:
        :param cellWidth:
        :param offset:
        :param drawGraph:
        :param drawNodeIds:
        :param graphTag:
        :param nodeTag:
        :return:
        """
        # just return if the graph has no nodes
        if graph.NumberOfNodes() == 0:
            return

        # draw the nodes
        for node in graph.Nodes:
            if node.Index != -1:
                if drawGraph:
                    canvas.create_oval(node.Position.X-1+offset, node.Position.Y-1+offset,
                                       node.Position.X+1+offset, node.Position.Y+1+offset,
                                       fill=color, outline=color, tags=graphTag)

                    for edge in graph.GetNodeEdges(node.Index):
                        fromPosition = node.Position
                        toPosition = graph.GetNode(edge.To).Position
                        canvas.create_line(fromPosition.X+offset, fromPosition.Y+offset,
                                           toPosition.X+offset, toPosition.Y+offset,
                                           fill=color, dash="-", tags=graphTag)

                if drawNodeIds:
                    x = node.Position.X - (cellWidth/2) + 10 + (2 * (math.floor(math.log10(node.Index + 1))))
                    y = node.Position.Y - (cellWidth/2) + 10
                    canvas.create_text(x, y, text=str(node.Index), fill="grey38", font="helvetica 8", tags=nodeTag)

    @staticmethod
    def WeightNavGraphNodeEdges(graph, nodeIndex, weight):
        """
        Given a cost value and an index to a valid node this function examines
        all a node's edges, calculates their length, and multiplies the value
        with the weight. Useful for setting terrain costs.

        :param graph:
        :param nodeIndex:
        :param weight:
        :return:
        """
        # Make sure the node is present
        if nodeIndex > graph.NumberOfNodes():
            raise Exception("Invalid node index")

        # Set the cost for each edge
        for edge in graph.GetNodeEdges(nodeIndex):
            # Calculate the distance between nodes
            distance = Vector2D.Vec2DDistance(graph.GetNode(edge.From).Position, graph.GetNode(edge.To).Position)

            # Set the cost of this edge
            graph.SetEdgeCost(edge.From, edge.To, distance * weight)

            # If not a digraph, set the cost of the parallel edge to be the same
            if not graph.IsDigraph:
                graph.SetEdgeCost(edge.To, edge.From, distance * weight)

    @staticmethod
    def CreateAllPairsTable(graph):
        """
        Creates a lookup table encoding the shortest path info between each node
        in a graph to every other

        Rows represent node.From, while columns represent node.To. So to navigate a 3x3 graph,
        start at node.0 and finishing at node.8 do the following:
          - nextNodeIndex = shortestPaths[0][8] = 4
          - nextNodeIndex = shortestPaths[4][8] = 8
          - nextNodeIndex = shortestPaths[8][8] = 8
          - destination reached!

        :param graph:
        :return:
        """
        NO_PATH = -1

        # Create a 2D matrix
        shortestPaths = [[NO_PATH] * graph.NumberOfNodes() for _ in range(graph.NumberOfNodes())]

        for sourceNodeIndex in range(graph.NumberOfNodes()):
            # Calculate the SPT for this node
            search = GraphSearchDijkstra(graph, sourceNodeIndex)

            shortestPathTree = search.GetShortestPathTree()

            # Now we have the SPT it's easy to work backwards through it to find
            # the shortest paths from each node to this source node
            for targetNodeIndex in range(graph.NumberOfNodes()):
                # if the source node is the same as the target just set to target
                if sourceNodeIndex == targetNodeIndex:
                    shortestPaths[sourceNodeIndex][targetNodeIndex] = targetNodeIndex

                else:
                    nodeIndex = targetNodeIndex

                    while (nodeIndex != sourceNodeIndex) and (shortestPathTree[nodeIndex] is not None):
                        shortestPaths[shortestPathTree[nodeIndex].From][targetNodeIndex] = nodeIndex

                        nodeIndex = shortestPathTree[nodeIndex].From

        return shortestPaths

    @staticmethod
    def CreateAllPairsCostsTable(graph):
        """
        Creates a lookup table of the cost associated from traveling from one
        node to every other
        :return:
        """
        # Create a two dimensional vector
        pathCosts = [[0.0] * graph.NumberOfNodes() for _ in range(graph.NumberOfNodes())]

        for source in range(graph.NumberOfNodes()):
            # do the search
            search = GraphSearchDijkstra(graph, source)

            # iterate through every node in the graph and grab the cost to travel to that node
            for target in range(graph.NumberOfNodes()):
                if source != target:
                    pathCosts[source][target] = search.GetCostToNode(target)

        return pathCosts

    @staticmethod
    def CalculateAverageGraphEdgeLength(graph):
        """
        Determines the average length of the edges in a navGraph (using the
        distance between the source & target node positions (not the cost of the
        edge as represented in the graph, which may account for all sorts of
        other factors such as terrain type, gradients etc)

        :param graph:
        :return:
        """
        totalLength = 0
        numberOfEdgesCounted = 0

        for node in graph.Nodes:
            if node.Index != -1:
                for edge in graph.GetNodeEdges(node.Index):
                    # Increment edge counter
                    numberOfEdgesCounted += 1

                    # Add length of edge to total length
                    totalLength += Vector2D.Vec2DDistance(graph.GetNode(edge.From).Position,
                                                          graph.GetNode(edge.To).Position)

        return totalLength / numberOfEdgesCounted

    @staticmethod
    def GetCostliestGraphEdge(graph):
        """
        Returns the cost of the costliest edge in the graph
        :param graph:
        :return:
        """
        greatest = -9999999

        for node in graph.Nodes:
            if node.Index != -1:
                for edge in graph.GetNodeEdges(node.Index):
                    if edge.Cost > greatest:
                        greatest = edge.Cost

        return greatest
