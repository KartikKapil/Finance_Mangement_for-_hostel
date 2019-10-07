from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
import tkinter as tk

def example():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(window)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def sure():
	sys.exit()


def add_date():
	
	b1=ttk.Button(window, text='Select Date ', command=example)
	b1.grid(row=6,column=1)

n=7
def add_dish():
	global n
	drop_list1=OptionMenu(window,l1[n-7],*dish_option)
	drop_list1.grid(row=n,column=2)
	n=n+1





window=Tk()
window.title("New User")

t1=Label(window,text="New Login ID")
t1.grid(row=0,column=0)

new_login=StringVar()
e1=Entry(window,textvariable=new_login)
e1.grid(row=0,column=1,columnspan=2)

t2=Label(window,text="New Password")
t2.grid(row=1,column=0)

new_password=StringVar()
e2=Entry(window,show="*",textvariable=new_password)
e2.grid(row=1,column=1,columnspan=2)

t3=Label(window,text="Retype Password")
t3.grid(row=2,column=0)

retype_password=StringVar()
e3=Entry(window,show="*",textvariable=retype_password)
e3.grid(row=2,column=1,columnspan=2)

if(retype_password==new_password):
	t4=Label(window,text="Matches prefectly")
	t4.grid(row=2,column=3)
else:
	t4=Label(window,text="Does Not Match")
	t4.grid(row=2,column=3)

t5=Label(window,text="Cuisine")
t5.grid(row=3,column=0)

cusin_1=IntVar()
check_cusin_1=Checkbutton(window,text="Italian",variable=cusin_1)
check_cusin_1.grid(row=3,column=1)

cusin_2=IntVar()
check_cusin_2=Checkbutton(window,text="Chinese",variable=cusin_2)
check_cusin_2.grid(row=3,column=2)

cusin_3=IntVar()
check_cusin_3=Checkbutton(window,text="Indian",variable=cusin_3)
check_cusin_3.grid(row=3,column=3)

cusin_4=IntVar()
check_cusin_4=Checkbutton(window,text="Tandoori",variable=cusin_4)
check_cusin_4.grid(row=4,column=1)

cusin_5=IntVar()
check_cusin_5=Checkbutton(window,text="Non Veg",variable=cusin_5)
check_cusin_5.grid(row=4,column=2)

cusin_6=IntVar()
check_cusin_6=Checkbutton(window,text="Tandoori",variable=cusin_6)
check_cusin_6.grid(row=4,column=3)

t6=Label(window,text="Montly Buget")
t6.grid(row=5,column=0)

montly_budget=StringVar()
e4=Entry(window,textvariable=montly_budget)
e4.grid(row=5,column=1,columnspan=2)

t7=Label(window,text="Select the Date ")
t7.grid(row=6,column=0)

b0=Button(window,text="ADD Date",command=add_date)#changes to be made here 
b0.grid(row=6,column=1)



t8=Label(window,text="Non prefarable dishes")
t8.grid(row=7,column=0)

dish_option=["Bread Pakoda","Bread jam","Dahi ke aloo","Dal tadka","Rice","Veg chowmien","Manchurian",
"Fried rice","Aloo tamatar","Mix veg parantha","Mutter paneer","Masoor dal","Raita","Gutta curry","Rajma"
,"Aloo sandwich","Veg kofta","Arhar dal","Choley","Aloo masala dry","Shimla mirch aloo","Kadhi pakoda"
,"Dal darbari","Coleslaw sandwich","Boiled egg","Veg keema","Chana dal","Mutter kulcha","Mix veg","Dal makhani"
,"Malai kofta","Paw bhaji","Kashmiri Dum aloo","Veg biryani","Uttapam","Paneer makhani","Egg curry","Palak paneer"
,"Panchratan dal","Navratan dal","Arhar dal","Moong dal"]

b2=Button(window,text="Add Non Prefarable Dishes",command=add_dish)
b2.grid(row=7,column=1)


option_1=StringVar()
option_1.set("Please choose first option")

#drop_list1=OptionMenu(window,option_1,*dish_option)
#drop_list1.grid(row=7,column=1)

option_2=StringVar()
option_2.set("Please choose second option")


#drop_list2=OptionMenu(window,option_2,*dish_option)
#drop_list2.grid(row=7,column=2)

t9=Label(window,text="Maxium of 4 dishes")
t9.grid(row=7,column=3)

option_3=StringVar()
option_3.set("Please choose third option")

#drop_list3=OptionMenu(window,option_3,*dish_option)
#drop_list3.grid(row=8,column=1)

option_4=StringVar()
option_4.set("Please choose fourth option")

l1=[option_1,option_2,option_3,option_4]

#drop_list4=OptionMenu(window,option_4,*dish_option)

#drop_list4.grid(row=8,column=2)

t10=Label(window,text="Amount You want save")
t10.grid(row=10,column=0)

saving_value=StringVar()
e5=Entry(window,textvariable=saving_value)
e5.grid(row=10,column=1)

b_final=Button(window,text="Submit")
b_final.grid(row=11,column=1)

b_final1=Button(window,text="Exit",command=sure)
b_final1.grid(row=11,column=2)

window.mainloop()