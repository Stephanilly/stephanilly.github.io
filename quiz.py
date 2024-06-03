from quiz_data import question_data
from quiz_brain import QuizBrain, Question

question_bank = []
for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

print("Welcome to the 10-question quiz!")
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
input(f"Your final score was {quiz.score}/{quiz.question_number}")
