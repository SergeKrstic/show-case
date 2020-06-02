import json

from HorizonCore.ToolBox.Utils import Utils


class Event:
    @staticmethod
    def FromDict(data):
        return Event(
            name=data['Name'],
            stateClassName=data['StateClassName'],
            startTime=Utils.TimeFromString(data['StartTime']),
            endTime=Utils.TimeFromString(data['EndTime']))

    def ToJson(self):
        return json.dumps({
            'Name': self.Name,
            'StateClassName': self.StateClassName,
            'StartTime': Utils.TimeToString(self.StartTime),
            'EndTime': Utils.TimeToString(self.EndTime),
        })

    def __init__(self, name, stateClassName, startTime, endTime):
        self.Name = name
        self.StateClassName = stateClassName
        self.StartTime = startTime
        self.EndTime = endTime
