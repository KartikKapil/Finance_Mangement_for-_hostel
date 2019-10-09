from tkinter import * 
from tkinter.ttk import * 
from Not_a_user import *
import os

def create_new_user():
	main()


def exit_pro():
	sys.exit()



window=Tk()
window.title("Welcome")

t1=Label(window,text="login")
t1.grid(row=0,column=0)

t2=Label(window,text="password")
t2.grid(row=1,column=0)

login_id=StringVar()
e1=Entry(window,textvariable=login_id)
e1.grid(row=0,column=1,columnspan=30)


pass_id=StringVar()
e2=Entry(window,show="*",textvariable=pass_id)
e2.grid(row=1,column=1,columnspan=30)


b1=Button(window,text="NOT A USER",command=create_new_user)
b1.grid(row=2,column=0)

b2=Button(window,text="Login")
b2.grid(row=2,column=1)

b3=Button(window,text="exit",command=exit_pro)
b3.grid(row=2,column=2)

window.mainloop()
