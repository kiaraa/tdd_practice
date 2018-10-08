import copy

class MockVictoryDeclarer:

    def __init__(self):
        self.maxDiff = None
        self.was_declare_victor_called = False
        self.passed_scorecards = []
        self.winner_name = ""

    def declare_victor(self, list_of_scorecards):
        self.was_declare_victor_called = True
        self.passed_scorecards = copy.deepcopy(list_of_scorecards)
        return self.winner_name

    def get_declare_victor_was_called(self):
        return self.was_declare_victor_called

    def get_passed_scorecards(self):
        return self.passed_scorecards

    def set_the_winner(self, winner_name):
        self.winner_name = winner_name

    def was_called_after_scorecards_have_been_updated(self):
        return len(self.passed_scorecards[0].available_score_types) == 0
