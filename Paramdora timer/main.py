from ctypes import alignment
import tkinter as tkn
from tkinter import font
import math
# -----------
# ----------------- CONSTANTS ------------------------------- #
FONT= ('Courier',35,'bold')
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 *60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
timer = None
reps = 1
text_tick = ''
def reset():
    global reps
    global text_tick
    windows.after_cancel(timer)
    canvas.itemconfig(time_text,text = '00:00')
    text_tick = ''
    tick_box.config(text= text_tick)
    label_timer.config(text = 'Timer',fg= GREEN)
    reps= 1
    
    

    



def countdown_mechanic(count):
    global timer
    second = count% 60
    if second < 10:
        second= f'0{second}'
    minutes = math.floor(count/ 60)
    canvas.itemconfig(time_text,text = f'{minutes}:{second}')
    if count > 0:
       timer= windows.after(10,countdown_mechanic,count-1)
    else:
        if reps< 9:
            start_timer()
    
def start_timer():
    global text_tick
    global reps
    if reps%8 == 0:
        label_timer.config(text='Break',fg=RED)
        countdown_mechanic(LONG_BREAK_MIN)
    elif reps % 2 ==0: 
        global text_tick
        text_tick += '✓'
        label_timer.config(text='Break',fg=PINK)
        tick_box.config(text= text_tick)
        countdown_mechanic(SHORT_BREAK_MIN)
    else:
        label_timer.config(text='Work',fg=GREEN)
        countdown_mechanic(WORK_MIN)

    reps += 1
    

        
        
    

windows = tkn.Tk()
windows.title('Pomdero')
windows.config(padx= 100,pady= 50 ,bg= YELLOW)

canvas = tkn.Canvas(width=200,height=224, bg= YELLOW , highlightthickness=0)
photo = tkn.PhotoImage(file = 'tomato.png')
canvas.create_image(100,112,image = photo)
time_text = canvas.create_text(100,130,text='00:00' ,fill='white', font= FONT)
canvas.grid(column=1,row=1)

label_timer = tkn.Label(text='Timer',font=FONT,fg=GREEN,bg=YELLOW)
label_timer.grid(column=1,row=0)

button_start = tkn.Button(text='Start' ,width=10,command=start_timer)
button_start.grid(column=0,row=2)
button_reset = tkn.Button(text='Reset' ,width=10,command=reset)
button_reset.grid(column=2,row=2)

tick_box = tkn.Label(text='', fg=GREEN ,font= FONT,bg=YELLOW)
tick_box.grid(column=1,row=2)


windows.mainloop()




# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #