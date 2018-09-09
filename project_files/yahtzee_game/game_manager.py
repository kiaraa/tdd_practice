from project_files.yahtzee_game.yahtzee_scorecard import Scorecard


class GameManager():

    def __init__(self, UI, turn_manager, victory_declarer):
        self.ui = UI
        self.turn_manager = turn_manager
        self.scorecards = []
        self.victory_declarer = victory_declarer

    def play_game(self):
        self.ui.display("Welcome to YAHTZEE!!!!!")

        number_of_players = self.ui.ask_user("How many people are playing?")
        for i in range(0, number_of_players):
            self.scorecards.append(Scorecard(player_name="Player " + str((i + 1))))

        number_of_score_types = len(Scorecard(player_name="full scorecard").available_score_types)
        for i in range(0, number_of_score_types):
            for scorecard in self.scorecards:
                self.turn_manager.take_a_turn(scorecard)

        victor = self.victory_declarer.declare_victor(self.scorecards)
        self.ui.display(victor + ' wins! Thanks for wasting your time on Yahtzee!')
