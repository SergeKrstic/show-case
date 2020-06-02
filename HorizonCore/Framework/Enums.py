from enum import Enum

# Todo: move file to HorizonAgents as it does not relate to the general framework

class Entity(Enum):
    # User, Coach = range(0, 2)
    DefaultType = -1
    User = 0
    SleepCoach = 1
    MotivationalCoach = 2
    MoodTracker = 3
    GratitudeHelper = 4
    AdministrationService = 5
    AgileResultsService = 6
    HomeService = 7
    ShoppingService = 8
    WeatherService = 9


class Location(Enum):
    Home = 0
    Work = 1


class Message(Enum):
    DayTime = 0
    BedTime = 1


class Goal(Enum):
    DefaultType = -1
