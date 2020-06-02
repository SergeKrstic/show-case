from HorizonCore.Framework.PriorityQueue import IndexedPriorityQLow


class GraphSearchAStar:
    """
    This searches a graph using the distance between the target node and the
    currently considered node as a heuristic.

    This search is more commonly known as A* (pronounced Ay-Star)
    """
    def __init__(self, graph, sourceNodeIndex, targetNodeIndex, heuristic):
        self._graph = graph
        self._heuristic = heuristic

        # Indexed into by node. Contains the 'real' accumulative cost to that node
        self._gCosts = [0] * graph.NumberOfNodes()

        # Indexed into by node. Contains the cost from adding m_GCosts[n] to
        # the heuristic cost from n to the target node. This is the vector the
        # iPQ indexes into.
        self._fCosts = [0] * graph.NumberOfNodes()

        self._shortestPathTree = [None] * graph.NumberOfNodes()
        self._searchFrontier = [None] * graph.NumberOfNodes()
        self._sourceNodeIndex = sourceNodeIndex
        self._targetNodeIndex = targetNodeIndex

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
        print("gCosts[{}]:\n  {}\n".format(len(self._gCosts), self._gCosts))
        print("fCosts[{}]:\n  {}\n".format(len(self._fCosts), self._fCosts))
        print("PathToTarget[{}]:\n  {}\n".format(len(self.GetPathToTarget()), list(self.GetPathToTarget())))

    def _search(self):
        """
        the A* search algorithm
        :return:
        """
        if self._targetNodeIndex < 0:
            # A target is required for AStar
            return

        # create an indexed priority queue of nodes. The nodes with the
        # lowest overall F cost (G+H) are positioned at the front.
        pq = IndexedPriorityQLow(self._fCosts, self._graph.NumberOfNodes())

        # put the source node on the queue
        pq.Insert(self._sourceNodeIndex)

        # while the queue is not empty
        while not pq.IsEmpty():
            # get lowest cost node from the queue
            nextClosestNode = pq.Pop()

            # move this node from the frontier to the spanning tree
            self._shortestPathTree[nextClosestNode] = self._searchFrontier[nextClosestNode]

            # if the nextClosestNode has been found exit
            if nextClosestNode == self._targetNodeIndex:
                return

            # now to test all the edges attached to this node
            edgeList = self._graph.GetNodeEdges(nextClosestNode)

            for edge in edgeList:
                # calculate the heuristic cost from this node to the target (H)
                hCost = self._heuristic.Calculate(self._graph, self._targetNodeIndex, edge.To)

                # calculate the 'real' cost to this node from the source (G)
                gCost = self._gCosts[nextClosestNode] + edge.Cost

                # if the node has not been added to the frontier, add it and update
                # the G and F costs
                if self._searchFrontier[edge.To] is None:
                    self._fCosts[edge.To] = gCost + hCost
                    self._gCosts[edge.To] = gCost

                    pq.Insert(edge.To)

                    self._searchFrontier[edge.To] = edge

                    # if this node is already on the frontier but the cost to get here
                    # is cheaper than has been found previously, update the node
                    # costs and frontier accordingly.
                elif (gCost < self._gCosts[edge.To]) and (self._shortestPathTree[edge.To] is None):
                    self._fCosts[edge.To] = gCost + hCost
                    self._gCosts[edge.To] = gCost

                    pq.ChangePriority(edge.To)

                    self._searchFrontier[edge.To] = edge

    def GetShortestPathTree(self):
        """
        :return: returns the vector of edges that the algorithm has examined
        """
        return self._shortestPathTree

    def GetPathToTarget(self):
        """
        :return: returns a vector of node indexes that comprise the shortest path
                from the source to the target
        """
        path = []

        # just return an empty path if no target or no path found
        if self._targetNodeIndex < 0:
            return path

        nodeIndex = self._targetNodeIndex

        path.insert(0, nodeIndex)

        while (nodeIndex != self._sourceNodeIndex) and (self._shortestPathTree[nodeIndex] is not None):
            nodeIndex = self._shortestPathTree[nodeIndex].From

            path.insert(0, nodeIndex)

        return path

    def GetCostToTarget(self):
        return self._gCosts[self._targetNodeIndex]
