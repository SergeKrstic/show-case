import unittest

from HorizonCore.Framework.GoalEvaluator import GoalEvaluator


class GoalEvaluatorSpecifications(unittest.TestCase):

    def test_SpecifyThatGoalEvaluatorCanBeConstructed(self):
        # arrange
        goalEvaluator = self.CreateGoalEvaluator()

        # assert
        self.assertEqual(1.0, goalEvaluator._characterBias)

    def test_SpecifyThatCalculateDesirabilityRaisesNotImplementedError(self):
        # arrange
        goalEvaluator = self.CreateGoalEvaluator()

        # assert
        self.assertRaises(NotImplementedError, goalEvaluator.CalculateDesirability, None)

    def test_SpecifyThatSetGoalRaisesNotImplementedError(self):
        # arrange
        goalEvaluator = self.CreateGoalEvaluator()

        # assert
        self.assertRaises(NotImplementedError, goalEvaluator.SetGoal, None)

    @staticmethod
    def CreateGoalEvaluator():
        return GoalEvaluator(characterBias=1.0)
