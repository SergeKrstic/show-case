"""
    Classes to implement graph algorithms, including DFS, BFS,
    Dijkstra's, A*, Prims etc. (based upon the code created
    by Robert Sedgewick in his book "Algorithms in C++")

    Any graphs passed to these functions must conform to the
    same interface used by the SparseGraph
"""
from collections import deque

from HorizonCore.Graph.GraphEdge import GraphEdge


DEBUG_ENABLED = False


class NodeState:
    NoParentAssigned = -1
    Unvisited = 0
    Visited = 1


class GraphSearchDFS:
    """
    Class to implement a depth first search.
    Todo: consider creating Depth-Limited-Search (DLS) algorithm (see p.222)
    Todo: consider creating Iterative-Deepening-Deep-Depth-First-Search (IDDFS) algorithm (see p.222)
    Todo: consider implementing a search algorithm that expands the graph is it goes along (see p.222)
    """

    def __init__(self, graph, sourceNodeIndex, targetNodeIndex=-1):
        # A reference to the graph to be searched
        self._graph = graph

        # This records the indexes of all the nodes that are visited as the
        # search progresses
        self._visited = [NodeState.Unvisited] * graph.NumberOfNodes()

        # this holds the route taken to the target. Given a node index, the value
        # at that index is the node's parent. ie if the path to the target is
        # 3-8-27, then m_Route[8] will hold 3 and m_Route[27] will hold 8.
        self._routeNodeToParent = [NodeState.NoParentAssigned] * graph.NumberOfNodes()

        # As the search progresses, this will hold all the edges the algorithm has
        # examined. THIS IS NOT NECESSARY FOR THE SEARCH, IT IS HERE PURELY
        # TO PROVIDE THE USER WITH SOME VISUAL FEEDBACK
        self._spanningTree = []

        # The source and target node indices
        self._sourceNodeIndex = sourceNodeIndex
        self._targetNodeIndex = targetNodeIndex

        # True if a path to the target has been found
        self._found = False

        self._found = self._search()

    def PrintStats(self, title):
        print("\n\n")
        print("="*100)
        print(title)
        print("-"*100)
        print("")
        print("SpanningTree[{}]:".format(len(self.GetSearchTree())))
        for edge in self.GetSearchTree():
            print("  " + str(edge))
        print("")
        print("Visited[{}]:\n  {}\n".format(len(self._visited), self._visited))
        print("RouteNodeToParent[{}]:\n  {}\n".format(len(self._routeNodeToParent), self._routeNodeToParent))
        print("PathToTarget[{}]:\n  {}\n".format(len(self.GetPathToTarget()), list(self.GetPathToTarget())))

    def _search(self):
        """
        This method performs the DFS search
        """
        # Create a standard stack of edges (LIFO)
        stack = []

        # Create a dummy edge and put on the stack
        dummyEdge = GraphEdge(self._sourceNodeIndex, self._sourceNodeIndex, cost=0)

        stack.append(dummyEdge)

        # While there are edges in the stack keep searching
        while len(stack) > 0:
            # Grab the next edge and remove the edge from the stack
            nextEdge = stack.pop()

            # Make a note of the parent of the node this edge points to
            self._routeNodeToParent[nextEdge.To] = nextEdge.From

            # Put it on the tree. (making sure the dummy edge is not placed on the tree)
            if nextEdge != dummyEdge:
                self._spanningTree.append(nextEdge)

            # and mark it visited
            self._visited[nextEdge.To] = NodeState.Visited

            # if the target has been found the method can return success
            if nextEdge.To == self._targetNodeIndex:
                return True

            # Push the edges leading from the node this edge points to onto the
            # stack (provided the edge does not point to a previously visited node)
            edgeList = self._graph.GetNodeEdges(nextEdge.To)

            for edge in edgeList:
                if self._visited[edge.To] == NodeState.Unvisited:
                    stack.append(edge)

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
