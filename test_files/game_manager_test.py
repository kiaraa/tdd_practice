import unittest

from project_files.yahtzee_game.game_manager import GameManager
from project_files.yahtzee_game.yahtzee_scorecard import Scorecard
from test_files.mocks.mock_ui import MockUI
from test_files.mocks.mock_victory_declarer import MockVictoryDeclarer
from test_files.mocks.mock_turn_manager import MockTurnManager


class GameManagerTest(unittest.TestCase):

    def setup_method(self, method):
        self.ui = MockUI()
        self.turn_manager = MockTurnManager()
        self.victory_declarer = MockVictoryDeclarer()
        self.game_manager = GameManager(UI=self.ui, turn_manager=self.turn_manager, victory_declarer=self.victory_declarer)

        self.ui.set_test_response(0)

    def test_welcome_message(self):
        self.game_manager.play_game()
        self.assertTrue(self.ui.check_if_message_was_displayed("Welcome to YAHTZEE!!!!!"))

    def test_welcome_message_comes_before_asking_number_of_players(self):
        self.game_manager.play_game()

        output_to_user = self.ui.get_all_output_to_user()
        self.assertEquals(output_to_user[0], "Welcome to YAHTZEE!!!!!")

    def test_asks_for_number_of_users_and_creates_a_scorecard_for_each(self):
        self.ui.set_test_response('2')

        self.game_manager.play_game()

        self.assertEqual(self.ui.last_question_to_user(), "How many people are playing? ")
        self.assertTrue(len(self.game_manager.scorecards) == 2)
        for scorecard in self.game_manager.scorecards:
            self.assertIsInstance(scorecard, Scorecard)

        self.assertEqual(self.game_manager.scorecards[0].player_name, "Player 1")
        self.assertEqual(self.game_manager.scorecards[1].player_name, "Player 2")

    def test_asks_for_number_of_users_with_3_users(self):
        self.ui.set_test_response(3)

        self.game_manager.play_game()

        self.assertEqual(self.ui.last_question_to_user(), "How many people are playing? ")
        self.assertTrue(len(self.game_manager.scorecards) == 3)
        for scorecard in self.game_manager.scorecards:
            self.assertIsInstance(scorecard, Scorecard)

        self.assertEqual(self.game_manager.scorecards[0].player_name, "Player 1")
        self.assertEqual(self.game_manager.scorecards[1].player_name, "Player 2")
        self.assertEqual(self.game_manager.scorecards[2].player_name, "Player 3")

    def test_calls_take_a_turn_for_three_users(self):
        self.ui.set_test_response(3)

        self.game_manager.play_game()

        scorecard1 = self.game_manager.scorecards[0]
        scorecard2 = self.game_manager.scorecards[1]
        scorecard3 = self.game_manager.scorecards[2]

        scorecards_used_for_turns = self.turn_manager.get_turn_parameters()
        self.assertEquals(scorecard1, scorecards_used_for_turns[0])
        self.assertEquals(scorecard2, scorecards_used_for_turns[1])
        self.assertEquals(scorecard3, scorecards_used_for_turns[2])

    def test_each_player_takes_a_turn_for_each_score_type(self):
        self.ui.set_test_response(2)

        self.game_manager.play_game()

        expected_number_of_turns_per_player = len(Scorecard(player_name="nobody").available_score_types)
        self.assertEquals(self.turn_manager.number_of_turns_taken(), expected_number_of_turns_per_player * 2)

    def check_a_blank_line_happens_before_every_turn(self, scorecard):
        self.assertEqual(self.ui.get_all_output_to_user()[-1], "")

    def test_empty_line_between_turns(self):
        self.ui.set_test_response(2)

        self.turn_manager.take_a_turn = self.check_a_blank_line_happens_before_every_turn
        self.game_manager.play_game()

        expected_number_of_turns_per_player = len(Scorecard(player_name="nobody").available_score_types)
        output = self.ui.get_all_output_to_user()
        self.assertTrue(len(output) == expected_number_of_turns_per_player * 2 + 4)

    def test_declares_correct_winner(self):
        self.ui.set_test_response(5)
        self.victory_declarer.set_the_winner("Player 3")

        self.game_manager.play_game()

        actual_scorecards = self.game_manager.scorecards
        passed_scorecards = self.victory_declarer.get_passed_scorecards()

        self.assertListEqual(passed_scorecards, actual_scorecards)
        self.assertTrue(self.victory_declarer.get_declare_victor_was_called())
        self.assertEqual(self.ui.get_last_output_to_user(), "Player 3 wins! Thanks for wasting your time on Yahtzee!")
        self.assertTrue(self.victory_declarer.was_called_after_scorecards_have_been_updated())

