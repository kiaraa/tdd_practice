from project_files.yahtzee_game.non_supported_rule_exception import NonSupportedRuleException


class Scorer(object):

    def score(self, dice_set, score_type):
        if score_type == 'yahtzee':
            return self.score_yahtzee(dice_set)

        if score_type == 'chance':
            return self.score_chance(dice_set)

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

    def all_dice_are_the_same(self, dice_set):
        first_dice = dice_set[0]

        for dice in dice_set:
            if dice != first_dice:
                return False

        return True

