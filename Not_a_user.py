from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
import tkinter as tk
#import backend_main

n=7
class imp():
	def run():
		global n
		dates=[]
		no_of_dates=0
		def example():
			def print_sel():
				global dates,no_of_dates
				no_of_dates=no_of_dates+1
				dates.append(cal.selection_get())
				if(no_of_dates==1):
					dates.append("NULL")
					dates.append("NULL")
					dates.append("NULL")
				elif(no_of_dates==2):
					dates.append("NULL")
					dates.append("NULL")
				elif(no_of_dates==3):
					dates.append("NULL")



			#print(type(cal.selection_get())) 
			#print(cal.selection_get())

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

		def add_dish():
			global n
			drop_list1=OptionMenu(window,l1[n-7],*dish_option)
			drop_list1.grid(row=n,column=2)
			n=n+1
		def submit():
			a=str(cusin_1.get())+str(cusin_2.get())+str(cusin_3.get())+str(cusin_4.get())+str(cusin_5.get())+str(cusin_6.get())
			a=int(a)
			#backend_main.enter_data(new_login.get(),new_password.get(),montly_budget.get(),saving_value.get(),option_1.get(),option_2.get(),option_3.get(),option_4.get(),a,dates[0],dates[1],dates[2],dates[3])
			print(option_1.get())

		window=Tk()
		window.title("New User")

		t1=Label(window,text="New Login ID")
		t1.grid(row=0,column=0)

		new_login=IntVar()
		e1=Entry(window,textvariable=new_login)
		e1.grid(row=0,column=1,columnspan=2)

		t2=Label(window,text="New Password")
		t2.grid(row=1,column=0)

		new_password=StringVar()
		e2=Entry(window,show="*",textvariable=new_password)
		e2.grid(row=1,column=1,columnspan=2)

		t3=Label(window,text="Make a strog Password Using alphabet")
		t3.grid(row=2,column=0)


		t5=Label(window,text="Cuisine")
		t5.grid(row=3,column=0)



		cusin_1=IntVar()
		cusin_2=IntVar()
		cusin_3=IntVar()
		cusin_4=IntVar()
		cusin_5=IntVar()
		cusin_6=IntVar()

		cusin_1.set(0)
		cusin_2.set(0)
		cusin_3.set(0)
		cusin_6.set(0)
		cusin_4.set(0)
		cusin_5.set(0)
		#global cusin_1
		#global cusin_2
		#global cusin_3
		#global cusin_4
		#global cusin_5
		#global cusin_6

		check_cusin_1=Radiobutton(window,text="Italian",variable=cusin_1, value= 1)
		check_cusin_1.grid(row=3,column=1)

		check_cusin_2=Radiobutton(window,text="Chinese",variable=cusin_2,value=2)
		check_cusin_2.grid(row=3,column=2)

		check_cusin_3=Radiobutton(window,text="Indian",variable=cusin_3,value=3)
		check_cusin_3.grid(row=3,column=3)

		check_cusin_4=Radiobutton(window,text="Tandoori",variable=cusin_4,value=4)
		check_cusin_4.grid(row=4,column=1)

		check_cusin_5=Radiobutton(window,text="fast food",variable=cusin_5,value=5)
		check_cusin_5.grid(row=4,column=2)

		check_cusin_6=Radiobutton(window,text="Non Veg",variable=cusin_6,value=6)
		check_cusin_6.grid(row=4,column=3)


		t6=Label(window,text="Montly Buget")
		t6.grid(row=5,column=0)

		montly_budget=IntVar()
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

		saving_value=IntVar()
		e5=Entry(window,textvariable=saving_value)
		e5.grid(row=10,column=1)

		b_final=Button(window,text="Submit",command=submit)
		b_final.grid(row=11,column=1)

		b_final1=Button(window,text="Exit",command=sure)
		b_final1.grid(row=11,column=2)

		window.mainloop()


