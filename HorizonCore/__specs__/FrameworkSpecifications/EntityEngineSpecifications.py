# Note: Need to start Django's ORM before importing models
import HorizonBackend.core.runtime  # <-- REQUIRED, DO NOT DELETE !!

import pytz
import datetime
import mock
from django.test import TestCase
from HorizonBackend.chatbot_manager.models import DialogFlowTransaction

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.EntityEngine import EntityEngine
from HorizonCore.Framework.EntityManager import EntityManager
from HorizonCore.Framework.TelegramDispatcher import TelegramDispatcher
from HorizonCore.ToolBox.Utils import Utils

UpdateHistory = []
TelegramHistory = []
ActionHistory = []


class EntityEngineSpecifications(TestCase):

    def setUp(self):
        Utils.DEBUG_PRINT_ENABLED = False

        global UpdateHistory
        self.UpdateHistory = []

        global TelegramHistory
        TelegramHistory = []

        global ActionHistory
        ActionHistory = []

        EntityManager.Reset()

        self.transactionDateTime = datetime.datetime(2018, 7, 18, 5, 45, tzinfo=pytz.UTC)

        DialogFlowTransaction.objects.filter(date_event_generated=self.transactionDateTime).all().delete()

    def tearDown(self):
        Utils.DEBUG_PRINT_ENABLED = True
        DialogFlowTransaction.objects.filter(date_event_generated=self.transactionDateTime).all().delete()

    def test_SpecifyThatEntityEngineCanBeConstructed(self):

        # Ensure that all singletons are reset
        self.assertEqual(0, BaseEntity.GetNextValidId(), "GetNextValidId 1")
        self.assertEqual({}, EntityManager._getEntityMap(), "_getEntityMap 1")
        self.assertEqual(True, TelegramDispatcher().PriorityQ.IsEmpty(), "PriorityQ 1")

        # Create the engine
        entityEngine = self.CreateTestEntityEngine()

        # Get references to objects under test
        entityMap = EntityManager._getEntityMap()
        actionMap = entityEngine._actionMap
        entityOne = entityMap[0]
        entityTwo = entityMap[1]

        # Assert singletons
        self.assertEqual(True, TelegramDispatcher().PriorityQ.IsEmpty(), "PriorityQ 2")

        # Assert entityMap
        self.assertEqual(2, len(entityMap), "len(entityMap)")
        self.assertEqual("TestEntityOne", type(entityMap[0]).__name__, "entityMap[0]")
        self.assertEqual("TestEntityTwo", type(entityMap[1]).__name__, "entityMap[1]")
        self.assertEqual(0, entityMap[0].Id, "entityMap[0].Id")
        self.assertEqual(1, entityMap[1].Id, "entityMap[1].Id")

        # Assert actionMap
        self.assertEqual(4, len(actionMap), "len(actionMap)")
        self.assertEqual("ActionOn", list(actionMap.keys())[0], "key 0")
        self.assertEqual("ActionOff", list(actionMap.keys())[1], "key 1")
        self.assertEqual("ActionEnable", list(actionMap.keys())[2], "key 2")
        self.assertEqual("ActionDisable", list(actionMap.keys())[3], "key 3")
        self.assertEqual(actionMap['ActionOn']['FunctionToExecute'], entityOne.ActionOn)
        self.assertEqual(actionMap['ActionOff']['FunctionToExecute'], entityOne.ActionOff)
        self.assertEqual(actionMap['ActionEnable']['FunctionToExecute'], entityTwo.ActionEnable)
        self.assertEqual(actionMap['ActionDisable']['FunctionToExecute'], entityTwo.ActionDisable)

    def test_SpecifyThatEntitiesCanBeUpdated(self):
        entityEngine = self.CreateTestEntityEngine()

        entityEngine.FireEngineCylinders()

        self.assertEqual('TestEntityOne was updated', UpdateHistory[0])
        self.assertEqual('TestEntityTwo was updated', UpdateHistory[1])

    def test_SpecifyThatEntityCanSendAndReceiveTelegrams(self):
        entityEngine = self.CreateTestEntityEngine()

        entityEngine.FireEngineCylinders()

        self.assertEqual('TestEntityTwo received a telegram', TelegramHistory[0])

    @mock.patch('HorizonCore.Framework.EntityEngine._thread.start_new_thread')
    def test_SpecifyThatASimpleDialogFlowRequestCanBeProcessedOnASeparateThread(self, mock_start_new_thread):
        # Populate the database with a simple request
        self.CreateSimpleDialogFlowRequest()

        # Assert transaction in database
        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_event_generated), 'date_event_generated 1')
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_received), 'date_received 1')
        self.assertEqual("{'result': {'action': 'ActionEnable'}}", str(processedTransaction.body), 'body 1')
        self.assertEqual(None, processedTransaction.request_meta, 'request_meta 1')
        self.assertEqual(None,  processedTransaction.response, 'response 1')
        self.assertEqual(str(DialogFlowTransaction.UNPROCESSED), processedTransaction.status, 'status 1')

        # Create the engine with a mock thread
        entityEngine = self.CreateTestEntityEngine()

        # Fire the engine through one cycle
        entityEngine.FireEngineCylinders()

        # Assert thread was called with correct parameters
        self.assertEqual(True, mock_start_new_thread.called)
        self.assertIn('EntityEngine._executeSimpleRequest', str(mock_start_new_thread.call_args))
        self.assertIn('TestEntityTwo.ActionEnable', str(mock_start_new_thread.call_args))
        self.assertIn("'UseRequestData': False", str(mock_start_new_thread.call_args))

        # Assert transaction in database after one engine cycle
        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_event_generated), 'date_event_generated')
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_received), 'date_received')
        self.assertEqual("{'result': {'action': 'ActionEnable'}}", str(processedTransaction.body), 'body')
        self.assertEqual(None, processedTransaction.request_meta, 'request_meta')
        self.assertEqual("{'source': 'https://sunny-ai.com', 'speech': '', 'displayText': ''}", str(processedTransaction.response), 'response')
        self.assertEqual(str(DialogFlowTransaction.PROCESSED), processedTransaction.status, 'status')

    @mock.patch('HorizonCore.Framework.EntityEngine._thread.start_new_thread')
    def test_SpecifyThatAComplexDialogFlowRequestCanBeProcessedOnASeparateThread(self, mock_start_new_thread):
        # Populate the database with a complex request
        self.CreateComplexDialogFlowRequest()

        # Assert transaction in database
        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_event_generated), 'date_event_generated 1')
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_received), 'date_received 1')
        self.assertEqual("{'result': {'action': 'ActionOn'}}", str(processedTransaction.body), 'body 1')
        self.assertEqual(None, processedTransaction.request_meta, 'request_meta 1')
        self.assertEqual(None, processedTransaction.response, 'response 1')
        self.assertEqual(str(DialogFlowTransaction.UNPROCESSED), processedTransaction.status, 'status 1')

        # Create the engine with a mock thread
        entityEngine = self.CreateTestEntityEngine()

        # Fire the engine through one cycle
        entityEngine.FireEngineCylinders()

        # Assert thread was called with correct parameters
        self.assertEqual(True, mock_start_new_thread.called)
        self.assertIn('EntityEngine._executeComplexRequest', str(mock_start_new_thread.call_args))
        self.assertIn('TestEntityOne.ActionOn', str(mock_start_new_thread.call_args))
        self.assertIn("'UseRequestData': True", str(mock_start_new_thread.call_args))

        # Assert transaction in database after one engine cycle
        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_event_generated), 'date_event_generated')
        self.assertEqual('2018-07-18 05:45:00+00:00', str(processedTransaction.date_received), 'date_received')
        self.assertEqual("{'result': {'action': 'ActionOn'}}", str(processedTransaction.body), 'body')
        self.assertEqual(None, processedTransaction.request_meta, 'request_meta')
        self.assertEqual("{'source': 'https://sunny-ai.com', 'speech': '', 'displayText': ''}", str(processedTransaction.response), 'response')
        self.assertEqual(str(DialogFlowTransaction.PROCESSED), processedTransaction.status, 'status')

    def test_SpecifyThatASimpleDialogFlowRequestCanBeExecuted(self):
        # setup
        self.CreateSimpleDialogFlowRequest()
        entityEngine = self.CreateTestEntityEngine()

        # execute the request
        transaction = DialogFlowTransaction.objects.first()
        action = entityEngine._actionMap.get(transaction.body['result']['action'])
        entityEngine._executeSimpleRequest(transaction, action)

        # Assert action performed
        self.assertEqual(1, len(ActionHistory), 'len(ActionHistory)')
        self.assertEqual('TestEntityTwo.ActionEnable() was called', ActionHistory[0], 'ActionHistory[0]')

        self.assertEqual(
            "[call.SendWorkingOnItMessage(), call.SendStateMessage('ActionEnableDone')]",
            str(entityEngine._baseCoach.method_calls))

    def test_SpecifyThatAComplexDialogFlowRequestCanBeExecuted(self):
        # setup
        self.CreateComplexDialogFlowRequest()
        entityEngine = self.CreateTestEntityEngine()

        # execute the request
        transaction = DialogFlowTransaction.objects.first()
        action = entityEngine._actionMap.get(transaction.body['result']['action'])
        entityEngine._executeComplexRequest(transaction, action)

        # Assert action performed
        self.assertEqual(1, len(ActionHistory), 'len(ActionHistory)')
        self.assertEqual('TestEntityOne.ActionOn() was called', ActionHistory[0], 'ActionHistory[0]')

    @mock.patch('HorizonCore.Framework.EntityEngine.print', create=True)
    def test_SpecifyThatAErrorWhilstProcessingADialogFlowRequestCanBeHandledInTheMainThread(self, print_):
        self.CreateComplexDialogFlowRequestThatResultsInAnError()

        entityEngine = self.CreateTestEntityEngine()
        entityEngine._processRequest = lambda x: 1/0

        entityEngine.FireEngineCylinders()

        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual(str(DialogFlowTransaction.ERROR), processedTransaction.status)

        print_.assert_called_with("<<EntityEngine>> An error occurred while processing the DialogFlow request :: division by zero")

    @mock.patch('HorizonCore.Framework.EntityEngine.print', create=True)
    def test_SpecifyThatAErrorWhilstProcessingASimpleRequestCanBeHandledInTheSubThread(self, print_):
        self.CreateSimpleDialogFlowRequestThatResultsInAnError()

        entityEngine = self.CreateTestEntityEngine()

        # execute the request
        transaction = DialogFlowTransaction.objects.first()
        action = entityEngine._actionMap.get(transaction.body['result']['action'])
        entityEngine._executeSimpleRequest(transaction, action)

        # Assert action performed
        self.assertEqual(1, len(ActionHistory))
        self.assertEqual('TestEntityTwo.ActionDisable() was called', ActionHistory[0])

        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual(str(DialogFlowTransaction.ERROR), processedTransaction.status)

        print_.assert_called_with(
            "<<EntityEngine>> An error occurred while processing the DialogFlow request :: An error occurred while processing ActionDisable()")

    @mock.patch('HorizonCore.Framework.EntityEngine.print', create=True)
    def test_SpecifyThatAErrorWhilstProcessingAComplexRequestCanBeHandledInTheSubThread(self, print_):
        # setup
        self.CreateComplexDialogFlowRequestThatResultsInAnError()
        entityEngine = self.CreateTestEntityEngine()

        # execute the request
        transaction = DialogFlowTransaction.objects.first()
        action = entityEngine._actionMap.get(transaction.body['result']['action'])
        entityEngine._executeComplexRequest(transaction, action)

        # Assert action performed
        self.assertEqual(1, len(ActionHistory))
        self.assertEqual('TestEntityOne.ActionOff() was called', ActionHistory[0])

        processedTransaction = DialogFlowTransaction.objects.first()
        self.assertEqual(str(DialogFlowTransaction.ERROR), processedTransaction.status)

        print_.assert_called_with(
            "<<EntityEngine>> An error occurred while processing the DialogFlow request :: An error occurred while processing ActionOff()")

    def test_SpecifyThatMultiDialogFlowRequestCanBeProcessInChronologicalOrder(self):
        # Setup the database
        self.CreateDialogFlowRequest(self.transactionDateTime + datetime.timedelta(minutes=2), 'ActionEnable')
        self.CreateDialogFlowRequest(self.transactionDateTime + datetime.timedelta(minutes=-1), 'ActionEnable')
        self.CreateDialogFlowRequest(self.transactionDateTime + datetime.timedelta(minutes=1), 'ActionEnable')
        self.CreateDialogFlowRequest(self.transactionDateTime + datetime.timedelta(minutes=0), 'ActionEnable')
        self.CreateDialogFlowRequest(self.transactionDateTime + datetime.timedelta(minutes=-2), 'ActionEnable')

        # setup
        entityEngine = self.CreateTestEntityEngine()

        # execute
        transactions = entityEngine._getTransactionsToProcess()

        # assert
        self.assertEqual(5, transactions.count(), 'count')
        self.assertEqual('2018-07-18 05:43:00+00:00', str(transactions[0].date_event_generated), 'date_event_generated 0')
        self.assertEqual('2018-07-18 05:44:00+00:00', str(transactions[1].date_event_generated), 'date_event_generated 1')
        self.assertEqual('2018-07-18 05:45:00+00:00', str(transactions[2].date_event_generated), 'date_event_generated 2')
        self.assertEqual('2018-07-18 05:46:00+00:00', str(transactions[3].date_event_generated), 'date_event_generated 3')
        self.assertEqual('2018-07-18 05:47:00+00:00', str(transactions[4].date_event_generated), 'date_event_generated 4')

    def test_SpecifyThatTheUserIsNotifiedWhenAnUnrecognisedActionIsRequested(self):
        # Setup the database
        self.CreateDialogFlowRequest(self.transactionDateTime, 'UnrecognisedAction')

        # setup
        entityEngine = self.CreateTestEntityEngine()

        # execute
        entityEngine.FireEngineCylinders()

        # assert
        self.assertEqual(
            "[call.SendMessageToUser(\"Sorry something went wrong. I don't recognise this request: 'UnrecognisedAction'\")]",
            str(entityEngine._baseCoach.method_calls))

    # Creation methods
    # ==================================================================================================================

    @staticmethod
    def CreateTestEntityEngine():
        return EntityEngine(
            baseCoach=mock.Mock(),
            entities=[
                TestEntityOne(),
                TestEntityTwo(),
            ]
        )

    @staticmethod
    def CreateDialogFlowRequest(transactionDateTime, actionFunctionName):
        DialogFlowTransaction.objects.create(
            date_event_generated=transactionDateTime,
            date_received=transactionDateTime,
            body={'result': {'action': actionFunctionName}},
            status=DialogFlowTransaction.UNPROCESSED
        )

    def CreateSimpleDialogFlowRequest(self):
        self.CreateDialogFlowRequest(self.transactionDateTime, 'ActionEnable')

    def CreateComplexDialogFlowRequest(self):
        self.CreateDialogFlowRequest(self.transactionDateTime, 'ActionOn')

    def CreateSimpleDialogFlowRequestThatResultsInAnError(self):
        self.CreateDialogFlowRequest(self.transactionDateTime, 'ActionDisable')

    def CreateComplexDialogFlowRequestThatResultsInAnError(self):
        self.CreateDialogFlowRequest(self.transactionDateTime, 'ActionOff')


class TestEntityOne(BaseEntity):
    def Update(self):

        UpdateHistory.append('TestEntityOne was updated')

        TelegramDispatcher().DispatchTelegram(
            delay=0,
            senderId=0,
            receiverId=1,
            message='message',
            extraInfo=None)

    def HandleTelegram(self, telegram):
        TelegramHistory.append('TestEntityOne received a telegram')

    @property
    def ActionMap(self):
        return {
            'ActionOn': {
                'FunctionToExecute': self.ActionOn,
                'ResponseName': 'ActionOnDone',
                'UseRequestData': True
            },
            'ActionOff': {
                'FunctionToExecute': self.ActionOff,
                'ResponseName': 'ActionOffDone',
                'UseRequestData': True
            },
        }

    @staticmethod
    def ActionOn(requestData):
        ActionHistory.append('TestEntityOne.ActionOn() was called')

    @staticmethod
    def ActionOff(requestData):
        ActionHistory.append('TestEntityOne.ActionOff() was called')
        raise Exception('An error occurred while processing ActionOff()')


class TestEntityTwo(BaseEntity):
    def Update(self):
        UpdateHistory.append('TestEntityTwo was updated')

    def HandleTelegram(self, telegram):
        TelegramHistory.append('TestEntityTwo received a telegram')

    @property
    def ActionMap(self):
        return {
            'ActionEnable': {
                'FunctionToExecute': self.ActionEnable,
                'ResponseName': 'ActionEnableDone',
                'UseRequestData': False
            },
            'ActionDisable': {
                'FunctionToExecute': self.ActionDisable,
                'ResponseName': 'ActionDisableDone',
                'UseRequestData': False
            },
        }

    @staticmethod
    def ActionEnable():
        ActionHistory.append('TestEntityTwo.ActionEnable() was called')

    @staticmethod
    def ActionDisable():
        ActionHistory.append('TestEntityTwo.ActionDisable() was called')
        raise Exception('An error occurred while processing ActionDisable()')
