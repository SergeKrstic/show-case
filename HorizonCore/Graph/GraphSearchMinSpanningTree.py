from HorizonCore.Framework.PriorityQueue import IndexedPriorityQLow


class GraphSearchMinSpanningTree:
    """
    Given a graph and a source node you can use this class to calculate
    the minimum spanning tree. If no source node is specified then the
    algorithm will calculate a spanning forest starting from node 1

    It uses a priority first queue implementation of Prims algorithm
    """

    def __init__(self, graph, sourceNodeIndex=-1):
        self._graph = graph
        self._costToThisNode = [-1] * graph.NumberOfNodes()
        self._spanningTree = [None] * graph.NumberOfNodes()
        self._fringe = [None] * graph.NumberOfNodes()

        if sourceNodeIndex < 0:
            for nodeIndex in range(graph.NumberOfNodes()):
                if self._spanningTree[nodeIndex] is None:
                    self._search(nodeIndex)

        else:
            self._search(sourceNodeIndex)

    def PrintStats(self, title):
        print("\n\n")
        print("=" * 100)
        print(title)
        print("-" * 100)
        print("")
        print("GetSpanningTree[{}]:".format(len(self.GetSpanningTree())))
        for edge in self._spanningTree:
            print("  " + str(edge))
        print("")
        print("Fringe[{}]:".format(len(self._fringe)))
        for edge in self._fringe:
            print("  " + str(edge))
        print("")
        print("CostToThisNode[{}]:\n  {}\n".format(len(self._costToThisNode), self._costToThisNode))

    def GetSpanningTree(self):
        return self._spanningTree

    def _search(self, sourceNodeIndex):
        # create a priority queue
        pq = IndexedPriorityQLow(self._costToThisNode, self._graph.NumberOfNodes())

        # put the source node on the queue
        pq.Insert(sourceNodeIndex)

        # while the queue is not empty
        while not pq.IsEmpty():
            # get lowest cost edge from the queue
            best = pq.Pop()

            # move this edge from the fringe to the spanning tree
            self._spanningTree[best] = self._fringe[best]

            # now to test the edges attached to this node
            edgeList = self._graph.GetNodeEdges(best)

            for edge in edgeList:
                priority = edge.Cost

                if self._fringe[edge.To] is None:
                    self._costToThisNode[edge.To] = priority

                    pq.Insert(edge.To)

                    self._fringe[edge.To] = edge

                elif (priority < self._costToThisNode[edge.To]) and (self._spanningTree[edge.To] is None):
                    self._costToThisNode[edge.To] = priority

                    pq.ChangePriority(edge.To)

                    self._fringe[edge.To] = edge
