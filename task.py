from tkinter import *
from tkinter import messagebox
from datetime import date, datetime
from tkcalendar import Calendar
import os

root = Tk()
root.title('Task managment')
root.config(bg='223441')
root.resizable(width=False, height=False)



left_frame = Frame(root, bg='#223441', width=400, height=500)
right_frame = Frame(root, bg='#223441', width=400, height=500)


left_frame.grid(row=0, column=0, pady = 20, padx = 20)
right_frame.grid(row=0, column=1, pady = 20, padx = 20)


lb = Listbox(
    left_frame,
    width=25,
    height=15,
    borderwidth=0,
    selectmode=SINGLE,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"
)
lb.grid(row=0, column=0)

input_field = Entry(
    right_frame,
    font=('times', 15),
    width=25
)

input_field.grid(row=0, column=0, sticky=W, pady=5)

cal = Calendar(right_frame, selectmode = 'day')
cal.grid(row=1, column=0, sticky=W, pady=5)

today = date.today()



def newTask():
    filesize = os.path.getsize('tasks.txt')
    task_name = input_field.get()
    if task_name !="":
        lb.insert(END, task_name)
        input_field.delete(0, "end")
        with open('tasks.txt', 'a') as file:
            if filesize == 0:
                file.write(task_name + ',' + cal.get_date())
            else:
                file.write('\n' + task_name + ',' + cal.get_date())
    else:
        messagebox.showwarning("warning", "Please enter a task.")
                     
                           



    
