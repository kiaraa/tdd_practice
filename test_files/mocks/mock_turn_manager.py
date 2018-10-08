class MockTurnManager:

    def __init__(self):
        self.number_of_times_take_a_turn_was_called = 0
        self.parameters_for_take_a_turn = []

    def number_of_turns_taken(self):
        return self.number_of_times_take_a_turn_was_called

    def take_a_turn(self, scorecard):
        self.number_of_times_take_a_turn_was_called += 1
        self.parameters_for_take_a_turn.append(scorecard)
        scorecard.score_a_turn(1, scorecard.available_score_types[0])

    def get_turn_parameters(self):
        return self.parameters_for_take_a_turn