import unittest

from project_files.yahtzee_game.game_manager import GameManager
from project_files.yahtzee_game.yahtzee_scorecard import Scorecard


class MockUI:

    def __init__(self):
        self.list_of_displayed_messages = []
        self.list_of_questions= []
        self.user_response = None

    def display(self, message):
        self.list_of_displayed_messages.append(message)

    def check_if_message_was_displayed(self, message):
        if message in self.list_of_displayed_messages:
            return True
        else:
            return False

    def ask_user(self, message):
        self.list_of_questions.append(message)
        return self.user_response

    def set_test_response(self, response):
        self.user_response = response

    def last_question_to_user(self):
        return self.list_of_questions[-1]


class MockTurnManager:

    def __init__(self):
        self.take_a_turn_was_called = False

    def was_take_a_turn_called(self):
        return self.take_a_turn_was_called

    def take_a_turn(self):
        self.take_a_turn_was_called = True


class GameManagerTest(unittest.TestCase):

    def setup_method(self, method):
        self.ui = MockUI()
        self.turn_manager = MockTurnManager()
        self.ui.set_test_response(0)
        self.game_manager = GameManager(UI=self.ui, turn_manager=self.turn_manager)

    def test_welcome_message(self):
        self.game_manager.start_game()
        self.assertTrue(self.ui.check_if_message_was_displayed("Welcome to YAHTZEE!!!!!"))

    def test_takes_a_turn(self):
        self.game_manager.start_game()
        self.assertTrue(self.turn_manager.was_take_a_turn_called())

    def test_asks_for_number_of_users_and_creates_a_scorecard_for_each(self):
        self.ui.set_test_response(2)

        self.game_manager.start_game()

        self.assertEqual(self.ui.last_question_to_user(), "How many people are playing?")
        self.assertTrue(len(self.game_manager.scorecards) == 2)
        for scorecard in self.game_manager.scorecards:
            self.assertIsInstance(scorecard, Scorecard)

        self.assertNotEquals(self.game_manager.scorecards[0], self.game_manager.scorecards[1])

    def test_asks_for_number_of_users_with_3_users(self):
        self.ui.set_test_response(3)

        self.game_manager.start_game()

        self.assertEqual(self.ui.last_question_to_user(), "How many people are playing?")
        self.assertTrue(len(self.game_manager.scorecards) == 3)
        for scorecard in self.game_manager.scorecards:
            self.assertIsInstance(scorecard, Scorecard)

        self.assertNotEquals(self.game_manager.scorecards[0], self.game_manager.scorecards[1])
        self.assertNotEquals(self.game_manager.scorecards[0], self.game_manager.scorecards[2])
        self.assertNotEquals(self.game_manager.scorecards[1], self.game_manager.scorecards[2])


# TODO: divide game manager into turn manager that manages a single turn for a single player
#and game manager that controls when turn manager is called