import unittest

import datetime

from HorizonCore.Framework.EventScheduler import EventScheduler
from HorizonCore.__specs__.TestHelpers.TestFactory import TestFactory


class EventSchedulerSpecifications(unittest.TestCase):

    ScheduleAsJsonString = '[{"Name": "TestEvent1", "StateClassName": "StateStartWakingUp", "StartTime": "07:00", "EndTime": "08:00"},{"Name": "TestEvent2", "StateClassName": "TimeForMorningGreeting", "StartTime": "08:00", "EndTime": "09:30"}]'

    def test_SpecifyThatAnEmptyScheduleCanBeConstructed(self):
        schedule = EventScheduler()

        self.assertEqual(schedule.NumberOfEvents(), 0)

    def test_SpecifyThatAnEventCanBeAddedToTheSchedule(self):
        schedule = TestFactory.CreateTestSchedule()

        self.assertEqual(schedule.NumberOfEvents(), 2)

    def test_SpecifyThatAnEventCanBeRetrievedFromTheScheduleByIndex(self):
        schedule = TestFactory.CreateTestSchedule()

        e = schedule.GetEventByIndex(0)

        self.assertEqual(e.Name, 'TestEvent1')

    def test_SpecifyThatAnEventCanBeRetrievedFromTheScheduleByName(self):
        schedule = TestFactory.CreateTestSchedule()

        e = schedule.GetEvent('TestEvent1')

        self.assertEqual(e.Name, 'TestEvent1')

    def test_SpecifyThatAnExceptionIsRaisedWhenTryingToRetrieveAnNonExistingEventByName(self):
        schedule = TestFactory.CreateTestSchedule()

        self.assertRaises(ValueError, schedule.GetEvent, 'TestEvent3')

    def test_SpecifyThatScheduleCanBeSavedToAJsonString(self):
        schedule = TestFactory.CreateTestSchedule()

        scheduleAsJson = schedule.ToJson()

        self.assertEqual(scheduleAsJson, self.ScheduleAsJsonString)

    def test_SpecifyThatAScheduleCanBeConstructedFromAJsonString(self):
        schedule = EventScheduler.FromJson(self.ScheduleAsJsonString)

        self.assertEqual(schedule.NumberOfEvents(), 2)
        self.assertEqual(schedule.GetEventByIndex(0).Name, 'TestEvent1')
        self.assertEqual(schedule.GetEventByIndex(1).Name, 'TestEvent2')

    def test_SpecifyThatEventsListCanBeAccessed(self):
        schedule = TestFactory.CreateTestSchedule()

        events = schedule.GetEvents()

        self.assertEqual(2, len(events))

    def test_SpecifyThatTheScheduleCanBeClearedOfAllEvents(self):
        schedule = TestFactory.CreateTestSchedule()

        schedule.Clear()

        self.assertEqual(0, schedule.NumberOfEvents())

    def test_SpecifyThatTheScheduleCanBeRepopulatedFromAJsonString(self):
        event1 = TestFactory.CreateTestEvent1()
        schedule = EventScheduler()
        schedule.AddEvent(event1)

        self.assertEqual(1, schedule.NumberOfEvents())

        schedule.PopulateFromJson(self.ScheduleAsJsonString)

        self.assertEqual(2, schedule.NumberOfEvents())

    def test_SpecifyThatTheScheduleCanDetermineWhetherTheLocalTimeIsWithAnEventPeriod(self):
        schedule = TestFactory.CreateTestSchedule()

        self.assertFalse(schedule.IsLocalTimeWithinScheduledEvent('TestEvent1', datetime.time(6, 30)))
        self.assertTrue(schedule.IsLocalTimeWithinScheduledEvent('TestEvent1', datetime.time(7, 30)))
