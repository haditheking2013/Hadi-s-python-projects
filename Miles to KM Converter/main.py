from cProfile import label
import tkinter


windows = tkinter.Tk()

windows.title('Miles to KM Converter')
windows.minsize()
windows.config(padx=20,pady=20)

my_label = tkinter.Label(text='Miles', font=('Arial',15,'bold'))
my_label.grid(column=2,row=0)


input_1 = tkinter.Entry(width=10)
input_1.grid(column=1,row=0)

my_label_2 = tkinter.Label(text='is equal to', font=('Arial',15,'bold'))
my_label_2.grid(column=0,row=1)

def button_pressed():
    my_label_3['text'] = str(round(float(input_1.get()) * 1.60934,2))

button_1 = tkinter.Button(text = 'Show result', command=button_pressed)
button_1.grid(column=1,row=2)

my_label_3 = tkinter.Label(text='', font=('Arial',15,'bold'))
my_label_3.grid(column=1, row=1)

my_label_4 = tkinter.Label(text='KM', font=('Arial',15,'bold'))
my_label_4.grid(column=2,row=1)



windows.mainloop()