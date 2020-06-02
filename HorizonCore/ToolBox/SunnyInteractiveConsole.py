from __future__ import print_function

import json
import apiai

from HorizonCore.ToolBox.TrelloPrinter import TrelloPrinter

CLIENT_ACCESS_TOKEN = '272369fa2cb8484cb7138d10b6f33f9d'
# CLIENT_ACCESS_TOKEN = '7062694ebfbd4df1a9c473da8f6dbbe3'


class InteractiveConsole:
    def __init__(self, bot):
        self.apiAi = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        self.displayResponseJson = False
        self.action = Action(bot)

    def Run(self):
        self.displayResponseJson = self._askQuestion(u"Display response json?")
        self.action.DisplayActionParameters = self._askQuestion(u"Display action parameters?")

        while True:
            userMessage = self._getUserMessageFromConsole()
            botResponse = self._getResponseFromBotInCloud(userMessage)

            self._displayBotResponseToConsole(botResponse)
            self._processAnyActionsFrom(botResponse)

    # Helper methods
    # ==================================================================================================================

    @staticmethod
    def _askQuestion(question):
        print(question + " [y/n]: ")
        user_input = input()
        if user_input == u"y":
            return True
        else:
            return False

    @staticmethod
    def _getUserMessageFromConsole():
        print(u"> ", end=u"")
        userMessage = input()
        if userMessage in [u"exit", u"quit"]:
            exit()
        return userMessage

    def _getResponseFromBotInCloud(self, userMessage):
        request = self.apiAi.text_request()
        request.query = userMessage
        response = request.getresponse().read()
        response = str(response, 'utf-8')
        response = json.loads(response)
        return response

    def _displayBotResponseToConsole(self, botResponse):
        if self.displayResponseJson:
            TrelloPrinter.PrintJsonObjectNicely(botResponse)
        print("< %s" % botResponse['result']['fulfillment']['speech'])

    def _processAnyActionsFrom(self, botResponse):
        self.action.Execute(botResponse)


class Action:
    def __init__(self, bot, displayActionParameters=True):
        self.bot = bot
        self.actions = bot.ActionsFactory
        self.displayActionParameters = displayActionParameters

    def Execute(self, botResponse):
        result = botResponse['result']
        actionName = result.get('action')
        actionComplete = not result.get('actionIncomplete', False)
        parameters = result.get('parameters')

        self._displayActionParameters(parameters)

        if actionComplete and self.actions.get(actionName):
            self.actions[actionName](self.bot, result)

    def _displayActionParameters(self, parameters):
        if parameters and self.displayActionParameters:
            index = 0
            count = len(parameters.items())
            parameterString = "  { "
            for key, value in parameters.items():
                value = value if value else "null"
                sep = separator(index, count)
                parameterString += key + ": " + value + sep
                index += 1
            print(parameterString + " }")


def separator(index, count):
    if count == 1 or index == count - 1:
        return ""
    else:
        return ", "


def isNotEmpty(s):
    return bool(s and s.strip())


class Sunny:
    def __init__(self):
        self._actionsFactory = ActionsFactory

    @property
    def ActionsFactory(self):
        return self._actionsFactory


# Actions (don't forget to add functions to dictionary)
# ======================================================================================================================

def PreformMessageAction():
    print(u"...Sending Message...")


ActionsFactory = {
        u"send_message": PreformMessageAction,
    }

if __name__ == '__main__':
    InteractiveConsole(Sunny()).Run()

