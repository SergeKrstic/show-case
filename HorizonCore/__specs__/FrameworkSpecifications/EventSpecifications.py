import unittest

import datetime

from HorizonCore.Framework.Event import Event

eventAsJson = {
            'Name': 'TimeToStartWakingUp',
            'StateClassName': 'StateStartWakingUp',
            'StartTime': '07:00',
            'EndTime': '08:00',
        }


class EventSpecifications(unittest.TestCase):

    def test_SpecifyThatAnEventCanBeConstructed(self):
        event = Event(
            name='TimeToStartWakingUp',
            stateClassName='StateStartWakingUp',
            startTime=datetime.time(7, 0),
            endTime=datetime.time(8, 0))

        self.assertEqual(event.Name, 'TimeToStartWakingUp')
        self.assertEqual(event.StateClassName, 'StateStartWakingUp')
        self.assertEqual(event.StartTime, datetime.time(7, 0))
        self.assertEqual(event.EndTime, datetime.time(8, 0))

    def test_SpecifyThatAnEventCanBeConstructedFromAJsonObject(self):
        event = Event.FromDict(eventAsJson)

        self.assertEqual(event.Name, 'TimeToStartWakingUp')
        self.assertEqual(event.StateClassName, 'StateStartWakingUp')
        self.assertEqual(event.StartTime, datetime.time(7, 0))
        self.assertEqual(event.EndTime, datetime.time(8, 0))

    def test_SpecifyThatAnEventCanBeSavedToJsonString(self):
        event = Event.FromDict(eventAsJson)

        eventSavedAsJsonString = event.ToJson()

        self.assertEqual(eventSavedAsJsonString, '{"Name": "TimeToStartWakingUp", "StateClassName": "StateStartWakingUp", "StartTime": "07:00", "EndTime": "08:00"}')
