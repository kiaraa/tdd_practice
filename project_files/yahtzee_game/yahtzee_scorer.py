from project_files.yahtzee_game.yahtzee_exceptions import *

class Scorer(object):

    def score(self, dice_set, score_type):
        if len(dice_set) != 5:
            raise WrongNumberOfDiceException()

        if score_type == 'yahtzee':
            return self.score_yahtzee(dice_set)

        if score_type == 'chance':
            return self.score_chance(dice_set)

        if score_type == 'ones':
            return self.score_single_number(dice_set, 1)

        if score_type == 'twos':
            return self.score_single_number(dice_set, 2)

        if score_type == 'threes':
            return self.score_single_number(dice_set, 3)

        if score_type == 'fours':
            return self.score_single_number(dice_set, 4)

        if score_type == 'fives':
            return self.score_single_number(dice_set, 5)

        if score_type == 'sixes':
            return self.score_single_number(dice_set, 6)

        if score_type == 'pair':
            return self.score_pair(dice_set)

        if score_type == 'two_pairs':
            return self.score_two_pairs(dice_set)

        if score_type == 'triples':
           return self.score_triples(dice_set)
        
        if score_type == 'quadruples':
           return self.score_quadruples(dice_set)

        if score_type == 'small_straight':
           return self.score_small_straight(dice_set)

        if score_type == 'large_straight':
           return self.score_large_straight(dice_set)

        if score_type == 'full_house':
           return self.score_full_house(dice_set)

        raise NonSupportedRuleException()

    def score_chance(self, dice_set):
        score = 0
        for dice in dice_set:
            score += dice
        return score

    def score_yahtzee(self, dice_set):
        if self.all_dice_are_the_same(dice_set):
            return 50
        else:
            return 0

    def score_single_number(self, dice_set, number_to_score):
        score = 0
        for dice in dice_set:
            if dice == number_to_score:
                score += number_to_score
        return score


    def all_dice_are_the_same(self, dice_set):
        first_dice = dice_set[0]

        for dice in dice_set:
            if dice != first_dice:
                return False

        return True

    def score_pair(self, dice_set):
        pairs_list = []
        for dice in dice_set:
            if self.has_pair(dice, dice_set):
                pairs_list.append(dice)

        if len(pairs_list) != 0:
            return 2 * max(pairs_list)
        else:
            return 0

    def score_two_pairs(self, dice_set):
        pairs_list = []
        for dice in dice_set:
            if self.has_pair(dice, dice_set) and dice not in pairs_list:
                pairs_list.append(dice)

        if len(pairs_list) == 2:
            return 2 * sum(pairs_list)
        else:
            return 0

    def score_triples(self, dice_set):
        for dice in dice_set:
            if self.has_triple(dice, dice_set):
                return 3 * dice
        return 0

    def has_pair(self, dice, dice_set):
        count = self.occurences(dice_set, dice)
        return count == 2

    def has_triple(self, dice, dice_set):
        count = self.occurences(dice_set, dice)
        return count == 3

    def has_quadruple(self, dice, dice_set):
        count = self.occurences(dice_set, dice)
        return count == 4

    def occurences(self, dice_set, dice_to_find):
        counter = 0
        for dice in dice_set:
            if dice == dice_to_find:
                counter += 1
        return counter

    def score_quadruples(self, dice_set):
        for dice in dice_set:
            if self.has_quadruple(dice, dice_set):
                return 4 * dice
        return 0

    def score_small_straight(self, dice_set):
        if all(x in dice_set for x in [1,2,3,4,5]):
            return 15
        else:
            return 0

    def score_large_straight(self, dice_set):
        if all(x in dice_set for x in [2,3,4,5,6]):
            return 20
        else:
            return 0

    def score_full_house(self, dice_set):
        dice_occurances = {}
        pair = 0
        triple = 0
        for dice in [1,2,3,4,5,6]:
            dice_occurances[dice] = self.occurences(dice_set, dice)
        for dice, count in dice_occurances.items():
            if count == 2:
                pair = dice
            if count == 3:
                triple = dice
        if triple != 0 and pair != 0:
            return (triple * 3) + (pair * 2)
        else:
            return 0
