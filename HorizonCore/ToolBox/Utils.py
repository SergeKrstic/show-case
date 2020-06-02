import random
import time
import datetime
from pprint import pprint
from decouple import config

import HorizonCore.Configuration as Config
from HorizonCore.AuthenticationDetails import AuthenticationDetails
from ThirdPartyWrappers.MessengerApi.MessengerApi import MessengerApi


class Utils:

    EPSILON = 0.000001
    DEBUG_PRINT_ENABLED = config('DEBUG_PRINT_ENABLED', default=False, cast=bool)

    @classmethod
    def GetLocalTime(cls):
        return time.asctime(time.localtime(time.time()))

    @staticmethod
    def SleepFor(amountOfTimeToSleep, units):
        timeInSeconds = Utils.ConvertTimeLengthToSeconds(amountOfTimeToSleep, units)
        time.sleep(timeInSeconds)

    @staticmethod
    def ConvertTimeLengthToSeconds(lengthOfTime, units):
        if units in ['second', 'seconds']:
            timeInSeconds = lengthOfTime
        elif units in ['minute', 'minutes']:
            timeInSeconds = lengthOfTime * 60
        elif units in ['hour', 'hours']:
            timeInSeconds = lengthOfTime * 60 * 60
        elif units in ['day', 'days']:
            timeInSeconds = lengthOfTime * 60 * 60 * 24
        else:
            raise Exception("Time unit not recognised")

        return timeInSeconds

    @staticmethod
    def GetShuffledIndices(numberOfIndices):
        indices = list(range(numberOfIndices))
        random.shuffle(indices)
        return indices

    @staticmethod
    def IsTimeWithinSchedule(timeToCheck, onTime, offTime):
        if onTime > offTime:
            if timeToCheck >= onTime or timeToCheck < offTime:
                return True

        elif onTime < offTime:
            if onTime <= timeToCheck < offTime:
                return True

        elif onTime == offTime:
            return False

        return False

    @staticmethod
    def AdjustTime(timeToAdjust, hoursOffset=0, minutesOffset=0, secondsOffset=0):
        return (datetime.datetime.combine(datetime.date(1, 1, 1), timeToAdjust) +
                datetime.timedelta(hours=hoursOffset, minutes=minutesOffset, seconds=secondsOffset)).time()

    @staticmethod
    def TimeFromString(timeAsString):
        return datetime.datetime.strptime(timeAsString, '%H:%M').time()

    @staticmethod
    def TimeToString(timeObject):
        return datetime.datetime.combine(datetime.date(1, 1, 1), timeObject).strftime('%H:%M')

    @staticmethod
    def DateFromString(dateAsString):
        return datetime.datetime.strptime(dateAsString, '%Y-%m-%d').date()

    @staticmethod
    def DateToString(dateObject):
        return dateObject.strftime('%Y-%m-%d')

    @staticmethod
    def DateTimeFromString(dateTimeAsString):
        return datetime.datetime.strptime(dateTimeAsString, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def DateTimeToString(dateTimeObject):
        return dateTimeObject.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def IsEqual(cls, value1, value2):
        return abs(value1 - value2) < cls.EPSILON

    @classmethod
    def DebugPrint(cls, message, withNewLine=True):
        if cls.DEBUG_PRINT_ENABLED:
            if isinstance(message, dict):
                pprint(message)
            else:
                if withNewLine:
                    print(message)
                else:
                    print(message, end = '')

    @staticmethod
    def NotifyAdminOfSystemEvent(errorMessage):
        messengerClient = MessengerApi(access_token=AuthenticationDetails.MessengerAccessTokenForSunny,
                                       api_version=AuthenticationDetails.MessengerApiVersion)
        messengerClient.Text.SendTextMessage(Config.AdminId, errorMessage)
        pprint(errorMessage)
