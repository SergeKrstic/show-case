import datetime

from HorizonCore.Framework.EntityManager import EntityManager
from HorizonCore.Framework.Enums import Entity
from HorizonCore.Framework.PriorityQueue import PriorityQueue
from HorizonCore.Framework.Singleton import Singleton
from HorizonCore.Framework.Telegram import Telegram


class TelegramDispatcher(metaclass=Singleton):

    # to make code easier to read
    SEND_MSG_IMMEDIATELY = 0.0
    NO_ADDITIONAL_INFO = None

    # a set is used as the container for the delayed messages
    # because of the benefit of automatic sorting and avoidance
    # of duplicates. Messages are sorted by their dispatch time.
    PriorityQ = PriorityQueue()
    _loggerEnabled = False
    _loggerHistory = []

    def DispatchTelegram(self, delay, senderId, receiverId, message, extraInfo):
        """
        Send a message to another agent. Receiving agent is referenced by ID.
        :param delay: length of time (in seconds) to delay sending message
        :param senderId: ID of sender entity
        :param receiverId: ID of receiver entity
        :param message: Message enum to send
        :param extraInfo: object collecting extra message information
        """
        # Get references to the sender and receiver
        sender = EntityManager.GetEntityFromID(senderId)
        receiver = EntityManager.GetEntityFromID(receiverId)

        # Create the telegram
        telegram = Telegram(0, sender.Id, receiver.Id, message, extraInfo)

        # If there is no delay, route telegram immediately
        if delay <= 0:
            # Send the telegram to the recipient
            self._discharge(receiver, telegram)

            self._log(
                "\nInstant telegram dispatched at time: {} by {} for {}. Message is {}".format(
                    datetime.datetime.utcnow(),
                    Entity(sender.Id).name,
                    Entity(receiver.Id).name,
                    message))

        # else calculate the time when the telegram should be dispatched
        else:
            currentTime = datetime.datetime.utcnow()

            telegram.DispatchTime = currentTime + datetime.timedelta(seconds=delay)

            # and put it in the queue
            self.PriorityQ.Insert(telegram)

            self._log(
                "\nDelayed telegram from {} recorded at time {} for {}. Msg is {}".format(
                    Entity(sender.Id),
                    datetime.datetime.utcnow(),
                    Entity(receiver.Id),
                    telegram.Message))

    def DispatchDelayedTelegrams(self):
        """
        Send out any delayed messages. This method is called each time through
        the main game loop.
        """
        # Get current time
        currentTime = datetime.datetime.utcnow()

        # now peek at the queue to see if any telegrams need dispatching.
        # remove all telegrams from the front of the queue that have gone
        # past their sell by date
        while (not self.PriorityQ.IsEmpty() and
                (self.PriorityQ.Peek().DispatchTime < currentTime)):  # and
                # (self.PriorityQ.Peek().DispatchTime > 0)):

            # Get the telegram from the front of the queue
            telegram = self.PriorityQ.Pop()

            # Find the recipient
            receiver = EntityManager.GetEntityFromID(telegram.ReceiverId)

            # Send the telegram to the recipient
            self._discharge(receiver, telegram)

            self._log("\nQueued telegram ready for dispatch: Sent to {}. Msg is {}".format(
                Entity(receiver.Id), telegram.Message))

    def Clear(self):
        self.PriorityQ = PriorityQueue()

    # Helper methods
    # ==========================================================================

    def _discharge(self, receiver, telegram):
        """
        This method is utilized by DispatchMessage or DispatchDelayedTelegrams.
        It calls the message handling member function of the receiving
        entity, receiver, with the newly created telegram
        :param receiver: the receiver entity
        :param telegram: the telegram
        """
        handled = receiver.HandleTelegram(telegram)
        if not handled:
            self._log("Telegram not handled")

    def _log(self, eventMessage):
        if self._loggerEnabled:
            self._loggerHistory.append(eventMessage)
            print(eventMessage)
