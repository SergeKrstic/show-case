import unittest

from HorizonCore.Framework.UserFeatureMap import UserFeatureMap


class UserFeatureMapSpecifications(unittest.TestCase):

    # Physical features
    # ==================================================================================================================

    def test_SpecifyThatHealthFeatureCanBeCalculated(self):
        
        self.assertEqual(UserFeatureMap.GetHealth(), 1)

    def test_SpecifyThatEnergyLevelFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetEnergyLevel(), 1)

    def test_SpecifyThatHungerLevelFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetHungerLevel(), 1)

    def test_SpecifyThatMuscleRecoveryLevelFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetMuscleRecoveryLevel(), 1)

    # Mental features
    # ==================================================================================================================

    def test_SpecifyThatMentalClarityFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetMentalClarity(), 1)

    def test_SpecifyThatMoodValanceFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetMoodValance(), 1)

    def test_SpecifyThatMoodIntensityFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetMoodIntensity(), 1)
        
    def test_SpecifyThatMotivationalLevelFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetMotivationalLevel(), 1)

    # Distance features
    # ==================================================================================================================

    def test_SpecifyThatDistanceFromHomeFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetDistanceFromHome(), 1)

    def test_SpecifyThatDistanceFromWorkFeatureCanBeCalculated(self):
        self.assertEqual(UserFeatureMap.GetDistanceFromWork(), 1)
