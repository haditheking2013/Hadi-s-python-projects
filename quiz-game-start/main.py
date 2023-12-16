from data import question_data
from question_model import Questions
from quiz_brain import BrainQuiz



question_list = []
for quest in question_data:
    question_list.append(Questions(quest['text'],quest['answer']))


quiz = BrainQuiz(question_list)
while quiz.still_questions():
         quiz.next_method()

print('you scored ',quiz.score)

