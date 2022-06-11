from multiprocessing import reduction


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"\n\nQ{self.question_number}. {curr_question.text} (True/False): ")
        self.check_answer(user_ans, curr_question.answer)
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect..")
        print(f"The correct answer was: {corr_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
