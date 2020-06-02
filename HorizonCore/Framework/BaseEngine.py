from HorizonCore.ToolBox.Utils import Utils


class BaseEngine:

    EngineCylinderDelayInSeconds = 10
    EngineRestartDelayInSeconds = 5

    def Run(self):
        while self.EngineIsRunning():
            try:
                self.FireEngineCylinders()
                Utils.SleepFor(self.EngineCylinderDelayInSeconds, 'seconds')
            except Exception as error:
                self.HandleEngineFailure(error)

    def EngineIsRunning(self):
        return True

    def FireEngineCylinders(self):
        raise NotImplementedError

    def HandleEngineFailure(self, error):
        Utils.NotifyAdminOfSystemEvent(f'Error message: {self.GetEngineName()} has crashed...')
        Utils.NotifyAdminOfSystemEvent(f'Error details: {error.args}')
        Utils.SleepFor(self.EngineRestartDelayInSeconds, 'seconds')

    def GetEngineName(self):
        return self.__class__.__name__
