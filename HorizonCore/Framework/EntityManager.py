from enum import Enum

from HorizonCore.Framework.Singleton import Singleton

"""
To facilitate quick lookup the entities are stored in a dictionary, in which
references to entities are cross referenced by their identifying number
"""
EntityMap = {}


class EntityManager(metaclass=Singleton):

    @staticmethod
    def RegisterEntity(newEntity):
        """
        This method stores a reference to the entity in the dictionary EntityMap at
        the index position indicated by the entity's ID (makes for faster access)
        """
        EntityMap[newEntity.Id] = newEntity

    @staticmethod
    def GetEntityFromID(entityId):
        """
        Gets the entity with matching id
        :param entityId: Id of entity (can be either a integer or enum)
        :return: returns a reference to the entity with the ID given as a parameter
        """
        if isinstance(entityId, Enum):
            entityId = entityId.value
        return EntityMap[entityId]

    @staticmethod
    def RemoveEntity(entity):
        """
        This method removes the entity from the map
        :param entity: reference to the entity
        """
        del EntityMap[entity.Id]

    @staticmethod
    def Reset():
        """
        Clears the Entity Map
        """
        global EntityMap
        EntityMap = {}

    @staticmethod
    def _getEntityMap():
        """
        Helper method used in unit tests to get direct access to the entity map
        :return: Returns the entity map
        """
        return EntityMap
