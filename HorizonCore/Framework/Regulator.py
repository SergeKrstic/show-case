import datetime
import random


def isEqual(value1, value2):
    EPSILON = 0.25
    return abs(value1 - value2) < EPSILON


class Regulator:
    """
    Use this class to regulate code flow (for an update function say)
    Instantiate the class with the frequency you would like your code
    section to flow (like 10 times per second) and then only allow
    the program flow to continue if IsReady() returns true
    """

    def __init__(self, numberOfSecondsBetweenUpdates, updatePeriodVariatorInSeconds=10):

        # The number of milliseconds the update period can vary per required
        # update-step. This is here to make sure any multiple clients of this class
        # have their updates spread evenly
        self._updatePeriodVariatorInSeconds = updatePeriodVariatorInSeconds

        # The next time the regulator allows code flow
        randomOffset = datetime.timedelta(seconds=random.randint(0, self._updatePeriodVariatorInSeconds))
        # randomOffset = datetime.timedelta(seconds=0)
        self._nextUpdateTime = datetime.datetime.utcnow() + randomOffset

        # The time period between updates
        self._updatePeriodInSeconds = 0

        if numberOfSecondsBetweenUpdates > 0:
            self._updatePeriodInSeconds = numberOfSecondsBetweenUpdates

        elif isEqual(0.0, numberOfSecondsBetweenUpdates):
            self._updatePeriodInSeconds = 0.0

        elif numberOfSecondsBetweenUpdates < 0:
            self._updatePeriodInSeconds = -1

    def IsReady(self):
        """
        :return: true if the current time exceeds _nextUpdateTime
        """
        # If a regulator is instantiated with a zero freq then it goes into
        # stealth mode (doesn't regulate)
        if isEqual(0.0, self._updatePeriodInSeconds):
            return True

        # If the regulator is instantiated with a negative freq then it will
        # never allow the code to flow
        if self._updatePeriodInSeconds < 0:
            return False

        currentTime = datetime.datetime.utcnow()

        if currentTime >= self._nextUpdateTime:
            randomOffsetInSeconds = random.randint(-self._updatePeriodVariatorInSeconds, self._updatePeriodVariatorInSeconds)
            self._nextUpdateTime = currentTime + datetime.timedelta(seconds=self._updatePeriodInSeconds + randomOffsetInSeconds)
            return True

        return False
