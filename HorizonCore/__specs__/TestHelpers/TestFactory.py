import datetime
import datetime
import json
import mock
import pprint as pp

import HorizonCore.Configuration as Config
from HorizonCore.AuthenticationDetails import AuthenticationDetails
from HorizonCore.Framework.Enums import Entity
from HorizonAgents.Factory import Factory

PATH_TO_FIXTURES = "/Users/srdjankrstic/Programming/Projects/Horizon/WebApps/HorizonModulesSpecifications/Fixtures/"


class TestFactory:

    PathToFixtures = PATH_TO_FIXTURES

    @classmethod
    def CreateMockTrelloClient(cls, authenticationDetails):
        from ThirdPartyWrappers.trello.trelloclient import TrelloClient

        trelloClient = TrelloClient(
            api_key=authenticationDetails.TrelloApiKey,
            api_secret=authenticationDetails.TrelloApiSecret,
            token=authenticationDetails.TrelloResourceOwnerToken,
            token_secret=authenticationDetails.TrelloResourceOwnerSecret
        )

        path = PATH_TO_FIXTURES

        params = {
            ('/boards/582da009ec5f65667b9a27d5',): path + 'GetQuotesBoard.json',
            ('/boards/582da009ec5f65667b9a27d5/lists',): path + 'GetListsFromQuotesBoards.json',
            ('/lists/582e9e5f0296b645e0867a82/cards/open',): path + 'GetCardsFromMotivationalListOnQuotesBoard.json',

            # Deleting cards from Locations board
            ('boards/561f417e3c407c4eba06553a/lists',): path + 'GetListsFromLocationsBoard.json',
            ('lists/561f43201b313623eeb0de48/cards',): path + 'GetCardsFromSupermarketListOnLocationsBoard.json',
            ('/cards/5848a89ed1a060a62f5e05b5',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a89ea26a7894caf69b94',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a89f6c7940ed653ea35c',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a89f55ac5c156606deeb',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a168fdc31ce153dbc3',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a2ab67e863e14c4f7c',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a26c7940ed653ea36a',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a4836eb19ed08d7e15',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a5583643b3c9e71f4a',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a5e0bca59b6792b6b6',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a6cb163ae465a03f93',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a6ba10470c6590b449',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a72aaea2866601e0d1',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a7d63135ccde28f5aa',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a806ef7b1130340635',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('/cards/5848a8a818b4201d2ad83b29',): path + 'DeleteCardFromAnyListOnAnyBoard.json',
            ('lists/571c4567d3da88abb6a54fdd/cards',): path + 'GetCardsFromDoneListOnLocationsBoard.json',
            ('/cards/58414b8ca13c05260b855c25',): path + 'DeleteCardFromAnyListOnAnyBoard.json',

            # Get lists from board
            ('boards/56f49db819d429e22c1a40ba/lists',): path + 'GetListsFromFridgeBoard.json',
            ('boards/56f4a476510f8f63a8aff26c/lists',): path + 'GetListsFromHouseHoldBoard.json',
            ('boards/56f08dc8a02610a9835c5a36/lists',): path + 'GetListsFromPantryBoard.json',

            # Updating time stamp card from Locations board
            ('/boards/561f417e3c407c4eba06553a/cards/',): path + 'GetCardsFromLocationsBoard.json',
            ('/cards/583fc41cf87920e3d5a1d02f/desc',): path + 'PutDescriptionOnTimeStampCardFromLocationsBoard.json',

            # Process Locations board
            ('/boards/56f49db819d429e22c1a40ba/cards/',): path + 'GetCardsFromFridgeBoard.json',
            ('/boards/56f49db819d429e22c1a40ba/labels/',): path + 'GetLabelsFromFridgeBoard.json',
            ('/boards/56f4a476510f8f63a8aff26c/cards/',): path + 'GetCardsFromHouseHoldBoard.json',
            ('/boards/56f4a476510f8f63a8aff26c/labels/',): path + 'GetLabelsFromHouseHoldBoard.json',
            ('/boards/56f08dc8a02610a9835c5a36/cards/',): path + 'GetCardsFromPantryBoard.json',
            ('/boards/56f08dc8a02610a9835c5a36/labels/',): path + 'GetLabelsFromPantryBoard.json',
            ('/cards',): path + 'PostAnyCardToAnyBoard.json',
        }
        original_fetch_json = trelloClient.fetch_json

        def sideEffects(*args, **kwargs):
            if args in params.keys():
                jsonFile = params[args]
                with open(jsonFile) as fileHandle:
                    return json.load(fileHandle)
            else:
                print('#########################################################')
                print('Actual Trello database was accessed. Decide if you need to mock out this action.\n')
                print('args = ' + str(args))
                print('kwargs = \n')
                pp.pprint(kwargs)
                print('\nJSON data = \n')

                json_obj = original_fetch_json(args,
                                               http_method='GET' if kwargs.get('http_method') is None else kwargs.get(
                                                   'http_method'),
                                               headers=kwargs.get('headers'),
                                               query_params=kwargs.get('query_params'),
                                               post_args=kwargs.get('post_args'),
                                               files=kwargs.get('files'))

                print(json.dumps(json_obj, indent=4))
                print('#########################################################')
                return json_obj

        trelloClient.fetch_json = mock.MagicMock(side_effect=sideEffects)

        return trelloClient

    # @classmethod
    # def CreateMockTrelloClientForTestAccount(cls):
    #     return TestFactory.CreateMockTrelloClient(AuthenticationDetailsForTestAccount)

    @classmethod
    def CreateMockTrelloClientForLiveAccount(cls):
        return TestFactory.CreateMockTrelloClient(AuthenticationDetails)

    # @classmethod
    # def CreatePublicOnlyTrelloClient(cls):
    #     return TrelloClient(api_key=AuthenticationDetailsForTestAccount.TrelloApiKey)

    @classmethod
    def CreateTestMotivationalCoach(cls):
        from HorizonAgents.Coaching.MotivationalCoach import MotivationalCoach

        # Enable the quote categories require for testing purposes
        # for user in Config.Users:
        #     for index, quoteCategory in enumerate(user['QuoteDictionary']):
        #         quoteCategory['Enabled'] = True if index in [0, 1] else False

        # Create and configure the motivationalCoach
        motivationalCoach = MotivationalCoach(Entity.MotivationalCoach,
                                              Config.Users[0],
                                              TestFactory.CreateTestDialogFlowClient(),
                                              TestFactory.CreateTestMessengerClient(),
                                              TestFactory.CreateTestQuotePopulator())

        motivationalCoach.debugQuoteEnable = False
        motivationalCoach.debugEnabled = False

        # Configure the quote categories for testing purposes by removing randomised quote
        # index sequence, and by only enabling the first two categories
        for index, quoteCategory in enumerate(motivationalCoach.User['QuoteDictionary']):
            quoteCategory['CurrentIndexInSequence'] = 0
            quoteCategory['QuoteIndexSequence'] = list(range(len(quoteCategory['Quotes'])))

        return motivationalCoach

    @classmethod
    def CreateTestDialogFlowClient(cls):
        return Factory.CreateDialogFlowClient()

    @classmethod
    def CreateTestMessengerClient(cls):
        testBot = Factory.CreateMessengerClient()

        # Mock out the Messenger service call, we don't actually want
        # to be sending messages to the user whilst testing
        response = {
            "message_id": "mid.1478595407715:21ec1de737",
            "recipient_id": "1339438022780029"
        }

        testBot.Text.SendTextMessage = mock.MagicMock(return_value=response)

        return testBot

    @classmethod
    def CreateTestQuotePopulator(cls):
        from HorizonAgents.Coaching.MotivationalQuotesPopulator import MotivationalQuotesPopulator

        quotesPopulator = MotivationalQuotesPopulator(TestFactory.CreateMockTrelloClientForLiveAccount())

        quotesPopulator.DebugPrintEnable = False

        return quotesPopulator

    @classmethod
    def CreateTestLocationsAdviser(cls):
        from HorizonAgents.AgileAssistance.LocationsAdviser import LocationsAdviser

        return LocationsAdviser(AuthenticationDetails)

    @staticmethod
    def CreateTestEvent1():
        from HorizonCore.Framework.Event import Event

        return Event(
            name='TestEvent1',
            stateClassName='StateStartWakingUp',
            startTime=datetime.time(7, 0),
            endTime=datetime.time(8, 0))

    @classmethod
    def CreateTestEvent2(cls):
        from HorizonCore.Framework.Event import Event

        return Event(
            name='TestEvent2',
            stateClassName='TimeForMorningGreeting',
            startTime=datetime.time(8, 0),
            endTime=datetime.time(9, 30))

    @staticmethod
    def CreateTestSchedule():
        from HorizonCore.Framework.EventScheduler import EventScheduler

        event1 = TestFactory.CreateTestEvent1()
        event2 = TestFactory.CreateTestEvent2()

        schedule = EventScheduler()
        schedule.AddEvent(event1)
        schedule.AddEvent(event2)

        return schedule

    @classmethod
    def CreateTestSleepCoach(cls):
        from HorizonAgents.Coaching.SleepCoach import SleepCoach

        return SleepCoach(Entity.SleepCoach,
                          Config.Users[0],
                          TestFactory.CreateTestDialogFlowClient(),
                          TestFactory.CreateTestMessengerClient())

    @classmethod
    def CreateTestGratitudeHelper(cls):
        from HorizonAgents.Coaching.GratitudeHelper import GratitudeHelper

        return GratitudeHelper(
            Entity.GratitudeHelper,
            Config.Users[0],
            TestFactory.CreateTestDialogFlowClient(),
            TestFactory.CreateTestMessengerClient(),
            updatePeriodInSeconds=0)

    @staticmethod
    def CreateUniGraph():
        from HorizonCore.Graph.SparseGraph import SparseGraph
        from HorizonCore.Graph.GraphEdge import GraphEdge
        from HorizonCore.Graph.GraphNode import GraphNode

        sparseGraph = SparseGraph(isDigraph=False)

        node0 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node0)
        node0.Index = -1

        node1 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node1)

        node2 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node2)

        node3 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node3)

        node4 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node4)

        node5 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node5)

        node6 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node6)

        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node1.Index, toNodeIndex=node5.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node1.Index, toNodeIndex=node6.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node2.Index, toNodeIndex=node3.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node2.Index, toNodeIndex=node5.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node3.Index, toNodeIndex=node2.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node3.Index, toNodeIndex=node4.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node3.Index, toNodeIndex=node5.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node4.Index, toNodeIndex=node3.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node4.Index, toNodeIndex=node6.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node5.Index, toNodeIndex=node1.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node5.Index, toNodeIndex=node2.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node5.Index, toNodeIndex=node3.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node5.Index, toNodeIndex=node6.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node6.Index, toNodeIndex=node1.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node6.Index, toNodeIndex=node4.Index))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node6.Index, toNodeIndex=node5.Index))

        return sparseGraph

    @staticmethod
    def CreateDigraph():
        from HorizonCore.Graph.SparseGraph import SparseGraph
        from HorizonCore.Graph.GraphEdge import GraphEdge
        from HorizonCore.Graph.GraphNode import GraphNode

        sparseGraph = SparseGraph(isDigraph=True)

        node0 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node0)
        node0.Index = -1

        node1 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node1)

        node2 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node2)

        node3 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node3)

        node4 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node4)

        node5 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node5)

        node6 = GraphNode(index=sparseGraph.GetNextFreeNodeIndex())
        sparseGraph.AddNode(node6)

        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node1.Index, toNodeIndex=node5.Index, cost=2.9))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node1.Index, toNodeIndex=node6.Index, cost=1.0))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node2.Index, toNodeIndex=node3.Index, cost=3.1))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node3.Index, toNodeIndex=node5.Index, cost=0.8))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node4.Index, toNodeIndex=node3.Index, cost=3.7))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node5.Index, toNodeIndex=node2.Index, cost=1.9))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node5.Index, toNodeIndex=node6.Index, cost=3.0))
        sparseGraph.AddEdge(GraphEdge(fromNodeIndex=node6.Index, toNodeIndex=node4.Index, cost=1.1))

        return sparseGraph
