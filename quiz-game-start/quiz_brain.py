


class BrainQuiz:


    def __init__(self,q_list):
            self.question_number = 0
            self.q_list = q_list 
            self.score = 0
            
    def next_method(self):
             print(f'Your score is {str(self.question_number)}')
             x = input(f'Q{self.question_number+1}: {self.q_list[self.question_number].question} (True/False)?')
             
             self.check_answer(x,self.q_list[self.question_number].answer)
             self.question_number += 1
            
    def still_questions(self):
        return self.question_number < len(self.q_list)

    def check_answer(self,quest_answer,answer):

        if quest_answer.lower() == answer.lower():
            print('Thats correct')
            self.score += 1
        else:
            print('Fail')
            print(f'THe answer was {answer}')
        
            










    
