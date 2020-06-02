import datetime
import mock as Mock
import unittest

from enum import Enum

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.EntityManager import EntityManager
from HorizonCore.Framework.TelegramDispatcher import TelegramDispatcher


class Entity(Enum):
    EntityOne = 1
    EntityTwo = 2


class Message(Enum):
    MessageOne = "MessageOne"
    MessageTwo = "MessageTwo"


class TelegramDispatcherSpecifications(unittest.TestCase):

    def setUp(self):
        entityOne = EntityOne(1)
        entityTwo = EntityTwo(2)

        EntityManager.RegisterEntity(entityOne)
        EntityManager.RegisterEntity(entityTwo)

        self.datetime = datetime.datetime(2016, 11, 8, 14, 00, 12, 18299)

        class fakeDateTime(datetime.datetime):
            @classmethod
            def utcnow(cls):
                return self.datetime

        patcher = Mock.patch('datetime.datetime', fakeDateTime)
        self.addCleanup(patcher.stop)
        patcher.start()

    def tearDown(self):
        EntityManager.Reset()
        BaseEntity.ResetNextValidId()
        TelegramDispatcher().Clear()

    def test_SpecifyThatATelegramCanBeAddedToTheTelegramDispatcherQueue(self):
        delayInSeconds = 5
        ExpectedDispatchTime = self.datetime + datetime.timedelta(seconds=delayInSeconds)
        TelegramDispatcher().DispatchTelegram(delayInSeconds,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        self.assertEqual(TelegramDispatcher().PriorityQ.IsEmpty(), False)
        self.assertEqual(TelegramDispatcher().PriorityQ.Peek().DispatchTime, ExpectedDispatchTime)

    def test_SpecifyThatMultipleTelegramsCanBeAddedToTheTelegramDispatcherQueue(self):
        delayInSeconds1 = 35
        delayInSeconds2 = 15
        delayInSeconds3 = 5
        ExpectedDispatchTime1 = self.datetime + datetime.timedelta(seconds=delayInSeconds1)
        ExpectedDispatchTime2 = self.datetime + datetime.timedelta(seconds=delayInSeconds2)
        ExpectedDispatchTime3 = self.datetime + datetime.timedelta(seconds=delayInSeconds3)

        TelegramDispatcher().DispatchTelegram(delayInSeconds1,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        TelegramDispatcher().DispatchTelegram(delayInSeconds2,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        TelegramDispatcher().DispatchTelegram(delayInSeconds3,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        self.assertEqual(TelegramDispatcher().PriorityQ.IsEmpty(), False, 'a1')
        self.assertEqual(len(TelegramDispatcher().PriorityQ._items), 3, 'a2')
        self.assertEqual(TelegramDispatcher().PriorityQ.Peek().DispatchTime, ExpectedDispatchTime3, 'a3')
        self.assertEqual(TelegramDispatcher().PriorityQ._items[2].DispatchTime, ExpectedDispatchTime3, 'a4')
        self.assertEqual(TelegramDispatcher().PriorityQ._items[1].DispatchTime, ExpectedDispatchTime2, 'a5')
        self.assertEqual(TelegramDispatcher().PriorityQ._items[0].DispatchTime, ExpectedDispatchTime1, 'a6')

    def test_SpecifyThatDuplicateTelegramsCanNotBeAddedToTheTelegramDispatcherQueue(self):
        delayInSeconds1 = 35
        ExpectedDispatchTime1 = self.datetime + datetime.timedelta(seconds=delayInSeconds1)

        TelegramDispatcher().DispatchTelegram(delayInSeconds1,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        TelegramDispatcher().DispatchTelegram(delayInSeconds1,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        TelegramDispatcher().DispatchTelegram(delayInSeconds1 + 0.2,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        self.assertEqual(TelegramDispatcher().PriorityQ.IsEmpty(), False, 'a1')
        self.assertEqual(len(TelegramDispatcher().PriorityQ._items), 1, 'a2')
        self.assertEqual(TelegramDispatcher().PriorityQ.Peek().DispatchTime, ExpectedDispatchTime1, 'a3')
        self.assertEqual(TelegramDispatcher().PriorityQ._items[0].DispatchTime, ExpectedDispatchTime1, 'a4')

    def test_SpecifyThatATelegramCanBeDispatchedImmediately(self):
        # arrange
        entity = EntityManager.GetEntityFromID(Entity.EntityTwo.value)

        # assert
        self.assertEqual(entity.Outcome, None)

        # act
        TelegramDispatcher().DispatchTelegram(TelegramDispatcher.SEND_MSG_IMMEDIATELY,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        # assert
        self.assertEqual(entity.Outcome, "Telegram received")

    def test_SpecifyThatDelayTelegramsCanBeDispatched(self):
        # arrange
        delayInSeconds = 5
        entityOne = EntityManager.GetEntityFromID(Entity.EntityOne.value)
        entityTwo = EntityManager.GetEntityFromID(Entity.EntityTwo.value)

        TelegramDispatcher().DispatchTelegram(delayInSeconds,
                                              Entity.EntityOne.value,
                                              Entity.EntityOne.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)

        TelegramDispatcher().DispatchTelegram(delayInSeconds,
                                              Entity.EntityOne.value,
                                              Entity.EntityTwo.value,
                                              Message.MessageOne.value,
                                              TelegramDispatcher.NO_ADDITIONAL_INFO)
        # act
        TelegramDispatcher().DispatchDelayedTelegrams()

        # assert
        self.assertEqual(entityOne.Outcome, None, "a1")
        self.assertEqual(entityTwo.Outcome, None, "a2")

        # act
        self.datetime = self.datetime + datetime.timedelta(seconds=delayInSeconds+1)
        TelegramDispatcher().DispatchDelayedTelegrams()

        # assert
        self.assertEqual(entityOne.Outcome, "Telegram received", "a3")
        self.assertEqual(entityTwo.Outcome, "Telegram received", "a4")

    def test_SpecifyThatUnhandledMessagesAreLogged(self):
        # arrange
        delayInSeconds = 0
        TelegramDispatcher()._loggerEnabled = True
        extraInfo = "Ignore me..."

        # act
        TelegramDispatcher().DispatchTelegram(delayInSeconds,
                                              Entity.EntityOne,
                                              Entity.EntityTwo,
                                              Message.MessageOne,
                                              extraInfo)

        # assert
        self.assertEqual(TelegramDispatcher()._loggerHistory[0], "Telegram not handled")


class EntityOne(BaseEntity):
    Outcome = None

    def Update(self):
        pass

    def HandleTelegram(self, telegram):
        self.Outcome = "Telegram received"
        return True


class EntityTwo(BaseEntity):
    Outcome = None

    def Update(self):
        pass

    def HandleTelegram(self, telegram):
        if telegram.ExtraInfo is not None:
            if telegram.ExtraInfo == "Ignore me...":
                return False
        else:
            self.Outcome = "Telegram received"
            return True
