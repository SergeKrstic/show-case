import json

from HorizonCore.Framework.Event import Event
from HorizonCore.ToolBox.Utils import Utils


class EventScheduler:

    def __init__(self):
        self._events = []

    def NumberOfEvents(self):
        return len(self._events)

    def Clear(self):
        self._events = []

    def AddEvent(self, event):
        self._events.append(event)

    def GetEventByIndex(self, value):
        return self._events[value]

    def GetEvent(self, name):
        for event in self._events:
            if event.Name == name:
                return event
        raise ValueError('Event not found in schedule. Invalid name {}'.format(name))

    def GetEvents(self):
        return self._events

    def IsLocalTimeWithinScheduledEvent(self, eventName, localTime):
        startTime = self.GetEvent(eventName).StartTime
        endTime = self.GetEvent(eventName).EndTime
        return Utils.IsTimeWithinSchedule(localTime, startTime, endTime)

    @staticmethod
    def FromJson(data):
        eventScheduler = EventScheduler()
        eventDataArray = json.loads(data)
        for eventData in eventDataArray:
            eventScheduler.AddEvent(Event.FromDict(eventData))

        return eventScheduler

    def PopulateFromJson(self, data):
        self.Clear()
        eventDataArray = json.loads(data)
        for eventData in eventDataArray:
            self.AddEvent(Event.FromDict(eventData))

    def ToJson(self):
        jsonString = "["
        for event in self._events:
            jsonString += event.ToJson() + ","
        return jsonString[:-1] + "]"
