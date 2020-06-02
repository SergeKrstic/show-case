class RequestDataTools:

    @staticmethod
    def GetParameter(requestData, parameterName):
        result = requestData.get("queryResult")
        parameters = result.get("parameters")
        parameterValue = parameters.get(parameterName)
        return parameterValue
