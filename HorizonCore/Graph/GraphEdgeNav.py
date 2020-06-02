from enum import Enum

from HorizonCore.Graph.GraphEdge import GraphEdge
from HorizonCore.Graph.NodeType import NodeType


# Examples of typical flags
class Flags(Enum):
    Normal = 0
    Swim = 1 << 0
    Crawl = 1 << 1
    Creep = 1 << 3
    Jump = 1 << 3
    Fly = 1 << 4
    Grapple = 1 << 5
    GoesThroughDoor = 1 << 6


class GraphEdgeNav(GraphEdge):

    def __init__(self, fromNodeIndex, toNodeIndex, cost=1.0, flags=Flags.Normal, idOfIntersectingEntity=NodeType.InvalidNodeIndex):
        super().__init__(fromNodeIndex, toNodeIndex, cost)
        self._flags = flags if isinstance(flags, int) else flags.value

        # If this edge intersects with an object (such as a door or lift), then this is that object's ID.
        self._idOfIntersectingEntity = idOfIntersectingEntity if isinstance(idOfIntersectingEntity, int) else idOfIntersectingEntity.value

    @property
    def Flags(self):
        return self._flags

    @Flags.setter
    def Flags(self, value):
        self._flags = value

    @property
    def IdOfIntersectingEntity(self):
        return self._idOfIntersectingEntity

    @IdOfIntersectingEntity.setter
    def IdOfIntersectingEntity(self, value):
        self._idOfIntersectingEntity = value

    def __repr__(self):
        return "From: {} | To: {} | Cost: {:.2f} | Flags: {} | IdOfIntersectingEntity: {}".format(
            self.From, self.To, self.Cost, self.Flags, self.IdOfIntersectingEntity)
