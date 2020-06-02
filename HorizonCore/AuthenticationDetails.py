from decouple import config


class AuthenticationDetails:

    TrelloApiKey = config('TRELLO_API_KEY')
    TrelloApiSecret = config('TRELLO_API_SECRET')

    TrelloResourceOwnerToken = config('TRELLO_RESOURCE_OWNER_TOKEN')
    TrelloResourceOwnerSecret = config('TRELLO_RESOURCE_OWNER_SECRET')

    DialogFlowClientAccessToken = config('DIALOG_FLOW_CLIENT_ACCESS_TOKEN')
    DialogFlowDeveloperAccessToken = config('DIALOG_FLOW_DEVELOPER_ACCESS_TOKEN')

    MessengerAccessTokenForSunny = config('MESSENGER_ACCESS_TOKEN_FOR_SUNNY')
    MessengerApiVersion = "3.2"
