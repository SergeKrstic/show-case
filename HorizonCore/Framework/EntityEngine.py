"""
    Mission:

        The purpose of EntityEngine is to provide a main loop where all the coaches and services can execute
        and communicate with each other and, of course, with the user via DialogFlow database transactions

    Objectives:

        [ ] Consider implement a Django style url router
        [ ] Create a script to rename DialogFlow action names
        [x] Break up and move dictionary items to appropriate coach/service modules
        [x] Consider moving this class into the Framework folder
"""

import _thread

from HorizonCore.Framework.BaseEngine import BaseEngine
from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.EntityManager import EntityManager
from HorizonCore.Framework.TelegramDispatcher import TelegramDispatcher
from HorizonCore.ToolBox.Utils import Utils

# Constants
DIALOG_FLOW_TRANSACTIONS_URL = 'users/Rwc20oNDgKQ32bwVOOKbPYzndrG3/third-parties/IOLImskUszfWPLz1EiOo/transactions'


class EntityEngine(BaseEngine):

    def __init__(self, firestoreClient, entities):

        self._firestoreClient = firestoreClient
        self._entities = entities
        self._actionMap = {}

        BaseEntity.ResetNextValidId()
        TelegramDispatcher().Clear()

        for entity in self._entities:
            EntityManager.RegisterEntity(entity)
            self._actionMap.update(entity.ActionMap)

        transactionsRef = self._firestoreClient \
            .collection(DIALOG_FLOW_TRANSACTIONS_URL) \
            .where('status', '==', 'UNPROCESSED')

        self._transactionListener = transactionsRef.on_snapshot(self._processRequests)

    def FireEngineCylinders(self):
        self._processEntities()
        self._processDelayedTelegrams()

    # Helper methods
    # ==================================================================================================================

    def _processEntities(self):
        for entity in self._entities:
            entity.Update()

    @staticmethod
    def _processDelayedTelegrams():
        TelegramDispatcher().DispatchDelayedTelegrams()

    def _processRequests(self, transactions, changes, readTime):
        for transaction in transactions:
            try:
                response = self._processRequest(transaction)
                transaction.reference.update({'status': 'PROCESSED', 'response': response})
            except Exception as error:
                self._handleTransactionError(transaction, error)

    def _handleTransactionError(self, transaction, error):
        print(f'<<EntityEngine._processRequests>> An error occurred while processing the DialogFlow request :: {error}')
        transaction.reference.update({'status': 'ERROR'})

    def _processRequest(self, transaction):
        transactionData = transaction.to_dict()
        actionName = transactionData['body']['queryResult'].get('action')
        actionData = self._actionMap.get(actionName)

        if actionData is not None:
            # Todo: figure out if this approach is robust (draw some flow/timing diagrams)
            _thread.start_new_thread(self._executeRequest, (actionData, transaction))
        else:
            Utils.NotifyAdminOfSystemEvent(f"Sorry something went wrong. I don't recognise this action: '{actionName}'")

        return self._createEmptyResponse()

    def _executeRequest(self, actionData, transaction):
        try:
            transactionData = transaction.to_dict()
            requestData = transactionData['body']
            actionFunction = actionData['FunctionToExecute']
            actionFunction(requestData)
        except Exception as error:
            self._handleTransactionError(transaction, error)

    @staticmethod
    def _createEmptyResponse():
        return {"speech": "", "displayText": "", "source": "https://sunny-ai.com"}


exampleData = {
    'id': '81317bba-f555-492f-830f-3df087636ada',
    'lang': 'en',
    'originalRequest': {
        'data': {
            'message': {
                'mid': 'mid.$cAAZA6lZU1XRhrDqdW1bevVeS2wFE',
                'seq': 21513,
                'text': 'prepare my grocery list'
            },
            'recipient': {
                'id': '1760225697577826'
            },
            'sender': {
                'id': '1339438022780029'
            },
            'timestamp': 1492416550235.0
        },
        'source': 'facebook'
    },
    'result': {
        'action': 'PrepareGroceryShoppingList',
        'actionIncomplete': False,
        'contexts': [
            {
                'lifespan': 2,
                'name': 'generic',
                'parameters': {
                    'facebook_sender_id': '1339438022780029'
                }
            }
        ],
        'fulfillment': {
            'messages': [
                {
                    'speech': '',
                    'type': 0
                }
            ],
            'speech': ''
        },
        'metadata': {
            'intentId': '6d858714-44cf-4b6b-beba-d948ce77d22a',
            'intentName': 'Trello - grocery list - prepare',
            'webhookForSlotFillingUsed': 'false',
            'webhookUsed': 'true'
        },
        'parameters': {},
        'resolvedQuery': 'prepare my grocery list',
        'score': 1.0,
        'source': 'agent',
        'speech': ''
    },
    'sessionId': '77bcadfe-fbea-4065-8a71-cb63539e37ad',
    'status': {
        'code': 200,
        'errorType': 'success'
    },
    'timestamp': '2017-04-17T08:09:10.459Z'
}
