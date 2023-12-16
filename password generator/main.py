from cgitb import text
import tkinter
from tkinter import messagebox
import json

def search():
    try:
        with open('json_data.json') as file:
            data = json.load(file)
            print(data[entry_website.get()])
    except FileNotFoundError:
        messagebox.showinfo(title ='OOPS!!', message='save before you search on!')
    except KeyError:
        messagebox.showinfo(title='key not found',message='no information found for this website')
    else:
        messagebox.showinfo(title='information',message= f"email: {data[entry_website.get()]['email']}\n password: {data[entry_website.get()]['password']}")
        
        




def save():
    if len(entry_password.get()) ==0 or len(entry_website.get()) ==0:
        messagebox.showinfo(title ='opps', message='dont leave the fields empty dummy')
    

    else:
         json_data = {entry_website.get():
                             {'email': entry_username.get(),
                                  'password': entry_password.get()
            }
         }
         try:
             with open('json_data.json') as file:
                pass
         except FileNotFoundError:
            with open('json_data.json','w') as file:
                json.dump(json_data,file , indent=4)

         else:
            with open('json_data.json') as file:
              data = json.load(file)
              data.update(json_data)
            with open('json_data.json','w') as file:
                json.dump(data,file,indent=4)
         finally:
            entry_website.delete(0,'end')
            entry_password.delete(0,'end')

window = tkinter.Tk()
window.title('Password generator')
window.config(padx=20,pady=20)


canvas = tkinter.Canvas(width=200,height=200)
image = tkinter.PhotoImage(file ='logo.png')
canvas.create_image(100,100,image = image)
canvas.grid(column= 1,row=0)
website_name_label = tkinter.Label(text='Website:',font=('Arial',13,'italic'))
website_name_label.grid(column=0,row=1)

entry_website = website_name_entry = tkinter.Entry(width=21)
website_name_entry.grid(column=1,row=1)
website_name_entry.focus()


website_name_username= tkinter.Label(text='Username/Email:',font=('Arial',13,'italic'))
website_name_username.grid(column=0,row=2)

entry_username = username_name_entry = tkinter.Entry(width=35)
username_name_entry.grid(column=1,row=2 ,columnspan=2)
username_name_entry.insert(0,'haditheking2013@gmail.com')





website_name_password= tkinter.Label(text='Password:',font=('Arial',13,'italic'))
website_name_password.grid(column=0,row=3)

entry_password = password_name_entry = tkinter.Entry(width=21)
password_name_entry.grid(column=1,row=3)


generate_button = tkinter.Button(width=10, text= 'Generate')
generate_button.grid(column= 2,row = 3)

button_add = tkinter.Button(text='Add' ,width=36 , command=save)
button_add.grid(column=1,row=4, columnspan=2)



button_add = tkinter.Button(text='Search' ,width=12 , command=search)
button_add.grid(column=2,row=1)









window.mainloop()
