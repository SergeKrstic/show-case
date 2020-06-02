import time


class Timer:
    def __init__(self):
        self.StartTime = 0
        self.StopTime = 0

    @property
    def ElapsedTime(self):
        return self.StopTime - self.StartTime

    def Reset(self):
        self.StartTime = 0
        self.StopTime = 0

    def Start(self):
        self.StartTime = time.time()

    def Stop(self):
        self.StopTime = time.time()
        self.PrintRunTime()

        return self.ElapsedTime

    def PrintRunTime(self):
        if self.ElapsedTime < 60:
            print('\nRun time: ' + str(int(self.ElapsedTime)) + ' seconds\n')
        else:
            minutes = int(self.ElapsedTime / 60)
            seconds = int(self.ElapsedTime - (minutes * 60))
            print('Run duration: ' + str(minutes) + ' minutes, ' + str(seconds) + ' seconds\n')
