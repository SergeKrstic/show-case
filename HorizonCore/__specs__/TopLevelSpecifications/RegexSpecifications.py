import unittest
import re


class RegexSpecifications(unittest.TestCase):

    def test_SpecifyThatARegularExpressionCanBeExecuted(self):
        # setup
        pattern = r"(.*) are (.*?) .*"
        string = "Cats are smarter than dogs"

        # execute
        matches = re.match(pattern, string, re.M | re.I)

        # verify
        self.assertEqual(matches.group(0), "Cats are smarter than dogs")
        self.assertEqual(matches.group(1), "Cats")
        self.assertEqual(matches.group(2), "smarter")

    def test_SpecifyThatLabelsCanBeExtractedFromCardTitles(self):
        # setup
        pattern = r"(^\[.*] )(.*$)"
        string = "[Clothes] [Shoes] Black thongs"

        # execute
        matches = re.match(pattern, string)

        # verify
        self.assertNotEqual(matches, None)
        self.assertEqual(matches.group(0), "[Clothes] [Shoes] Black thongs")
        self.assertEqual(matches.group(1), "[Clothes] [Shoes] ")
        self.assertEqual(matches.group(2), "Black thongs")

if __name__ == '__main__':
    unittest.main()
