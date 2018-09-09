import unittest

from project_files.yahtzee_game.yahtzee_scorecard import Scorecard
from project_files.yahtzee_game.yahtzee_victory_declarer import VictoryDeclarer


class TestYahtzeeVictoryDeclarer(unittest.TestCase):

    def test_tells_who_winner_is(self):
        victory_declarer = VictoryDeclarer()
        scorecards = [Scorecard(player_name="Player 1"), Scorecard(player_name="Player 2")]
        scorecards[0].total_score = 11
        scorecards[1].total_score = 2

        winner = victory_declarer.declare_victor(scorecards)

        self.assertEqual(winner, "Player 1")

    def test_tells_who_winner_is_with_three_players(self):
        victory_declarer = VictoryDeclarer()
        scorecards = [Scorecard(player_name="Player 1"), Scorecard(player_name="Player 2"), Scorecard(player_name="Player 3")]
        scorecards[0].total_score = 11
        scorecards[1].total_score = 2
        scorecards[2].total_score = 12

        winner = victory_declarer.declare_victor(scorecards)

        self.assertEqual(winner, "Player 3")

    def test_calls_a_tie(self):
        victory_declarer = VictoryDeclarer()

        scorecards = [Scorecard(player_name="Player 1"), Scorecard(player_name="Player 2"), Scorecard(player_name="Player 3")]
        scorecards[0].total_score = 11
        scorecards[1].total_score = 2
        scorecards[2].total_score = 11

        winner = victory_declarer.declare_victor(scorecards)

        self.assertEqual(winner, "Player 1 and Player 3")

    def test_calls_a_tie_with_all_zeros(self):
        victory_declarer = VictoryDeclarer()

        scorecards = [Scorecard(player_name="Player 1"), Scorecard(player_name="Player 2"), Scorecard(player_name="Player 3")]
        scorecards[0].total_score = 0
        scorecards[1].total_score = 0
        scorecards[2].total_score = 0

        winner = victory_declarer.declare_victor(scorecards)

        self.assertEqual(winner, "Player 1 and Player 2 and Player 3")
