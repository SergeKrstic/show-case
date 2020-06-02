from collections import deque

from HorizonCore.Framework.PriorityQueue import IndexedPriorityQLow


# Todo: consider limiting the priorityQ size to implement a beam search (see p.246)
class GraphSearchDijkstra:
    """
    Given a graph, source and optional target this class solves for
    single source shortest paths (without a target being specified) or
    shortest path from source to target.

    The algorithm used is a priority queue implementation of Dijkstra's.
    note how similar this is to the algorithm used in Graph_MinSpanningTree.
    The main difference is in the calculation of the priority in the line:

        newCost = costToThisNode[best] + edge.Cost
    """
    def __init__(self, graph, sourceNodeIndex, targetNodeIndex=-1):
        self._graph = graph
        self._sourceNodeIndex = sourceNodeIndex
        self._targetNodeIndex = targetNodeIndex

        # This is an indexed (by node) vector of 'parent' edges leading to nodes
        # connected to the SPT but that have not been added to the SPT yet. This is
        # a little like the stack or queue used in BST and DST searches.
        self._searchFrontier = [None] * graph.NumberOfNodes()

        # This vector contains the edges that comprise the shortest path tree -
        # a directed subtree of the graph that encapsulates the best paths from
        # every node on the SPT to the source node.
        self._shortestPathTree = [None] * graph.NumberOfNodes()

        # This is indexed into by node index and holds the total cost of the best
        # path found so far to the given node. For example, m_CostToThisNode[5]
        # will hold the total cost of all the edges that comprise the best path
        # to node 5, found so far in the search (if node 5 is present and has
        # been visited)
        self._costToThisNode = [0.0] * graph.NumberOfNodes()

        self._search()

    def PrintStats(self, title):
        print("\n\n")
        print("=" * 100)
        print(title)
        print("-" * 100)
        print("")
        print("ShortestPathTree[{}]:".format(len(self.GetShortestPathTree())))
        for edge in self.GetShortestPathTree():
            print("  " + str(edge))
        print("")
        print("SearchFrontier[{}]:".format(len(self._searchFrontier)))
        for edge in self._searchFrontier:
            print("  " + str(edge))
        print("")
        print("CostToThisNode[{}]:\n  {}\n".format(len(self._costToThisNode), self._costToThisNode))
        print("PathToTarget[{}]:\n  {}\n".format(len(self.GetPathToTarget()), list(self.GetPathToTarget())))

    def _search(self):
        # Create an indexed priority queue that sorts smallest to largest
        # (front to back). Note that the maximum number of elements the iPQ
        # may contain is N. This is because no node can be represented on the
        # queue more than once.
        priorityQueue = IndexedPriorityQLow(self._costToThisNode, self._graph.NumberOfNodes())

        # Put the source node index on the queue
        priorityQueue.Insert(self._sourceNodeIndex)

        # While the queue is not empty
        while not priorityQueue.IsEmpty():
            # Get lowest cost node from the queue. Don't forget, the return value
            # is a *node index*, not the node itself. This node is the node not already
            # on the SPT that is the closest to the source node
            nextClosestNodeIndex = priorityQueue.Pop()

            # Move this edge from the frontier to the shortest path tree
            self._shortestPathTree[nextClosestNodeIndex] = self._searchFrontier[nextClosestNodeIndex]

            # If the target has been found exit
            if nextClosestNodeIndex == self._targetNodeIndex:
                return

            # Now to relax the edges.
            edgesOfNextClosestNode = self._graph.GetNodeEdges(nextClosestNodeIndex)

            # For each edge connected to the next closest node
            for edge in edgesOfNextClosestNode:
                # The total cost to the node this edge points to is the cost to the
                # current node plus the cost of the edge connecting them.
                newCost = self._costToThisNode[nextClosestNodeIndex] + edge.Cost

                # If this edge has never been on the frontier make a note of the cost
                # to get to the node it points to, then add the edge to the frontier
                # and the destination node to the PQ.
                if self._searchFrontier[edge.To] is None:
                    self._costToThisNode[edge.To] = newCost

                    priorityQueue.Insert(edge.To)

                    self._searchFrontier[edge.To] = edge

                # Else test to see if the cost to reach the destination node via the
                # current node is cheaper than the cheapest cost found so far. If
                # this path is cheaper, we assign the new cost to the destination
                # node, update its entry in the PQ to reflect the change and add the
                # edge to the frontier
                elif (newCost < self._costToThisNode[edge.To]) and (self._shortestPathTree[edge.To] is None):
                    self._costToThisNode[edge.To] = newCost

                    # Because the cost is less than it was previously, the PQ must be
                    # re-sorted to account for this.
                    priorityQueue.ChangePriority(edge.To)

                    self._searchFrontier[edge.To] = edge

    def GetShortestPathTree(self):
        """
        Returns the vector of edges that defines the SPT. If a target was given
        in the constructor then this will be an SPT comprising of all the nodes
        examined before the target was found, else it will contain all the nodes
        in the graph.
        :return:
        """
        return self._shortestPathTree

    def GetPathToTarget(self):
        """
        Returns a vector of node indexes that comprise the shortest path
        rom the source to the target. It calculates the path by working
        backwards through the SPT from the target node.
        :return:
        """
        path = deque()

        # just return an empty path if no target or no path found
        if self._targetNodeIndex < 0:
            return path

        nodeIndex = self._targetNodeIndex

        path.appendleft(nodeIndex)

        while (nodeIndex != self._sourceNodeIndex) and (self._shortestPathTree[nodeIndex] is not None):
            nodeIndex = self._shortestPathTree[nodeIndex].From

            path.appendleft(nodeIndex)

        return path

    def GetCostToTarget(self):
        """
        returns the total cost to the target
        :return:
        """
        return self._costToThisNode[self._targetNodeIndex]

    def GetCostToNode(self, nodeIndex):
        """
        returns the total cost to the given node
        :param nodeIndex:
        :return:
        """
        return self._costToThisNode[nodeIndex]
