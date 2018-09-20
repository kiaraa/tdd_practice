class MockUI:

    def __init__(self):
        self.list_of_displayed_messages = []
        self.list_of_questions= []
        self.user_response = None
        self.all_output_to_user = []

    def display(self, message):
        self.list_of_displayed_messages.append(message)
        self.all_output_to_user.append(message)

    def check_if_message_was_displayed(self, message):
        if message in self.list_of_displayed_messages:
            return True
        else:
            return False

    def ask_user(self, message):
        self.list_of_questions.append(message)
        self.all_output_to_user.append(message)
        return self.user_response

    def set_test_response(self, response):
        self.user_response = response

    def last_question_to_user(self):
        return self.list_of_questions[-1]

    def get_all_output_to_user(self):
        return self.all_output_to_user

    def get_last_output_to_user(self):
        return self.all_output_to_user[-1]