class Assert:
    def SetDateTime(self, hour, minute):
        self.datetime = self.datetime.replace(hour=hour, minute=minute)
        self.datetime = self.datetime - datetime.timedelta(hours=self.testUser['TimeZoneOffset'])

    def AssertTimePeriod(self, timeCheckingFunction, startTime, endTime):
        self.SetDateTime(startTime.hour, startTime.minute - 1)
        self.assertEqual(timeCheckingFunction(), False)

        self.SetDateTime(startTime.hour, startTime.minute)
        self.assertEqual(timeCheckingFunction(), True)

        self.SetDateTime(startTime.hour, startTime.minute + 1)
        self.assertEqual(timeCheckingFunction(), True)

        self.SetDateTime(endTime.hour, endTime.minute - 1)
        self.assertEqual(timeCheckingFunction(), True)

        self.SetDateTime(endTime.hour, endTime.minute)
        self.assertEqual(timeCheckingFunction(), False)