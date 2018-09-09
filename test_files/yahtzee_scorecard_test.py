import unittest

from project_files.yahtzee_game.yahtzee_exceptions import ScoreTypeNotAvailableException, InvalidScoreException
from project_files.yahtzee_game.yahtzee_scorecard import Scorecard




class TestYahtzeeScorecard(unittest.TestCase):

    def setup_method(self, method):
        self.scorecard = Scorecard(player_name="nobody should see this")
        self.all_score_types = ['yahtzee',
                                'chance',
                                'ones',
                                'twos',
                                'threes',
                                'fours',
                                'fives',
                                'sixes',
                                'pair',
                                'two_pairs',
                                'triples',
                                'quadruples',
                                'small_straight',
                                'large_straight',
                                'full_house']

    def test_initial_total_score(self):
        self.assertEqual(self.scorecard.get_total_score(), 0)

    def test_taking_turn_updates_total_score(self):
        self.scorecard.score_a_turn(turn_score=5, score_type='ones')
        self.assertEqual(self.scorecard.get_total_score(), 5)

    def test_score_sums_multiple_turns(self):
        self.scorecard.score_a_turn(turn_score=5, score_type='ones')
        self.scorecard.score_a_turn(turn_score=13, score_type='fives')
        self.assertEqual(self.scorecard.get_total_score(), 18)

    def test_all_score_types_initially_available(self):
        available_score_types = self.scorecard.get_available_score_types()
        self.assertListEqual(available_score_types, self.all_score_types)

    def test_scoring_a_turn_removes_the_score_type_from_the_available_score_types(self):
        expected_score_types = self.all_score_types
        expected_score_types.remove('triples')

        self.scorecard.score_a_turn(turn_score=1, score_type='triples')
        available_score_types = self.scorecard.get_available_score_types()

        self.assertListEqual(available_score_types, expected_score_types)

    def test_throws_exception_when_score_type_is_not_available(self):
        try:
            self.scorecard.score_a_turn(turn_score=5, score_type='ones')
            self.scorecard.score_a_turn(turn_score=5, score_type='ones')
            self.fail("expecting an exception")
        except ScoreTypeNotAvailableException as exception:
            self.assertEqual(exception.message, "This score type is not currently available to you.")

    def test_bad_score_values_give_exception(self):
        try:
            self.scorecard.score_a_turn(turn_score="hi im the best score", score_type='ones')
            self.fail("expecting an exception")
        except InvalidScoreException as exception:
            self.assertEqual(exception.message, "Score must be a non-negative integer.")

    def test_raises_exception_with_negative_score(self):
        try:
            self.scorecard.score_a_turn(turn_score=-1, score_type='ones')
            self.fail("expecting an exception")
        except InvalidScoreException as exception:
            self.assertEqual(exception.message, "Score must be a non-negative integer.")

    def test_equals(self):
        scorecard1 = Scorecard("player")
        scorecard2 = Scorecard("player")
        self.assertEquals(scorecard1, scorecard2)

        scorecard1.player_name = "player1"
        self.assertNotEqual(scorecard1, scorecard2)

        scorecard1.player_name = "player"
        scorecard1.total_score = -1
        self.assertNotEqual(scorecard1, scorecard2)

        scorecard1.total_score = 0
        scorecard1.available_score_types.append("extra type")
        self.assertNotEqual(scorecard1, scorecard2)

        scorecard2.available_score_types.append("different extra type")
        self.assertNotEqual(scorecard1, scorecard2)
