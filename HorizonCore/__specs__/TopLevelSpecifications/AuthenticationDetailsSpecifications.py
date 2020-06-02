import unittest

from HorizonCore.AuthenticationDetails import AuthenticationDetails


class AuthenticationDetailsSpecifications(unittest.TestCase):

    # These key are important, so some duplication here is justified

    def test_SpecifyThatAuthenticationDetailsForLiveAccountAreCorrect(self):

        self.assertEqual(AuthenticationDetails.TrelloApiKey,
                         'be289cb776d5951803174a11968faed1')

        self.assertEqual(AuthenticationDetails.TrelloApiSecret,
                         'Emperor30')

        self.assertEqual(AuthenticationDetails.TrelloResourceOwnerToken,
                         '62d7d3732da709db13ace041302d64dee46f6c32442120f6a3edbf7b517949fb')

        self.assertEqual(AuthenticationDetails.TrelloResourceOwnerSecret,
                         'Emperor30')

    # def test_SpecifyThatAuthenticationDetailsForTestAccountAreCorrect(self):
    #
    #     self.assertEqual(AuthenticationDetails.TrelloApiKey,
    #                      'd0a575d8dc6b07ef0b0a198a9ddc7325')
    #
    #     self.assertEqual(AuthenticationDetails.TrelloApiSecret,
    #                      'Emperor30')
    #
    #     self.assertEqual(AuthenticationDetails.TrelloResourceOwnerToken,
    #                      '9af1a59d81de8dd3f0f6bad43d987e90c4a94f9145bb7b24cd08ee1cd54d04c5')
    #
    #     self.assertEqual(AuthenticationDetails.TrelloResourceOwnerSecret,
    #                      'Emperor30')


if __name__ == '__main__':
    unittest.main()
