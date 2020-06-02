from HorizonCore.Framework.Singleton import Singleton


class State(metaclass=Singleton):

    def Enter(self, entity):
        """This will execute when the state is entered"""
        pass

    def Execute(self, entity):
        """This is the states normal update function, it must be overridden"""
        raise NotImplementedError

    def Exit(self, entity):
        """This will execute when the state is exited."""
        pass

    def OnTelegram(self, entity, telegram):
        """This executes if the agent receives a message from the message dispatcher"""
        return False
