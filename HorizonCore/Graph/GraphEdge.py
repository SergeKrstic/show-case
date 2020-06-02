from HorizonCore.Graph.NodeType import NodeType


class GraphEdge:
    """
    Class to define an edge connecting two nodes where an edge has an associated cost.
    """

    def __init__(self,
                 fromNodeIndex=NodeType.InvalidNodeIndex,
                 toNodeIndex=NodeType.InvalidNodeIndex,
                 cost=1.0):

        # An edge connects two nodes. Valid node indices are always positive.
        self._fromNodeIndex = fromNodeIndex if isinstance(fromNodeIndex, int) else fromNodeIndex.value
        self._toNodeIndex = toNodeIndex if isinstance(toNodeIndex, int) else toNodeIndex.value

        # the cost of traversing the edge
        self._cost = cost

    @property
    def From(self):
        return self._fromNodeIndex

    @From.setter
    def From(self, value):
        self._fromNodeIndex = value

    @property
    def To(self):
        return self._toNodeIndex

    @To.setter
    def To(self, value):
        self._toNodeIndex = value

    @property
    def Cost(self):
        return self._cost

    @Cost.setter
    def Cost(self, value):
        self._cost = value

    def __eq__(self, other):
        return (self.From == other.From) and \
               (self.To == other.To) and \
               (self.Cost == other.Cost)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "From: {} | To: {} | Cost: {}".format(self.From, self.To, self.Cost)
