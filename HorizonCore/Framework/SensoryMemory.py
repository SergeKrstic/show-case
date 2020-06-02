import datetime


# Todo: see page 319 of "Programming Game AI by Example"
class MemoryRecord:

    def __init__(self, timeLastSensed=None, timeBecameVisible=None, timeLastVisible=None, lastSensedPosition=None):
        # Records the time the event/object was last sensed (seen or heard). This
        # is used to determine if a bot can 'remember' this record or not.
        # (if CurrentTime() - TimeLastSensed is greater than the bot's
        # memory span, the data in this record is made unavailable to clients)
        self._timeLastSensed = timeLastSensed

        # It can be useful to know how long an event/object has been visible. This
        # variable is tagged with the current time whenever an opponent first event/object
        # visible. It's then a simple matter to calculate how long the event/object has
        # been in view (CurrentTime - TimeBecameVisible)
        self._timeBecameVisible = timeBecameVisible

        # It can also be useful to know the last time an event/object was seen
        self._timeLastVisible = timeLastVisible

        # A vector marking the position where the event/object was last sensed. This can
        # be used to help find the event/object when needed next
        self._lastSensedPosition = lastSensedPosition

    @property
    def TimeLastSensed(self):
        return self._timeLastSensed

    @TimeLastSensed.setter
    def TimeLastSensed(self, value):
        self._timeLastSensed = value

    @property
    def TimeBecameVisible(self):
        return self._timeBecameVisible

    @TimeBecameVisible.setter
    def TimeBecameVisible(self, value):
        self._timeBecameVisible = value

    @property
    def TimeLastVisible(self):
        return self._timeLastVisible

    @TimeLastVisible.setter
    def TimeLastVisible(self, value):
        self._timeLastVisible = value

    @property
    def LastSensedPosition(self):
        return self._lastSensedPosition

    @LastSensedPosition.setter
    def LastSensedPosition(self, value):
        self._lastSensedPosition = value


class SensoryMemory:

    def __init__(self, owner, memorySpan):
        # the owner of this instance
        self._owner = owner

        # A bot has a memory span equivalent to this value. When a bot requests a list
        # of all recently sensed event/object this value is used to determine if the
        # bot is able to remember an event/object or not.
        self._memorySpan = memorySpan

        # This container is used to simulate memory of sensory events. A MemoryRecord
        # is created for each notable event/object in the environment. Each record is
        # updated whenever the event/object is re-encountered. (when it is seen or heard)
        self._memoryMap = {}

    @property
    def Owner(self):
        return self._owner

    @property
    def MemorySpan(self):
        return self._memorySpan

    def Update(self, eventName):
        """
        This method is used to update the memory map whenever an event is re-encountered
        :param eventName:
        """
        # If the event is already part of the memory then update its data, else
        # create a new memory record and add it to the memory
        self._makeNewRecordIfNotAlreadyPresent(eventName)

        memoryRecord = self._memoryMap[eventName]

        # Record the time it was sensed
        currentDateTime = datetime.datetime.utcnow()
        memoryRecord.TimeLastSensed = currentDateTime
        memoryRecord.TimeBecameVisible = currentDateTime
        memoryRecord.TimeLastVisible = currentDateTime

        # Todo: implement user location
        memoryRecord.LastSensedPosition = None  # self.Owner.User.GetCurrentPosition()

    def RemoveEventFromMemory(self, eventName):
        """
        This removes a bot's record from memory
        :param eventName:
        """
        if eventName in self._memoryMap:
            del self._memoryMap[eventName]

    def IsEventLocationWithinRange(self, eventName):
        # Todo: need to retrieve user location and calculate distance to eventLocation
        raise NotImplementedError

    def GetLastRecordedPositionOfEventLocation(self, eventName):
        return self._getMemoryRecord(eventName).LastSensedPosition

    def GetTimeEventLocationHasBeenVisible(self, eventName):
        return self._getMemoryRecord(eventName).TimeBecameVisible

    def GetTimeSinceEventWasLastSensed(self, eventName):
        return self._getMemoryRecord(eventName).TimeLastSensed

    def GetTimeEventLocationHasBeenOutOfView(self, eventName):
        memoryRecord = self._getMemoryRecord(eventName)
        currentDateTime = datetime.datetime.utcnow()
        return currentDateTime - memoryRecord.TimeLastVisible

    def GetListOfRecentlySensedEvents(self):
        """
        This method returns a list of all the opponents that have had their
        records updated within the last m_dMemorySpan seconds.
        :return:
        """
        recentMemory = []
        currentDateTime = datetime.datetime.utcnow()

        for _, memoryRecord in self._memoryMap.items():
            if currentDateTime < memoryRecord.TimeLastSensed + self._memorySpan:
                recentMemory.append(memoryRecord)

        return recentMemory

    def _makeNewRecordIfNotAlreadyPresent(self, eventName):
        """
        This method checks to see if there is an existing record for 'eventName'. If
        not a new MemoryRecord record is made and added to the memory map. (called
        by UpdateWithSoundSource & UpdateVision)
        :param eventName:
        """
        if eventName not in self._memoryMap:
            self._memoryMap[eventName] = MemoryRecord()

    def _getMemoryRecord(self, eventName):
        if eventName in self._memoryMap:
            return self._memoryMap[eventName]

        raise Exception("Attempting to get position of unrecorded event")
