from project_files.yahtzee_game.yahtzee_scorecard import Scorecard


class GameManager():

    def __init__(self, UI, turn_manager):
        self.ui = UI
        self.turn_manager = turn_manager
        self.scorecards = []

    def start_game(self):
        self.turn_manager.take_a_turn()

        number_of_players = self.ui.ask_user("How many people are playing?")
        while number_of_players != 0:
            self.scorecards.append(Scorecard())
            number_of_players -= 1

        self.ui.display("Welcome to YAHTZEE!!!!!")

#TODO: Make tests so that this ridiculous order of doing things doesn't work.