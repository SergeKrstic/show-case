from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.State import State


class StateMachine:
    def __init__(self, owner):
        self._setOwner(owner)
        self._currentState = None
        self._previousState = None
        self._globalState = None
        self._historyEnabled = False
        self._history = []

    # Properties
    # ==========================================================================

    @property
    def Owner(self):
        return self._owner

    def _setOwner(self, value):
        if not isinstance(value, BaseEntity):
            raise ValueError("StateMachine requires 'owner' to be of type BaseEntity")
        self._owner = value

    @property
    def CurrentState(self):
        return self._currentState

    @CurrentState.setter
    def CurrentState(self, value):
        self.RaiseExceptionIfStateValueIsInvalid(value)
        self._currentState = value

    @property
    def PreviousState(self):
        return self._previousState

    @PreviousState.setter
    def PreviousState(self, value):
        self.RaiseExceptionIfStateValueIsInvalid(value)
        self._previousState = value

    @property
    def GlobalState(self):
        return self._globalState

    @GlobalState.setter
    def GlobalState(self, value):
        self.RaiseExceptionIfStateValueIsInvalid(value)
        self._globalState = value

    @property
    def History(self):
        return self._history

    # Methods
    # ==========================================================================

    def Update(self):
        # If a global state exists, call its execute method, else do nothing
        if self.GlobalState is not None:
            self._recordHistory("Executing", self.GlobalState)
            self.GlobalState.Execute(self.Owner)

        # Same for the current state
        if self.CurrentState is not None:
            self._recordHistory("Executing", self.CurrentState)
            self.CurrentState.Execute(self.Owner)

    def ChangeState(self, newState):
        self.RaiseExceptionIfStateIsNone(newState)
        self.RaiseExceptionIfStateIsNone(self.CurrentState)

        # Keep a record of the previous state
        self.PreviousState = self.CurrentState

        # Call the exit method of the existing state
        self._recordHistory("Exiting", self.CurrentState)
        self.CurrentState.Exit(self.Owner)

        # Change state to the new state
        self.CurrentState = newState

        # Call the entry method of the new state
        self._recordHistory("Entering", self.CurrentState)
        self.CurrentState.Enter(self.Owner)

    def RevertToPreviousState(self):
        # Change state back to the previous state
        self.ChangeState(self.PreviousState)

    def IsInState(self, state):
        # Returns true if the current state's type is equal to the type of the
        # class passed as a parameter.
        return self.CurrentState == state

    def HandleTelegram(self, telegram):
        # First see if the current state is valid and that it can handle the message
        if self.CurrentState is not None and self.CurrentState.OnTelegram(self.Owner, telegram):
            return True

        # If not, then check if a global state has been implemented before sending the message to the global state
        if self.GlobalState is not None and self.GlobalState.OnTelegram(self.Owner, telegram):
            return True

        return False

    # Helper methods
    # ==========================================================================

    def _recordHistory(self, stateTransitionString, state):
        if self._historyEnabled:
            self.History.append(stateTransitionString + " " + str(state.__class__.__name__) + "...")

    @staticmethod
    def RaiseExceptionIfStateIsNone(state):
        if state is None:
            raise ValueError('State is None')

    @staticmethod
    def RaiseExceptionIfStateValueIsInvalid(value):
        if not(isinstance(value, State) or value is None):
            raise ValueError('Value must be either type State or None')


