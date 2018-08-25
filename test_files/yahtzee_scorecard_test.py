import unittest

from project_files.yahtzee_game.yahtzee_scorecard import Scorecard


class TestYahtzeeScorecard(unittest.TestCase):

    def test_initial_total_score(self):
        scorecard = Scorecard()
        self.assertEqual(scorecard.get_total_score(), 0)
