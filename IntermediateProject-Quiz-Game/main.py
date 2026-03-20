
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""
Quiz Brain - Main Entry Point

A command-line quiz game that presents true/false questions to the player
and tracks their score throughout the game.

Process:
    1. Imports question data from the `data` module and creates a list of
       `Question` objects, each containing a question and its correct answer.
    2. Passes the question bank to a `QuizBrain` object which manages the
       quiz logic and score tracking.
    3. Continuously presents questions to the player using `next_question()`
       until all questions in the bank have been answered.
    4. Displays the player's running score after each question.
    5. Announces the final score when all questions have been completed.

Dependencies:
    question_model.Question: Provides the Question class used to create
                             individual question objects with a question
                             text and correct answer.
    data.question_data:      Provides the raw question data as a list of
                             dictionaries, each containing a question and
                             its correct answer.
    quiz_brain.QuizBrain:    Manages the quiz flow, tracks the current
                             question, checks for remaining questions via
                             still_has_questions(), and presents each
                             question via next_question().
"""




# define empty list of question objects
question_bank = []

# Add question objects to the list
for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

# create a new QuizBrain object and pass in the question_bank list of questions
quiz = QuizBrain(question_bank)

# Loop through all the questions in the quiz
while quiz.still_has_questions():
    quiz.next_question()




