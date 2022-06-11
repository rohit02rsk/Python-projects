
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(q_list=question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
