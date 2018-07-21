from project_files.yahtzee_game.non_supported_rule_exception import NonSupportedRuleException


class Scorer(object):

    def score(self, dice_set, score_type):
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

        raise NonSupportedRuleException


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
            if self.hasPair(dice, dice_set):
                pairs_list.append(dice)

        if len(pairs_list) != 0:
            return 2 * max(pairs_list)
        else:
            return 0

    def hasPair(self, dice, dice_set):
        count = self.occurences(dice_set, dice)
        return count == 2

    def occurences(self, dice_set, dice_to_find):
        counter = 0
        for dice in dice_set:
            if dice == dice_to_find:
                counter += 1
        return counter


