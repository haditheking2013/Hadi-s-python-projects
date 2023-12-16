from cgitb import text
import tkinter
from turtle import bgcolor, color, shapesize
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"




class QuizInterface:
    
    def __init__(self,quiz_object :QuizBrain):
        self.score = 0
        self.quiz_object = quiz_object
        self.windows = tkinter.Tk()
        self.windows.title('Quizler')
        self.windows.configure(background=THEME_COLOR,padx=20)
        self.canvas = tkinter.Canvas(self.windows,height=250,width=300,bg='white')
        self.question_text = self.canvas.create_text(150,125,text='hey its hadi',font=('Arial',20,'italic'),fill=THEME_COLOR,width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.labelScore = tkinter.Label(text='score: 0',bg=THEME_COLOR,fg='white',font=('Arial',20,'italic'))
        self.labelScore.grid(column=1,row=0,padx=20,pady=20)
        self.image1 = tkinter.PhotoImage(file='images/true.png')
        self.buttonYes = tkinter.Button(self.windows,image=self.image1,highlightthickness=0,borderwidth=0,command=self.check_answer_true)
        self.buttonYes.grid(column=0,row=2,padx=20,pady=20)

        self.image2 = tkinter.PhotoImage(file='images/false.png')
        self.buttonNo = tkinter.Button(self.windows,image=self.image2,highlightthickness=0,borderwidth=0,command=self.check_answer_false)
        self.buttonNo.grid(column=1,row=2,padx=20,pady=20)
        self.get_next_question()
        self.windows.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_object.still_has_questions():
           q_text =  self.quiz_object.next_question()
           self.canvas.itemconfig(self.question_text,text=q_text)
           self.canvas.config(bg='white')
        else:
            self.canvas.itemconfig(self.question_text, text = f'You are done you scored {self.score}')
            self.buttonNo.config(state='disabled')
            self.buttonYes.config(state='disabled')

           
        

    def check_answer_true(self):
         if self.quiz_object.check_answer('True'):
            self.score +=1 
            self.labelScore.config(text=f'score: {self.score}')
            self.give_feedback_right()
            self.windows.after(1000,self.get_next_question)
         else:
            self.give_feedback_wrong()
            self.windows.after(1000,self.get_next_question)
         

     

    def check_answer_false(self):
        if self.quiz_object.check_answer('False'):
            self.score +=1 
            self.labelScore.config(text=f'score: {self.score}')
            self.give_feedback_right()
            self.windows.after(1000,self.get_next_question)
        else:
            self.give_feedback_wrong()
            self.windows.after(1000,self.get_next_question)
        

    def give_feedback_right(self):
        self.canvas.config(bg='green')

    def give_feedback_wrong(self):
        self.canvas.config(bg='red')
        
    


        


