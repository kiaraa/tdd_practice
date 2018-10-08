from project_files.yahtzee_game.game_manager import GameManager
from project_files.yahtzee_game.turn_manager import TurnManager
from project_files.yahtzee_game.ui import UI
from project_files.yahtzee_game.yahtzee_victory_declarer import VictoryDeclarer

ui = UI()
turn_manager = TurnManager()
victory_declarer = VictoryDeclarer()
game_manager = GameManager(UI=ui, turn_manager=turn_manager, victory_declarer=victory_declarer)

game_manager.play_game()
