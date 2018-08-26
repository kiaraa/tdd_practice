from project_files.yahtzee_game.yahtzee_exceptions import ScoreTypeNotAvailableException, InvalidScoreException


class Scorecard:

    def __init__(self):
        self.total_score = 0
        self.available_score_types = ['yahtzee',
                                      'chance',
                                      'ones',
                                      'twos',
                                      'threes',
                                      'fours',
                                      'fives',
                                      'sixes',
                                      'pair',
                                      'two_pairs',
                                      'triples',
                                      'quadruples',
                                      'small_straight',
                                      'large_straight',
                                      'full_house']

    def get_total_score(self):
        return self.total_score

    def score_a_turn(self, turn_score, score_type):
        self.check_for_bad_input(score_type, turn_score)

        self.available_score_types.remove(score_type)
        self.total_score += turn_score

    def get_available_score_types(self):
        return self.available_score_types

    def check_for_bad_input(self, score_type, turn_score):
        if score_type not in self.available_score_types:
            raise ScoreTypeNotAvailableException()
        if not isinstance(turn_score, int) or turn_score < 0:
            raise InvalidScoreException()
