from enum import Enum

from HorizonCore.Framework.Enums import Entity

"""Global static variable used to create unique IDs for each entity"""
NextValidId = 0


class BaseEntity:

    def __init__(self, entityId=None, entityType=Entity.DefaultType, isTagged=False):
        self._id = None
        self._type = entityType
        self._isTagged = isTagged

        self._setId(entityId)

    # Properties
    # ==========================================================================

    @property
    def Id(self):
        """
        :return: Returns the ID of the entity
        """
        return self._id

    def _setId(self, value):
        """
        Sets the id of the entity, ensuring that it is unique,
        otherwise an exception is raised

        - If an enum is used as the ID, it is assumed to be unique by design (e.g. specialised coaches)

        - Integer can also be used, this allows an array of agents to be created (e.g. soccer players)

        - If no value is supplied, then the next available is integer is used

        :param value: Id of entity (can be an enum or an integer)
        """
        if isinstance(value, Enum):
            # Enums are assumed to be unique by design
            self._id = value.value
        elif isinstance(value, int):
            # Enum integers are unique
            if value >= self.GetNextValidId():
                self._id = value
                self.UpdatedNextValidId(value)
            else:
                raise ValueError("Id is not unique")
        elif value is None:
            # Auto generate a unique integer
            self._id = self.GetNextValidId()
            self.IncrementNextValidId()

    @property
    def EntityType(self):
        return self._type

    @EntityType.setter
    def EntityType(self, value):
        self._type = value

    @property
    def ActionMap(self):
        raise NotImplementedError

    # Methods
    # ==========================================================================

    def Update(self):
        raise NotImplementedError

    def HandleTelegram(self, telegram):
        raise NotImplementedError

    def IsTagged(self):
        return self._isTagged

    def Tag(self):
        self._isTagged = True

    def UnTag(self):
        self._isTagged = False

    # Helper Methods
    # ==========================================================================

    @staticmethod
    def GetNextValidId():
        global NextValidId
        return NextValidId

    @staticmethod
    def IncrementNextValidId():
        global NextValidId
        NextValidId += 1

    @staticmethod
    def UpdatedNextValidId(value):
        global NextValidId
        NextValidId = value + 1

    @staticmethod
    def ResetNextValidId():
        global NextValidId
        NextValidId = 0

