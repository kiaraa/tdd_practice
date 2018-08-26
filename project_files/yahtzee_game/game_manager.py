class GameManager():

    def __init__(self, UI, dice_roller):
        self.ui = UI
        self.dice_roller = dice_roller

    def start_game(self):
        self.ui.display("Welcome to YAHTZEE!!!!!")
        dice_roll = self.dice_roller.roll_dice()
        self.ui.display("Dice roll: " + str(dice_roll))
