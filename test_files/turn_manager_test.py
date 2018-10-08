'''
The turn manager will:
-say who's turn it is
-call the dice roller
-show the dice roll
-call the scorecard to check what scoring methods are available
-ask the user what scoring method to use
-call scorer to decide the score
-call the scorecard and tell it to update itself
-tell the user how much they scored and their total score
-end the turn
'''

import unittest

from project_files.yahtzee_game.yahtzee_scorer import Scorer
from test_files.mocks.mock_ui import MockUI
from project_files.yahtzee_game.yahtzee_scorecard import Scorecard
from project_files.yahtzee_game.turn_manager import TurnManager
import random, string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class MockDiceRoller:

    def __init__(self):
        self.dice = []

    def roll_dice(self):
        return self.dice

    def set_dice(self, dice):
        self.dice = dice



class TestYahtzeeTurnManager(unittest.TestCase):

    def setup_method(self, method):
        self.ui = MockUI()
        self.player_name = randomword(10)
        self.scorecard = Scorecard(player_name=self.player_name)
        self.dice_roller = MockDiceRoller()
        self.dice_roller.set_dice([1, 1, 1, 1, 1])
        self.scorer = Scorer()
        self.ui.set_test_response("full_house")
        self.turn_manager = TurnManager(UI=self.ui, dice_roller=self.dice_roller, scorer=self.scorer)


    def test_says_whos_turn_it_is(self):
        self.turn_manager.take_a_turn(self.scorecard)
        
        self.assertTrue(self.ui.check_if_message_was_displayed(self.player_name + "'s turn."))

    def test_calls_dice_roller(self):
        self.dice_roller.set_dice([1, 2, 3, 4, 5])

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertTrue(self.ui.check_if_message_was_displayed("You rolled: 1 2 3 4 5"))

    def test_calls_dice_roller_in_a_different_way(self):
        self.dice_roller.set_dice([1, 2, 2, 4, 6])

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertTrue(self.ui.check_if_message_was_displayed("You rolled: 1 2 2 4 6"))

    def test_says_turn_before_saying_dice(self):
        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        output_to_user = self.ui.get_all_output_to_user()

        self.assertEquals(output_to_user[0], self.player_name + "'s turn.")

    def test_asks_user_which_scoring_rule_to_use(self):
        self.setup_scorecard_to_have_these_rules_available(self.scorecard, ["ones", "full_house"])

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertEqual(self.ui.last_question_to_user(), "What scoring method do you want to use? Choose from: ones, full_house")

    def test_asks_user_which_scoring_rule_to_use_with_three(self):
        self.setup_scorecard_to_have_these_rules_available(self.scorecard, ["ones", "full_house", "anything"])

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertEqual(self.ui.last_question_to_user(), "What scoring method do you want to use? Choose from: ones, full_house, anything")

    def setup_scorecard_to_have_these_rules_available(self, scorecard, score_types):
        scorecard.available_score_types = score_types

    def test_scorecard_is_updated_according_to_user_choice(self):
        self.setup_scorecard_to_have_these_rules_available(self.scorecard, ["twos"])
        self.dice_roller.set_dice([1, 2, 2, 4, 6])
        self.ui.set_test_response("twos")

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertEqual(self.scorecard.total_score, 4)

    def test_tells_user_about_their_score(self):
        self.setup_scorecard_to_have_these_rules_available(self.scorecard, ["fours"])
        self.dice_roller.set_dice([4, 4, 2, 4, 6])
        self.ui.set_test_response("fours")

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertTrue(self.ui.check_if_message_was_displayed("You scored 12 points this turn.  Your total score is: 12"))

    def test_tells_user_score_with_points_already(self):
        self.setup_scorecard_to_have_these_rules_available(self.scorecard, ["two_pairs"])
        self.scorecard.total_score = 6
        self.dice_roller.set_dice([4, 4, 3, 3, 6])
        self.ui.set_test_response("two_pairs")

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertTrue(self.ui.check_if_message_was_displayed("You scored 14 points this turn.  Your total score is: 20"))