class TurnManager:

    def __init__(self, UI, dice_roller, scorer):
        self.ui = UI
        self.dice_roller = dice_roller
        self.scorer = scorer


    def take_a_turn(self, scorecard):
        self.ui.display(message = scorecard.player_name + "'s turn.")

        dice = self.dice_roller.roll_dice()
        self.ui.display(message=(self.build_dice_string(dice)))

        score_types_message = self.build_scoring_types_string(scorecard)
        selected_score_type = self.ui.ask_user(message=score_types_message)

        turn_score = self.scorer.score(dice_set=dice, score_type=selected_score_type)
        scorecard.score_a_turn(turn_score=turn_score, score_type=selected_score_type)

        self.ui.display("You scored " + str(turn_score) + " points this turn.  Your total score is: " + str(scorecard.total_score))


    def build_scoring_types_string(self, scorecard):
        intro_message = "What scoring method do you want to use? Choose from:\n"
        types_message = ""
        type_count = 0
        for score_type in scorecard.available_score_types:
            type_count += 1
            types_message += score_type.ljust(20)

            if type_count % 3 == 0:
                types_message += "\n"

        if not types_message.endswith("\n"):
            types_message += "\n"

        return intro_message + types_message


    def build_dice_string(self, dice):
        message = "You rolled:"
        for die in dice:
            message += " " + str(die)
        return message
