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
from test_files.mocks.mockui import MockUI
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
        self.scorer = Scorer()
        self.turn_manager = TurnManager(UI=self.ui, dice_roller=self.dice_roller, scorer=self.scorecard)

    def test_says_whos_turn_it_is(self):
        self.turn_manager.take_a_turn(self.scorecard)
        
        self.assertTrue(self.ui.check_if_message_was_displayed(self.player_name + "'s turn."))

    def test_calls_dice_roller(self):
        self.dice_roller.set_dice([1, 2, 3, 4, 5])

        self.turn_manager.take_a_turn(scorecard=self.scorecard)

        self.assertTrue(self.ui.check_if_message_was_displayed("You rolled: 1 2 3 4 5"))

    def test_calls_dice_roller(self):
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

