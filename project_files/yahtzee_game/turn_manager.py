'''The turn manager will:
-say who's turn it is
-call the dice roller
-show the dice roll
-call the scorecard to check what scoring methods are available
-ask the user what scoring method to use
-call scorer to decide the score
-call the scorecard and tell it to update itself
-tell the user how much they scored and their total score
-end the turn
-'''


class TurnManager:

    def __init__(self, UI, dice_roller, scorer):
        self.ui = UI
        self.dice_roller = dice_roller
        self.scorer = scorer


    def take_a_turn(self, scorecard):
        self.ui.display(message = scorecard.player_name + "'s turn.")

        dice = self.dice_roller.roll_dice()
        self.ui.display(message=(self.build_dice_string(dice)))

        score_types_message = "What scoring method do you want to use? Choose from: " + ", ".join(scorecard.available_score_types)
        self.ui.ask_user(message=score_types_message)

    def build_dice_string(self, dice):
        message = "You rolled:"
        for die in dice:
            message += " " + str(die)
        return message
