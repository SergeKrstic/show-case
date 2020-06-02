import unittest

import datetime

from HorizonCore.Framework.Telegram import Telegram


class TelegramSpecifications(unittest.TestCase):

    dispatchTime = datetime.datetime(2016, 11, 8, 14, 00, 12, 18299)

    def test_SpecifyThatTelegramCanBeConstructed(self):
        # arrange
        dispatchTime = self.dispatchTime
        senderId = 1
        receiverId = 2
        message = "Hello"
        extraInfo = None

        # act
        telegram = Telegram(dispatchTime, senderId, receiverId, message, extraInfo)

        # assert
        self.assertEqual(telegram.DispatchTime, dispatchTime, "DispatchTime")
        self.assertEqual(telegram.SenderId, senderId, "SenderId")
        self.assertEqual(telegram.ReceiverId, receiverId, "ReceiverId")
        self.assertEqual(telegram.Message, message, "Message")
        self.assertEqual(telegram.ExtraInfo, extraInfo, "ExtraInfo")

    def test_SpecifyThatStringDescriptionCanBeRetrieved(self):
        # arrange
        telegram = Telegram(dispatchTime=self.dispatchTime, senderId=1, receiverId=2, message="Hello", extraInfo=None)

        # act
        stringDescription = str(telegram)

        # assert
        self.assertEqual(stringDescription, "Time: 2016-11-08 14:00:12.018299  Sender: 1   Receiver: 2   Msg: Hello")

    def test_SpecifyThatTelegramsCanBeCompared(self):
        # arrange
        t1 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5), senderId=1, receiverId=2, message="Hello", extraInfo=None)
        t2 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5), senderId=1, receiverId=2, message="Hello", extraInfo=None)
        t3 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5.1), senderId=1, receiverId=2, message="Hello", extraInfo=None)
        t4 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5.5), senderId=1, receiverId=2, message="Hello", extraInfo=None)

        t5 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5), senderId=-1, receiverId=2, message="Hello", extraInfo=None)
        t6 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5), senderId=1, receiverId=-1, message="Hello", extraInfo=None)
        t7 = Telegram(dispatchTime=self.GetDelayedDispatchTime(5), senderId=1, receiverId=2, message="GoodBye", extraInfo=None)

        # assert
        self.assertEqual(t1 == t2, True, "t1 == t2")
        self.assertEqual(t1 == t3, True, "t1 == t3")
        self.assertEqual(t1 == t4, False, "t1 == t4")

        self.assertEqual(t1 == t5, False, "t1 == t5")
        self.assertEqual(t1 == t6, False, "t1 == t6")
        self.assertEqual(t1 == t7, False, "t1 == t7")

        self.assertEqual(t1 != t7, True, "t1 != t7")

    def test_SpecifyThatATelegramCanReturnAHashValue(self):
        # arrange
        telegram = Telegram(dispatchTime=self.dispatchTime, senderId=1, receiverId=2, message="Hello", extraInfo=None)

        # act
        hashValue = hash(telegram)

        # assert
        self.assertEqual(hashValue, 1475446365873459918)

    def GetDelayedDispatchTime(self, delay):
        return self.dispatchTime + datetime.timedelta(seconds=delay)
