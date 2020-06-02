# Todo: consider 'PathFinderBFS' as a class name instead of 'GraphSearchBFS'
from collections import deque

from HorizonCore.Graph.GraphEdge import GraphEdge


class NodeState:
    NoParentAssigned = -1
    Unvisited = 0
    Visited = 1


class GraphSearchBFS:
    """
    Class to implement a depth first search.
    Todo: consider implementing a bidirectional search to speed up the algorithm (see p.229)
    Todo: consider implementing a search algorithm that expands the graph is it goes along (see p.230-231)
    """

    def __init__(self, graph, sourceNodeIndex, targetNodeIndex=-1):
        # A reference to the graph to be searched
        self._graph = graph

        # This records the indexes of all the nodes that are visited as the search progresses
        self._visited = [NodeState.Unvisited] * graph.NumberOfNodes()

        # this holds the route taken to the target. Given a node index, the value
        # at that index is the node's parent. ie if the path to the target is
        # 3-8-27, then m_Route[8] will hold 3 and m_Route[27] will hold 8.
        self._routeNodeToParent = [NodeState.NoParentAssigned] * graph.NumberOfNodes()

        # As the search progresses, this will hold all the edges the algorithm has
        # examined. THIS IS NOT NECESSARY FOR THE SEARCH, IT IS HERE PURELY
        # TO PROVIDE THE USER WITH SOME VISUAL FEEDBACK
        self._spanningTree = []

        # the source and target node indices
        self._sourceNodeIndex = sourceNodeIndex
        self._targetNodeIndex = targetNodeIndex

        # true if a path to the target has been found
        self._found = False

        self._found = self._search()

    def PrintStats(self, title):
        print("\n\n")
        print("=" * 100)
        print(title)
        print("-" * 100)
        print("")
        print("SpanningTree[{}]:".format(len(self.GetSearchTree())))
        for edge in self.GetSearchTree():
            print("  " + str(edge))
        print("")
        print("Visited[{}]:\n  {}\n".format(len(self._visited), self._visited))
        print("RouteNodeToParent[{}]:\n  {}\n".format(len(self._routeNodeToParent), self._routeNodeToParent))
        print("PathToTarget[{}]:\n  {}\n".format(len(self.GetPathToTarget()), list(self.GetPathToTarget())))

    def _search(self):
        # Create a standard queue of edges
        queue = deque()

        dummy = GraphEdge(self._sourceNodeIndex, self._sourceNodeIndex, 0)

        # Create a dummy edge and put on the queue
        queue.appendleft(dummy)

        # Mark the source node as visited
        self._visited[self._sourceNodeIndex] = NodeState.Visited

        # While there are edges in the queue keep searching
        while len(queue) > 0:
            # Grab the next edge
            nextEdge = queue.pop()

            # Mark the parent of this node
            self._routeNodeToParent[nextEdge.To] = nextEdge.From

            # Put it on the tree. (making sure the dummy edge is not placed on the tree)
            if nextEdge != dummy:
                self._spanningTree.append(nextEdge)

            # Exit if the target has been found
            if nextEdge.To == self._targetNodeIndex:
                return True

            # Push the edges leading from the node at the end of this edge onto the queue
            edgeList = self._graph.GetNodeEdges(nextEdge.To)

            for edge in edgeList:
                # If the node hasn't already been visited we can push the edge onto the queue
                if self._visited[edge.To] == NodeState.Unvisited:
                    queue.appendleft(edge)

                    # and mark it visited
                    self._visited[edge.To] = NodeState.Visited

        # No path to target
        return False

    def GetSearchTree(self):
        """
        :return: returns a vector containing pointers to all the edges the search has examined
        """
        return self._spanningTree

    def Found(self):
        return self._found

    def GetPathToTarget(self):
        """
        Returns a vector of node indexes that comprise the shortest path from the source to the target
        :return: 
        """
        path = deque()

        # Just return an empty path if no path to target found or if
        # no target has been specified
        if not self._found or self._targetNodeIndex < 0:
            return path

        nodeIndex = self._targetNodeIndex

        path.appendleft(nodeIndex)

        while nodeIndex != self._sourceNodeIndex:
            nodeIndex = self._routeNodeToParent[nodeIndex]

            path.appendleft(nodeIndex)

        return path


