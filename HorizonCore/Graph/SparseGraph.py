from HorizonCore.Graph.GraphEdge import GraphEdge
from HorizonCore.Graph.GraphEdgeNav import GraphEdgeNav
from HorizonCore.Graph.GraphNode import GraphNode
from HorizonCore.Graph.GraphNodeNav import GraphNodeNav
from HorizonCore.Graph.NodeType import NodeType


class SparseGraph:
    """
    Graph class using the adjacency list representation.
    """

    def __init__(self, isDigraph, nodeClass=GraphNode, edgeClass=GraphEdge):
        # The nodes that comprise this graph
        self._nodes = []

        # A vector of adjacency edge lists. (each node index keys into the
        # list of edges associated with that node)
        self._edgeListVector = []

        # Is this a directed graph?
        self._isDigraph = isDigraph

        # The index of the next node to be added
        self._nextNodeIndex = 0

        self._nodeClass = nodeClass
        self._edgeClass = edgeClass

    def _createNode(self, nodeIndex):
        return self._nodeClass(nodeIndex)

    def _createEdge(self, fromNodeIndex, toNodeIndex, cost):
        return self._edgeClass(fromNodeIndex, toNodeIndex, cost)

    @staticmethod
    def CreateNavGraph(isDigraph):
        return SparseGraph(isDigraph, nodeClass=GraphNodeNav, edgeClass=GraphEdgeNav)

    @property
    def IsDigraph(self):
        """
        returns true if the graph is directed
        :return:
        """
        return self._isDigraph

    @property
    def IsEmpty(self):
        """
        returns true if the graph contains no nodes
        :return:
        """
        return len(self._nodes) == 0

    @property
    def Nodes(self):
        return self._nodes

    def GetNodeEdges(self, nodeIndex):
        return self._edgeListVector[nodeIndex]

    def GetNextFreeNodeIndex(self):
        """
        Retrieves the next free node index
        """
        return self._nextNodeIndex

    def AddNode(self, node):
        """
        Adds a node to the graph and returns its index

        Given a node this method first checks to see if the node has been added
        previously but is now inactive. If it is, it is reactivated.

        If the node has not been added previously, it is checked to make sure its
        index matches the next node index before being added to the graph

        :param node: The node to add to the graph
        :return: Return the node's index
        """
        if node.Index < len(self._nodes):
            # Make sure the client is not trying to add a node with the same ID as
            # a currently active node
            if self._nodes[node.Index].Index != NodeType.InvalidNodeIndex.value:
                raise Exception("<SparseGraph::AddNode>: Attempting to add a node with a duplicate ID")

            self._nodes[node.Index] = node

            return self._nextNodeIndex
        else:
            # Make sure the new node has been indexed correctly
            if node.Index != self._nextNodeIndex:
                raise Exception("<SparseGraph::AddNode>:invalid index")

            self._nodes.append(node)
            self._edgeListVector.append([])

            self._nextNodeIndex += 1

            return self._nextNodeIndex

    def GetNode(self, index):
        """
        Method for obtaining a reference to a specific node
        :param index:
        :return: Returns the node at the given index
        """
        self._raiseExceptionIfIndexIsOutOfRange(index, "GetNode")

        return self._nodes[index]

    def _raiseExceptionIfIndexIsOutOfRange(self, index, functionName):
        if index < 0 or index >= len(self._nodes):
            raise Exception("<SparseGraph.{}>: invalid index".format(functionName))

    def RemoveNode(self, nodeIndex):
        """
        Removes a node from the graph and removes any links to neighbouring nodes
        :param nodeIndex:
        """
        self._raiseExceptionIfIndexIsOutOfRange(nodeIndex, "RemoveNode")

        # Set this node's index to invalid_node_index
        self._nodes[nodeIndex].Index = NodeType.InvalidNodeIndex.value

        # If the graph is not directed remove all edges leading to this node and then
        # clear the edges leading from the node
        if not self._isDigraph:
            # Visit each neighbour and erase any edges leading to this node
            for nodeEdge in self._edgeListVector[nodeIndex]:
                for neighbourNodeEdge in self._edgeListVector[nodeEdge.To]:
                    if neighbourNodeEdge.To == nodeIndex:
                        self._edgeListVector[neighbourNodeEdge.From].remove(neighbourNodeEdge)
                        break

        # if a digraph then remove the edges the slow way
        else:
            self._cullInvalidEdges()

        # Finally, clear this node's edges
        self._edgeListVector[nodeIndex].clear()

    def _cullInvalidEdges(self):
        """
        Iterates through all the edges in the graph and removes any that point
        to an invalidated node
        :return:
        """
        for edgeList in self._edgeListVector:
            for edge in edgeList:
                if self._nodes[edge.To].Index == NodeType.InvalidNodeIndex.value or \
                   self._nodes[edge.From].Index == NodeType.InvalidNodeIndex.value:
                    edgeList.remove(edge)

    def AddEdge(self, edge):
        """
        Use this to add an edge to the graph. The method will ensure that the
        edge passed as a parameter is valid before adding it to the graph. If the
        graph is a digraph then a similar edge connecting the nodes in the opposite
        direction will be automatically added.
        :param edge:
        """
        # First make sure the from and to nodes exist within the graph
        self._raiseExceptionIfIndexIsOutOfRange(edge.From, "AddEdge")
        self._raiseExceptionIfIndexIsOutOfRange(edge.To, "AddEdge")

        # Make sure both nodes are active before adding the edge
        if self._nodes[edge.To].Index != NodeType.InvalidNodeIndex.value and \
           self._nodes[edge.From].Index != NodeType.InvalidNodeIndex.value:

            # Add the edge, first making sure it is unique
            if self._isUniqueEdge(edge.From, edge.To):
                self._edgeListVector[edge.From].append(edge)

            # If the graph is undirected we must add another connection in the opposite direction
            if not self._isDigraph:
                # Check to make sure the edge is unique before adding
                if self._isUniqueEdge(edge.To, edge.From):
                    newEdge = self._createEdge(fromNodeIndex=edge.To, toNodeIndex=edge.From, cost=edge.Cost)
                    self._edgeListVector[edge.To].append(newEdge)

    def _isUniqueEdge(self, fromNodeIndex, toNodeIndex):
        """
        Returns true if an edge is not already present in the graph. Used
        when adding edges to make sure no duplicates are created.
        :param fromNodeIndex:
        :param toNodeIndex:
        :return:
        """
        for edge in self._edgeListVector[fromNodeIndex]:
            if edge.To == toNodeIndex:
                return False

        return True

    def GetEdge(self, fromNodeIndex, toNodeIndex):
        """
        Method for obtaining a reference to a specific edge
        :param fromNodeIndex:
        :param toNodeIndex:
        :return:
        """
        if (fromNodeIndex < 0) or (fromNodeIndex >= len(self._nodes)) or \
                self._nodes[fromNodeIndex].Index == NodeType.InvalidNodeIndex.value:
            raise Exception("<SparseGraph::GetEdge>: invalid 'from' index")

        if (toNodeIndex < 0) or (toNodeIndex >= len(self._nodes)):
            raise Exception("<SparseGraph::GetEdge>: invalid 'to' index")

        for edge in self._edgeListVector[fromNodeIndex]:
            if edge.To == toNodeIndex:
                return edge

        raise Exception("<SparseGraph::GetEdge>: edge does not exist")

    def RemoveEdge(self, fromNodeIndex, toNodeIndex):
        """
        Removes the edge connecting from and to from the graph (if present). If
        a digraph then the edge connecting the nodes in the opposite direction
        will also be removed.
        :param fromNodeIndex:
        :param toNodeIndex:
        """
        self._raiseExceptionIfIndexIsOutOfRange(fromNodeIndex, "RemoveEdge")
        self._raiseExceptionIfIndexIsOutOfRange(toNodeIndex, "RemoveEdge")

        if not self._isDigraph:
            for edge in self._edgeListVector[toNodeIndex]:
                if edge.To == fromNodeIndex:
                    self._edgeListVector[toNodeIndex].remove(edge)
                    break

        for edge in self._edgeListVector[fromNodeIndex]:
            if edge.To == toNodeIndex:
                self._edgeListVector[fromNodeIndex].remove(edge)
                break

    def SetEdgeCost(self, fromNodeIndex, toNodeIndex, cost):
        """
        Sets the cost of a specific edge
        :param fromNodeIndex:
        :param toNodeIndex:
        :param cost:
        """
        self._raiseExceptionIfIndexIsOutOfRange(fromNodeIndex, "SetEdgeCost")
        self._raiseExceptionIfIndexIsOutOfRange(toNodeIndex, "SetEdgeCost")

        for edge in self._edgeListVector[fromNodeIndex]:
            if edge.To == toNodeIndex:
                edge.Cost = cost
                break

    def NumberOfNodes(self):
        """
        Returns the number of active + inactive nodes present in the graph
        :return:
        """
        return len(self._nodes)

    def NumberOfActiveNodes(self):
        """
        Returns the number of active nodes present in the graph (this method's
        performance can be improved greatly by caching the value)
        :return:
        """
        count = 0
        for node in self._nodes:
            if node.Index != NodeType.InvalidNodeIndex.value:
                count += 1
        return count

    def NumberOfEdges(self):
        """
        returns the total number of edges present in the graph
        :return:
        """
        count = 0
        for edgeList in self._edgeListVector:
            count += len(edgeList)
        return count

    def IsNodePresent(self, nodeIndex):
        """
        Returns true if a node with the given index is present in the graph
        :param nodeIndex:
        :return:
        """
        if nodeIndex < 0 or nodeIndex >= len(self._nodes) or \
           self._nodes[nodeIndex].Index == NodeType.InvalidNodeIndex.value:
            return False
        else:
            return True

    def IsEdgePresent(self, fromNodeIndex, toNodeIndex):
        """
        returns true if an edge connecting the nodes 'to' and 'from'
        is present in the graph
        :param fromNodeIndex:
        :param toNodeIndex:
        :return:
        """
        if self.IsNodePresent(fromNodeIndex) and self.IsNodePresent(toNodeIndex):
            for edge in self._edgeListVector[fromNodeIndex]:
                if edge.To == toNodeIndex:
                    return True
            return False
        else:
            return False

    def Clear(self):
        self._nextNodeIndex = 0
        self._nodes.clear()
        self._edgeListVector.clear()

    def RemoveEdges(self):
        for edgeList in self._edgeListVector:
            edgeList.clear()

    def Save(self, fileName):
        """
        Methods for loading and saving graphs from an open file stream or from a file name
        :param fileName:
        """
        try:
            with open(fileName, 'w') as file:
                file.write(str(self._isDigraph) + "\n")
                file.write(str(self.NumberOfNodes()) + "\n")

                for node in self._nodes:
                    file.writelines(str(node) + "\n")

                file.write(str(self.NumberOfEdges()) + "\n")

                for edgeList in self._edgeListVector:
                    for edge in edgeList:
                        file.write(str(edge) + "\n")

        except IOError:
            raise Exception("Cannot open file: " + fileName)

    def Load(self, fileName):
        """
        Methods for loading and saving graphs from an open file stream or from a file name
        :param fileName:
        """
        try:
            with open(fileName, 'r') as file:
                self.Clear()

                self._isDigraph = bool(file.readline())

                # Get the number of nodes and read them in
                numberOfNodes = int(file.readline())

                for nodeIndex in range(numberOfNodes):
                    newNodeData = file.readline()
                    newNodeIndex = int(newNodeData.split(":")[1])
                    newNode = self._createNode(newNodeIndex)

                    # When editing graphs it's possible to end up with a situation where some
                    # of the nodes have been invalidated (their id's set to invalid_node_index). Therefore
                    # when a node of index invalid_node_index is encountered, it must still be added.

                    if newNode.Index != NodeType.InvalidNodeIndex.value:
                        self.AddNode(newNode)
                    else:
                        self._nodes.append(newNode)

                        # Make sure an edgeList is added for each node
                        self._edgeListVector.append([])

                        self._nextNodeIndex += 1

                # Get the number of nodes and read them in
                numberOfEdges = int(file.readline())

                # now add the edges
                for edgeIndex in range(numberOfEdges):
                    newEdgeData = file.readline().split("|")
                    fromIndex = int(newEdgeData[0].split(":")[1])
                    toIndex = int(newEdgeData[1].split(":")[1])
                    cost = float(newEdgeData[2].split(":")[1])
                    nextEdge = GraphEdge(fromIndex, toIndex, cost)

                    self._edgeListVector[nextEdge.From].append(nextEdge)

            return True

        except IOError:
            raise Exception("Cannot open file: " + fileName)

    def __repr__(self):
        outputString = ""
        for node in self._nodes:
            outputString += "Node {} \n".format(str(node))
            if node.Index != NodeType.InvalidNodeIndex.value:
                for edge in self._edgeListVector[node.Index]:
                    outputString += "  - Edge [{}] \n".format(str(edge))
        return outputString
