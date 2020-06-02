"""
    Class templates defining a heuristic policy for use with the A* search algorithm
"""
from numpy.random import uniform


from HorizonCore.Framework.Vector2D import Vector2D


class Heuristic:
    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        raise NotImplementedError


class HeuristicEuclidean(Heuristic):
    """
    The euclidean heuristic (straight-line distance)
    """
    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        """
        Calculate the straight line distance from node nodeIndex1 to node nodeIndex2
        :param graph:
        :param nodeIndex1:
        :param nodeIndex2:
        :return:
        """
        return Vector2D.Vec2DDistance(
            graph.GetNode(nodeIndex1).Position,
            graph.GetNode(nodeIndex2).Position)


class HeuristicNoisyEuclidean(Heuristic):
    """
    This uses the euclidean distance but adds in an amount of noise to the
    result. You can use this heuristic to provide imperfect paths. This can
    be handy if you find that you frequently have lots of agents all following
    each other in single file to get from one place to another
    """

    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        """
        Calculate the straight line distance from node nodeIndex1 to node nodeIndex2
        :param graph:
        :param nodeIndex1:
        :param nodeIndex2:
        :return:
        """
        return Vector2D.Vec2DDistance(
            graph.GetNode(nodeIndex1).Position,
            graph.GetNode(nodeIndex2).Position) * uniform(0.9, 1.1)


class HeuristicDijkstra(Heuristic):
    """
    You can use this class to turn the A* algorithm into Dijkstra's search.
    this is because Dijkstra's is equivalent to an A* search using a heuristic
    value that is always equal to zero.
    """

    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        return 0


class HeuristicManhattan(Heuristic):
    """
    The manhattan distance heuristic (x + y distance)
    """

    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        n1 = graph.GetNode(nodeIndex1).Position
        n2 = graph.GetNode(nodeIndex2).Position
        ySeparation = abs(n2.Y - n1.Y)
        xSeparation = abs(n2.X - n1.X)

        return ySeparation + xSeparation


class HeuristicEuclideanSquared(Heuristic):
    """
    The euclidean-squared heuristic (straight-line distance)
    """

    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        return Vector2D.Vec2DDistanceSq(
            graph.GetNode(nodeIndex1).Position,
            graph.GetNode(nodeIndex2).Position)


class HeuristicNoisyEuclideanSquared(Heuristic):
    """
    The noisy euclidean heuristic (straight-line distance)
    """

    @staticmethod
    def Calculate(graph, nodeIndex1, nodeIndex2):
        return Vector2D.Vec2DDistanceSq(
            graph.GetNode(nodeIndex1).Position,
            graph.GetNode(nodeIndex2).Position) * uniform(0.9, 1.1)
