import unittest

from HorizonCore.Framework.State import State
from HorizonCore.Framework.BaseEntity import BaseEntity


class StateSpecifications(unittest.TestCase):

    EntityId = 0

    def tearDown(self):
        BaseEntity.ResetNextValidId()

    def test_SpecifyThatExecuteThrowsNotImplementedError(self):
        # arrange
        entity = BaseEntity(self.EntityId)
        state = State()

        # assert
        self.assertRaises(NotImplementedError, state.Execute, entity)

    def test_SpecifyThatEnterDoesNotThrowANotImplementedError(self):
        # arrange
        entity = BaseEntity(self.EntityId)
        state = State()

        # assert
        try:
            state.Enter(entity)
        except:
            self.fail('Enter() should not throw an exception')

    def test_SpecifyThatExitDoesNotThrowANotImplementedError(self):
        # arrange
        entity = BaseEntity(self.EntityId)
        state = State()

        # assert
        try:
            state.Exit(entity)
        except:
            self.fail('Exit() should not throw an exception')

    def test_SpecifyThatOnTelegramReturnsFalse(self):
        # arrange
        entity = BaseEntity(self.EntityId)
        state = State()

        # assert
        self.assertFalse(state.OnTelegram(entity, None))
