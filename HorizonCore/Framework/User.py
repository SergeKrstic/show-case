from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.UserFeatureMap import UserFeatureMap


class User(BaseEntity):

    def __init__(self, entityId):
        super().__init__(entityId)
        self._features = UserFeatureMap()

    @property
    def Features(self):
        return self._features

    def Update(self):
        raise NotImplementedError

    def HandleTelegram(self, telegram):
        raise NotImplementedError
