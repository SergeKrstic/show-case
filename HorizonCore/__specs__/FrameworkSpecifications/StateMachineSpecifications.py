import unittest

import mock

from HorizonCore.Framework.State import State
from HorizonCore.Framework.StateMachine import StateMachine
from HorizonCore.Framework.BaseEntity import BaseEntity


class StateMachineSpecifications(unittest.TestCase):

    EntityId = 0

    def tearDown(self):
        BaseEntity.ResetNextValidId()

    def test_SpecifyThatAStateMachineCanBeConstructed(self):
        # arrange
        entity = BaseEntity(self.EntityId)
        stateMachine = StateMachine(entity)

        # assert
        self.assertEqual(stateMachine.Owner, entity)
        self.assertEqual(stateMachine.CurrentState, None)
        self.assertEqual(stateMachine.PreviousState, None)
        self.assertEqual(stateMachine.GlobalState, None)

    def test_SpecifyThatStateMachineRaisesAnExceptionIsOwnerIsNotOfTypeBaseEntity(self):
        self.assertRaises(ValueError, StateMachine, None)

    def test_SpecifyThatTheHelperMethodRaisesAnExceptionIfStateIsNone(self):
        # arrange
        NullState = None

        # assert
        self.assertRaises(ValueError, StateMachine.RaiseExceptionIfStateIsNone, NullState)

    def test_SpecifyStatePropertiesRaiseExceptionsIfSetToInvalidType(self):
        # arrange
        stateMachine = self.CreateStateMachine()
        invalidType = 'Invalid Type'

        # assert
        self.assertRaises(ValueError, setattr, stateMachine, 'CurrentState', invalidType)
        self.assertRaises(ValueError, setattr, stateMachine, 'PreviousState', invalidType)
        self.assertRaises(ValueError, setattr, stateMachine, 'GlobalState', invalidType)

    def test_SpecifyThatStatePropertySettersCanBeSetToAStateObjectOrNone(self):
        # arrange
        stateMachine = self.CreateStateMachine()
        someState = State()

        # act
        stateMachine.CurrentState = None
        stateMachine.PreviousState = None
        stateMachine.GlobalState = None

        # assert
        self.assertIsNone(stateMachine.CurrentState)
        self.assertIsNone(stateMachine.PreviousState)
        self.assertIsNone(stateMachine.GlobalState)

        # act
        stateMachine.CurrentState = someState
        stateMachine.PreviousState = someState
        stateMachine.GlobalState = someState

        # assert
        self.assertTrue(isinstance(stateMachine.CurrentState, State))
        self.assertTrue(isinstance(stateMachine.PreviousState, State))
        self.assertTrue(isinstance(stateMachine.GlobalState, State))

    def test_SpecifyThatStateMachineCanPerformAnUpdate(self):
        ExpectedStateProcess = [
            'Executing GlobalState...',
            'Executing OffState...',
        ]

        # arrange
        entity = self.CreateEntityWithStateMachine()

        # act
        entity.Update()

        # assert
        self.assertEqual(entity.StateMachine.History, ExpectedStateProcess)

    def test_SpecifyThatStateMachineCanPerformAnUpdateWithEmptyStates(self):
        ExpectedStateProcess = []

        # arrange
        entity = self.CreateEntityWithStateMachine()
        entity.StateMachine.CurrentState = None
        entity.StateMachine.GlobalState = None

        # act
        entity.Update()

        # assert
        self.assertEqual(entity.StateMachine.History, ExpectedStateProcess)

    def test_SpecifyThatStateMachineChangeState(self):
        ExpectedStateProcess = [
            'Executing GlobalState...',
            'Executing OffState...',
            'Exiting OffState...',
            'Entering OnState...',
        ]

        # arrange
        entity = self.CreateEntityWithStateMachine()

        # act
        entity.Update()
        entity.StateMachine.ChangeState(OnState())

        # assert
        self.assertEqual(entity.StateMachine.History, ExpectedStateProcess)

    def test_SpecifyThatAnExceptionIsRaisedWhenChangingToANoneState(self):
        # arrange
        entity = self.CreateEntityWithStateMachine()

        # assert
        self.assertRaises(ValueError, entity.StateMachine.ChangeState, None)

    def test_SpecifyThatAnExceptionIsRaisedWhenChangingFromANoneState(self):
        # arrange
        entity = self.CreateEntityWithStateMachine()
        entity.StateMachine.CurrentState = None

        # assert
        self.assertRaises(ValueError, entity.StateMachine.ChangeState, OnState())

    def test_SpecifyThatStateMachineRevertToPreviousState(self):
        ExpectedStateProcess = [
            'Executing GlobalState...',
            'Executing OffState...',
            'Exiting OffState...',
            'Entering OnState...',
            'Exiting OnState...',
            'Entering OffState...',
        ]

        # arrange
        entity = self.CreateEntityWithStateMachine()

        # act
        entity.Update()
        entity.StateMachine.ChangeState(OnState())
        entity.StateMachine.RevertToPreviousState()

        # assert
        self.assertEqual(entity.StateMachine.History, ExpectedStateProcess)

    def test_SpecifyThatTheCurrentStateCanBeQueried(self):
        # arrange
        entityWithStateMachine = self.CreateEntityWithStateMachine()

        # assert
        self.assertTrue(entityWithStateMachine.StateMachine.IsInState(OffState()))

    def test_SpecifyThatATelegramCanBeHandledFromTheCurrentState(self):
        # arrange
        entity = self.CreateEntityWithStateMachine()
        entity.StateMachine.GlobalState = None

        OffState.OnTelegram = mock.Mock()
        OffState.OnTelegram.return_value = True

        # act & assert
        self.assertTrue(entity.HandleTelegram('test message'))
        OffState.OnTelegram.assert_called_with(entity, 'test message')

    def test_SpecifyThatATelegramCanBeHandledFromTheGlobalState(self):
        # arrange
        entity = self.CreateEntityWithStateMachine()
        entity.StateMachine.CurrentState = None

        GlobalState.OnTelegram = mock.Mock()
        GlobalState.OnTelegram.return_value = True

        # act & assert
        self.assertTrue(entity.HandleTelegram('test message'))
        GlobalState.OnTelegram.assert_called_with(entity, 'test message')

    def test_SpecifyThatATelegramCanBeHandledWithNoStatesActive(self):
        # arrange
        entity = self.CreateEntityWithStateMachine()
        entity.StateMachine.CurrentState = None
        entity.StateMachine.GlobalState = None

        # act & assert
        self.assertFalse(entity.HandleTelegram('test message'))

    # Helper methods
    # --------------------------------------------------------------------------------------------------

    def CreateStateMachine(self):
        BaseEntity.ResetNextValidId()
        entity = BaseEntity(self.EntityId)
        stateMachine = StateMachine(entity)

        return stateMachine

    def CreateEntityWithStateMachine(self):
        return TestEntity(self.EntityId)


class TestEntity(BaseEntity):

    def __init__(self, entityId):
        super().__init__(entityId)

        self._stateMachine = StateMachine(self)
        self._stateMachine.CurrentState = OffState()
        self._stateMachine.GlobalState = GlobalState()
        self._stateMachine._historyEnabled = True

    @property
    def StateMachine(self):
        return self._stateMachine

    def Update(self):
        self.StateMachine.Update()

    def HandleTelegram(self, telegram):
        return self.StateMachine.HandleTelegram(telegram)


class OnState(State):
    def Enter(self, entity):
        pass

    def Execute(self, entity):
        pass

    def Exit(self, entity):
        pass

    def OnTelegram(self, entity, telegram):
        return True


class OffState(State):
    def Enter(self, entity):
        pass

    def Execute(self, entity):
        pass

    def Exit(self, entity):
        pass

    def OnTelegram(self, entity, telegram):
        return True


class GlobalState(State):
    def Enter(self, entity):
        pass

    def Execute(self, entity):
        pass

    def Exit(self, entity):
        pass

    def OnTelegram(self, entity, telegram):
        return True
