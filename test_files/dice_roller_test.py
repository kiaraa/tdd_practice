import unittest

from project_files.yahtzee_game.dice_roller import DiceRoller


class TestDiceRoller(unittest.TestCase):


    def test_returns_5_numbers(self):
        dice_roller = DiceRoller()
        dice = dice_roller.roll_dice()
        self.assertEqual(len(dice), 5)

    def test_rolls_5_random_die(self):
        dice_roller = DiceRoller()
        allTheDice = []
        for i in range(0,10000):
            allTheDice.append(dice_roller.roll_dice())

        ones = self.count(allTheDice, 1)
        twos = self.count(allTheDice, 2)
        threes = self.count(allTheDice, 3)
        fours = self.count(allTheDice, 4)
        fives = self.count(allTheDice, 5)
        sixes = self.count(allTheDice, 6)

        self.assertGreater(ones, 7500)
        self.assertLess(ones, 9000)
        self.assertGreater(twos, 7500)
        self.assertLess(twos, 9000)
        self.assertGreater(threes, 7500)
        self.assertLess(threes, 9000)
        self.assertGreater(fours, 7500)
        self.assertLess(fours, 9000)
        self.assertGreater(fives, 7500)
        self.assertLess(fives, 9000)
        self.assertGreater(sixes, 7500)
        self.assertLess(sixes, 9000)


    def count(self, allTheDice, target_number):
        count = 0
        for dice_set in allTheDice:
            for dice in dice_set:
                if target_number == dice:
                    count += 1
        return count

    def test_rolls_are_different(self):
        dice_roller = DiceRoller()
        set1 = dice_roller.roll_dice()
        set2 = dice_roller.roll_dice()
        set3 = dice_roller.roll_dice()
        set4 = dice_roller.roll_dice()
        set5 = dice_roller.roll_dice()
        set6 = dice_roller.roll_dice()
        set7 = dice_roller.roll_dice()
        self.assertTrue(set1 != set2 and set2 != set3 and set3 != set4 and set4 != set5 and set5 != set6 and set6 != set7)