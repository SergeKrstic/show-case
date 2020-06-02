from HorizonCore.Graph.GraphNode import GraphNode


class GraphNodeNav(GraphNode):
    """
    Graph node for use in creating a navigation graph. This node contains
    the position of the node and a pointer to a BaseGameEntity... useful
    if you want your nodes to represent health packs, gold mines and the like
    """

    def __init__(self, index, position, extraInfo=None):
        super().__init__(index)

        # The node's position
        self._position = position

        # Often you will require a NavGraph node to contain additional information.
        # For example a node might represent a pickup such as armor in which
        # case _extraInfo could be an enumerated value denoting the pickup type,
        # thereby enabling a search algorithm to search a graph for specific items.
        # Going one step further, _extraInfo could be a pointer to the instance of
        # the item type the node is twinned with. This would allow a search algorithm
        # to test the status of the pickup during the search.
        self._extraInfo = extraInfo

    @property
    def Position(self):
        return self._position

    @Position.setter
    def Position(self, value):
        self._position = value

    @property
    def ExtraInfo(self):
        return self._extraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, value):
        self._extraInfo = value

    def __repr__(self):
        return "Index: {} | Position: ({:.2f}, {:.2f}) | ExtraInfo: '{}'".format(
            self.Index, self.Position.X, self.Position.Y, self.ExtraInfo)
