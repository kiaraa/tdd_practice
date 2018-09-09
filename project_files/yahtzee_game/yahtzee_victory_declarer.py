from project_files.yahtzee_game.yahtzee_scorecard import Scorecard


# noinspection PyMethodMayBeStatic
class VictoryDeclarer:

    def declare_victor(self, scorecards):
        highest_scorecards = self.find_highest_scorecards(scorecards)
        return self.build_victor_string(highest_scorecards)

    def find_highest_scorecards(self, scorecards):
        nobody = Scorecard(player_name="nobody")
        highest_scorecards = [nobody]

        for scorecard in scorecards:
            if scorecard.total_score > highest_scorecards[0].total_score:
                highest_scorecards = [scorecard]

            elif scorecard.total_score == highest_scorecards[0].total_score:
                highest_scorecards.append(scorecard)

        if nobody in highest_scorecards:
            highest_scorecards.remove(nobody)

        return highest_scorecards

    def build_victor_string(self, highest_scorecards):
        victors = highest_scorecards[0].player_name
        for i in range(1, len(highest_scorecards)):
            victors += " and " + highest_scorecards[i].player_name
        return victors

