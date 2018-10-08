import random

class DiceRoller:
    def __init__(self):
        pass

    def roll_dice(self):
        dice_set = []
        for i in range (0, 5):
            dice_set.append(random.randint(1, 6))
        return dice_set
