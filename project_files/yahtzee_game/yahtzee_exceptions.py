
class WrongNumberOfDiceException(Exception):
    message = "A list of exactly 5 values must be passed in as dice_set"



class NonSupportedRuleException(Exception):
    message = "Please enter a valid ruleset name :)"


class ScoreTypeNotAvailableException(Exception):
    message = "This score type is not currently available to you."

class InvalidScoreException(Exception):
    message = "Score must be an integer."