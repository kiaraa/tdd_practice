'''The game of yatzy is a simple dice game. Each player
rolls five six-sided dice. The player places the roll in
a category, such as ones, twos, fives, pair, two pairs
etc (see below).
If the roll is compatible with the category, the player
gets a score for the roll according to the rules. If the
roll is not compatible with the category, the player scores
zero for the roll.

For example, if a player rolls 5,6,5,5,2 and scores the
dice in the fives category they would score 15 (three fives).

Your task is to score a GIVEN roll in a GIVEN category.
You do NOT have to program the random dice rolling.
You do NOT have to program re-rolls (as in the real game).
You do NOT play by letting the computer choose the highest
scoring category for a given roll.


Yatzy Categories and Scoring Rules
==================================

Chance:
The player scores the sum of all dice,
no matter what they read.
For example,
1,1,3,3,6 placed on "chance" scores 14 (1+1+3+3+6)
4,5,5,6,1 placed on "chance" scores 21 (4+5+5+6+1)

Yatzy:
If all dice have the same number,
the player scores 50 points.
For example,
1,1,1,1,1 placed on "yatzy" scores 50
5,5,5,5,5 placed on "yatzy" scores 50
1,1,1,2,1 placed on "yatzy" scores 0

Ones, Twos, Threes, Fours, Fives, Sixes:
The player scores the sum of the dice that reads one,
two, three, four, five or six, respectively.
For example,
1,1,2,4,4 placed on "fours" scores 8 (4+4)
2,3,2,5,1 placed on "twos" scores 4  (2+2)
3,3,3,4,5 placed on "ones" scores 0

Pair:
If exactly two dice have the same value then
the player scores the sum of the two highest matching dice.
For example, when placed on "pair"
3,3,3,4,4 scores 8 (4+4)
1,1,6,2,6 scores 12 (6+6)
3,3,3,4,1 scores 0
3,3,3,3,1 scores 0

Two pairs:
If exactly two dice have the same value and exactly
two dice have a different value then the
player scores the sum of these four dice.
For example, when placed on "two pairs"
1,1,2,3,3 scores 8 (1+1+3+3)
1,1,2,3,4 scores 0
1,1,2,2,2 scores 0

Three of a kind:
If there are exactly three dice with the same number
then the player scores the sum of these dice.
For example, when placed on "three of a kind"
3,3,3,4,5 scores 9 (3+3+3)
3,3,4,5,6 scores 0
3,3,3,3,1 scores 0

Four of a kind:
If there are exactly four dice with the same number
then the player scores the sum of these dice.
For example, when placed on "four of a kind"
2,2,2,2,5 scores 8 (2+2+2+2)
2,2,2,5,5 scores 0
2,2,2,2,2 scores 0

Small straight:
When placed on "small straight", if the dice read
1,2,3,4,5, the player scores 15 (the sum of all the dice).

Large straight:
When placed on "large straight", if the dice read
2,3,4,5,6, the player scores 20 (the sum of all the dice).

Full house:
If the dice are two of a kind and three of a different kind
then the player scores the sum of all five dice.
For example, when placed on "full house"
1,1,2,2,2 scores 8 (1+1+2+2+2)
2,2,3,3,4 scores 0
4,4,4,4,4 scores 0'''

import unittest

from project_files.yahtzee_game.non_supported_rule_exception import NonSupportedRuleException
from project_files.yahtzee_game.yahtzee_scorer import Scorer

class TestYahtzee(unittest.TestCase):

    def setup_method(self, method):
        self.scorer = Scorer()

    def test_chance_13264(self):
        dice_set = [1,3,2,6,4]
        score = self.scorer.score(dice_set, 'chance')
        self.assertEqual(score, 16)

    def test_chance_13365(self):
        dice_set = [1,3,3,6,5]
        score = self.scorer.score(dice_set, 'chance')
        self.assertEqual(score, 18)

    def test_yahtzee_66666(self):
        dice_set = [6,6,6,6,6]
        score = self.scorer.score(dice_set, 'yahtzee')
        self.assertEqual(score, 50)

    def test_yahtzee_61666(self):
        dice_set = [6,1,6,6,6]
        score = self.scorer.score(dice_set, 'yahtzee')
        self.assertEqual(score, 0)

    def test_yahtzee_16111(self):
        dice_set = [1,6,1,1,1]
        score = self.scorer.score(dice_set, 'yahtzee')
        self.assertEqual(score, 0)

    def test_yahtzee_11113(self):
        dice_set = [1,1,1,1,3]
        score = self.scorer.score(dice_set, 'yahtzee')
        self.assertEqual(score, 0)

    def test_ones_12131(self):
        dice_set = [1,2,1,3,1]
        score = self.scorer.score(dice_set, 'ones')
        self.assertEqual(score, 3)

    def test_ones_11111(self):
        dice_set = [1,1,1,1,1]
        score = self.scorer.score(dice_set, 'ones')
        self.assertEqual(score, 5)

    def test_ones_22222(self):
        dice_set = [2,2,2,2,2]
        score = self.scorer.score(dice_set, 'ones')
        self.assertEqual(score, 0)

    def test_twos_22222(self):
        dice_set = [2,2,2,2,2]
        score = self.scorer.score(dice_set, 'twos')
        self.assertEqual(score, 10)

    def test_twos_23262(self):
        dice_set = [2,3,2,6,2]
        score = self.scorer.score(dice_set, 'twos')
        self.assertEqual(score, 6)

    def test_threes_23233(self):
        dice_set = [2,3,2,3,3]
        score = self.scorer.score(dice_set, 'threes')
        self.assertEqual(score, 9)

    def test_fours_46524(self):
        dice_set = [4,6,5,2,4]
        score = self.scorer.score(dice_set, 'fours')
        self.assertEqual(score, 8)

    def test_fours_15555(self):
        dice_set = [1,5,5,5,5]
        score = self.scorer.score(dice_set, 'fives')
        self.assertEqual(score, 20)

    def test_fours_66666(self):
        dice_set = [6,6,6,6,6]
        score = self.scorer.score(dice_set, 'sixes')
        self.assertEqual(score, 30)

    def test_pair_66123(self):
        dice_set = [6,6,1,2,3]
        score = self.scorer.score(dice_set, 'pair')
        self.assertEqual(score, 12)

    def test_pair_22134(self):
        dice_set = [2,2,1,3,4]
        score = self.scorer.score(dice_set, 'pair')
        self.assertEqual(score, 4)

    def test_pair_22234(self):
        dice_set = [2,2,2,3,4]
        score = self.scorer.score(dice_set, 'pair')
        self.assertEqual(score, 0)

    def test_pair_22166(self):
        dice_set = [2,2,1,6,6]
        score = self.scorer.score(dice_set, 'pair')
        self.assertEqual(score, 12)

    def test_pair_33331(self):
        dice_set = [3,3,3,3,1]
        score = self.scorer.score(dice_set, 'pair')
        self.assertEqual(score, 0)


    def test_nonsense(self):
        dice_set = [3,2,1,5,1]

        try:
            score = self.scorer.score(dice_set, 'nonsense')
            self.fail('Expecting an exception')
        except NonSupportedRuleException:
            self.assertTrue(True, "the correct type of exception was raised")


