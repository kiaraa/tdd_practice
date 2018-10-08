from project_files.yahtzee_game.dice_roller import DiceRoller
from project_files.yahtzee_game.turn_manager import TurnManager
from project_files.yahtzee_game.ui import UI
from project_files.yahtzee_game.yahtzee_scorer import Scorer
from project_files.yahtzee_game.yahtzee_victory_declarer import VictoryDeclarer
from project_files.yahtzee_game.game_manager import GameManager

if __name__ == '__main__':
    ui = UI()
    scorer = Scorer()
    dice_roller = DiceRoller()
    turn_manager = TurnManager(ui, dice_roller, scorer)
    victory_declarer = VictoryDeclarer()
    game_manager = GameManager(UI=ui, turn_manager=turn_manager, victory_declarer=victory_declarer)


    game_manager.play_game()
