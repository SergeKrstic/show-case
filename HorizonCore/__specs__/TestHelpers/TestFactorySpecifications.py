import json
import unittest

from mock import MagicMock

from HorizonCore.AuthenticationDetails import *

from HorizonCore.__specs__.TestHelpers import TestFactory


@unittest.skip("TestFactorySpecifications")
class TestFactorySpecifications(unittest.TestCase):

    # def test_SpecifyThatTrelloClientForTestAccountCanBeConstructed(self):
    #     # act
    #     client = TestFactory.CreateMockTrelloClientForTestAccount()
    #
    #     # assert
    #     self.assertEqual(client.public_only, False, 'public_only')
    #     self.assertEqual(client.api_key, AuthenticationDetailsForTestAccount.TrelloApiKey, 'api_key')
    #     self.assertEqual(client.api_secret, AuthenticationDetailsForTestAccount.TrelloApiSecret, 'api_secret')
    #     self.assertEqual(client.resource_owner_key, AuthenticationDetailsForTestAccount.TrelloResourceOwnerToken, 'resource_owner_key')
    #     self.assertEqual(client.resource_owner_secret, AuthenticationDetailsForTestAccount.TrelloResourceOwnerSecret, 'resource_owner_secret')

    def test_SpecifyThatTrelloClientForLiveAccountCanBeConstructed(self):
        # act
        client = TestFactory.CreateMockTrelloClientForLiveAccount()

        # assert
        self.assertEqual(client.public_only, False, 'public_only')
        self.assertEqual(client.api_key, AuthenticationDetails.TrelloApiKey, 'api_key')
        self.assertEqual(client.api_secret, AuthenticationDetails.TrelloApiSecret, 'api_secret')
        self.assertEqual(client.resource_owner_key, AuthenticationDetails.TrelloResourceOwnerToken, 'resource_owner_key')
        self.assertEqual(client.resource_owner_secret, AuthenticationDetails.TrelloResourceOwnerSecret, 'resource_owner_secret')

    # def test_SpecifyThatAPublicOnlyTrelloClientCanBeConstructed(self):
    #     # act
    #     client = TestFactory.CreatePublicOnlyTrelloClient()
    #
    #     # assert
    #     self.assertEqual(client.public_only, True, 'public_only')
    #     self.assertEqual(client.api_key, AuthenticationDetailsForTestAccount.TrelloApiKey, 'api_key')
    #     self.assertEqual(client.api_secret, None, 'api_secret')
    #     self.assertEqual(client.resource_owner_key, None, 'resource_owner_key')
    #     self.assertEqual(client.resource_owner_secret, None, 'resource_owner_secret')

    def test_SpecifyThatMockTrelloClientCanRetrieveJsonDataFromTestFixtures(self):
        # arrange
        mockClient = TestFactory.CreateMockTrelloClientForLiveAccount()

        # act
        jsonResult = mockClient.fetch_json('/boards/582da009ec5f65667b9a27d5')
        with open(TestFactory.PathToFixtures + 'GetQuotesBoard.json') as fileHandle:
            expectJsonResult = json.load(fileHandle)

        # assert
        self.assertEqual(jsonResult, expectJsonResult)

    def test_SpecifyThatTestAutoMessengerCanBeConstructed(self):
        # act
        autoMessenger = TestFactory.CreateTestMotivationalCoach()

        # assert
        self.assertEqual(len(autoMessenger.User['QuoteDictionary']), 2)
        self.assertFalse(autoMessenger.debugQuoteEnable)
        self.assertFalse(autoMessenger.debugEnabled)
        self.assertEqual(autoMessenger.User['QuoteDictionary'][0]['CurrentIndexInSequence'], 0)
        self.assertEqual(autoMessenger.User['QuoteDictionary'][0]['QuoteIndexSequence'],
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_SpecifyThatTestMessengerBotCanBeConstructed(self):
        # act
        messengerBot = TestFactory.CreateTestMessengerBot()
        response = messengerBot.Text.SendTextMessage(0, 'message')

        # assert
        self.assertTrue(isinstance(messengerBot.Text.SendTextMessage, MagicMock))
        self.assertEqual(response['message_id'], 'mid.1478595407715:21ec1de737')
        self.assertEqual(response['recipient_id'], '1339438022780029')

    def test_SpecifyThatTestQuotesPopulatorCanBeConstructed(self):
        # act
        quotesPopulator = TestFactory.CreateTestQuotePopulator()

        # assert
        self.assertTrue(isinstance(quotesPopulator.trelloClient.fetch_json, MagicMock))

    # def test_SpecifyThatTestLocationsAdviserCanBeConstructed(self):
    #     # act
    #     locationsAdviser = TestFactory.CreateTestLocationsAdviser()
    #
    #     # assert
    #     self.assertIsNotNone(locationsAdviser.trelloApi)
    #     self.assertTrue(isinstance(locationsAdviser.trelloApi.fetch_json, MagicMock), 'isinstance(MagicMock)')


if __name__ == '__main__':
    unittest.main()
