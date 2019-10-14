from tkinter import *

master = Tk()
var = IntVar()
var.set(2)

def quit_loop():
    print ("Selection:",var.get())
    global selection
    selection = var.get()
    master.quit()

Label(master, text = "Select OCR language").grid(row=0, sticky=W)
Radiobutton(master, text = "default", variable=var, value = 1).grid(row=1, sticky=W)
Radiobutton(master, text = "user-defined", variable=var, value = 2).grid(row=2, sticky=W)
Button(master, text = "OK", command=quit_loop).grid(row=3, sticky=W)

master.mainloop()

if selection == 1:
    print ("My Value is equal to one.")
elif selection == 2:
    print ("My value is equal to two.")