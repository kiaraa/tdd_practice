import unittest

from project_files.yahtzee_game.game_manager import GameManager


class MockUI:

    def __init__(self):
        self.list_of_displayed_messages = []

    def display(self, message):
        self.list_of_displayed_messages.append(message)

    def check_if_method_was_displayed(self, message):
        if message in self.list_of_displayed_messages:
            return True
        else:
            return False


class MockDiceRoller:

    def __init__(self):
        self.dice_to_return = None

    def set_up_the_mock_to_return_these_dice(self, dice):
        self.dice_to_return = dice

    def roll_dice(self):
        return self.dice_to_return


class GameManagerTest(unittest.TestCase):

    def setup_method(self, method):
        self.ui = MockUI()
        self.dice_roller = MockDiceRoller()
        self.game_manager = GameManager(UI=self.ui, dice_roller=self.dice_roller)

    def test_welcome_message(self):
        self.game_manager.start_game()
        self.assertTrue(self.ui.check_if_method_was_displayed("Welcome to YAHTZEE!!!!!"))

    def test_rolls_the_dice(self):
        self.dice_roller.set_up_the_mock_to_return_these_dice([2,2,4,5,6])
        self.game_manager.start_game()
        self.assertTrue(self.ui.check_if_method_was_displayed("Dice roll: [2, 2, 4, 5, 6]"))


# TODO: divide game manager into turn manager that manages a single turn for a single player
#and game manager that controls when turn manager is called