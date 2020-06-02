from HorizonCore.Graph.NodeType import NodeType
# import pyximport
# pyximport.install()


class GraphNode:
    """
    Node classes to be used with graphs
    """
    def __init__(self, index=NodeType.InvalidNodeIndex):
        # Every node has an index. A valid index is >= 0
        self._index = index.value if isinstance(index, NodeType) else index
        # cdef int _index = index.value if isinstance(index, NodeType) else index

    @property
    def Index(self):
        return self._index

    @Index.setter
    def Index(self, index):
        self._index = index.value if isinstance(index, NodeType) else index

    def __repr__(self):
        return "Index: {}".format(self.Index)
