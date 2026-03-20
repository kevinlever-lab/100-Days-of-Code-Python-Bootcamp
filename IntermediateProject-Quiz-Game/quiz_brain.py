class QuizBrain:
    """
    Manages the logic and flow of a true/false quiz game.
    Tracks the current question number, the player's score, and the
    list of questions. Controls question progression, answer validation,
    and determines when the quiz has ended.

    """
    def __init__(self, q_list):
        """
        Initializes the QuizBrain with a list of questions.
        Args:
            q_list (list): A list of Question objects to be used in the quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # Check users answers
    def check_answer(self, user_answer, correct_answer):
        """
        Compares the player's answer to the correct answer and updates
        the score accordingly.

        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print() # print blank line to separate questions

    # Method to retrieve the item at the current question_number from question_list
    def next_question(self):
        """
        Retrieves the next question from the question list, prompts the
        player for a true/false answer, and passes the response to
        check_answer() for validation.

        """
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # Determine if the quiz has ended
    def still_has_questions(self):
        """
        Checks whether there are remaining questions in the quiz.
        If all questions have been answered, prints the completion message
        and the player's final score.

        """
        num_questions = len(self.question_list)
        if self.question_number < num_questions:
            return True
        else:
            print("You have completed the quiz.")
            print(f"Your total score was: {self.score}/{self.question_number}")
            return False

