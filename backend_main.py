import sqlite3
from pandas import *

def connect():
	conn=sqlite3.connect("Main_database.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS info(login_id INT PRIMARY KEY,password VARCHAR(30),amout_monthly INT,saving_monthly INT DEFAULT 0,date_of_event_1 DATE DEFAULT NULL,date_of_event_2 DATE DEFAULT NULL,date_of_event_3 DATE DEFAULT NULL ,date_of_event_4 DATE DEFAULT NULL,dislike_1 VARCHAR(30),dislike_2 VARCHAR(30) ,dislike_3 VARCHAR(30),dislike_4 VARCHAR(30),cuisine INT)")
	conn.commit()
	conn.close()

connect()

def enter_data(login_id,password,amout_monthly,saving_monthly,dislike_1,dislike_2,dislike_3,dislike_4,cuisine,date_of_event_1,date_of_event_2,date_of_event_3,date_of_event_4):

	conn=sqlite3.connect("Main_database.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO info VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(login_id,password,amout_monthly,saving_monthly,date_of_event_1,date_of_event_2,date_of_event_3,date_of_event_4,dislike_1,dislike_2,dislike_3,dislike_4,cuisine))
	conn.commit()
	conn.close()


def auth_main(login_id,password):
	conn=sqlite3.connect("Main_database.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM info WHERE login_id=? and password=?",(login_id,password))
	#print(cur.execute("SELECT * FROM info WHERE login_id=? and password=?",(login_id,password)))
	if cur.fetchone() is not None:
		return 1;#if is welcome
	else :
		print("login failed") 
	conn.commit()
	conn.close()

mon_amo=0
mon_sav=0
doe1=None
doe2=None
doe3=None
doe4=None
dislike1=None
dislike2=None
dislike3=None 
dislike4=None
cusi1=None
def save_main(login_id,password):
	global mon_amo,mon_sav,doe1,doe2,doe3,doe4,dislike1,dislike2,dislike3,dislike4,cusi1
	conn=sqlite3.connect("Main_database.db")
	cur=conn.cursor()
	for row in cur.execute("SELECT * FROM info WHERE login_id=? and password=?",(login_id,password)):
		mon_amo=row[2]
		mon_sav=row[3]
		doe1=row[4]
		doe2=row[5]
		doe3=row[6]
		doe4=row[7]
		dislike1=row[8]
		dislike2=row[9]
		dislike3=row[10]
		dislike4=row[11]
		cusi1=row[12]
	conn.commit()
	conn.close()

actual_date=[]

mon_amo=mon_amo-mon_sav
def cal_date(dislike):
	#mon_amo=(mon_amo-mon_sav)
	data=pandas.read_csv("food.csv")
	#data=data.set_index('Day')
	ber=[]
	count=0
	a=""
	global actual_date
	#print(data.loc[:,"Breakfast"])
	for j in range(0,7):
		for i in data.loc[:,"Breakfast"][j]:
			if(i==","):
				if(a==dislike):
					count=count+1
				

				ber.append(a)
				a=""
				continue
			a=a+i
	#print(count)
	for k in range(0,(count+1)):
		if(k==count):
			actual_date=list(data.loc[k,"Day"])

	to_check_date=""
	for t in actual_date:
		if((ord(t)>=48) and (ord(t)<=57)):
			to_check_date=to_check_date+t
		if(t=="."):
			to_check_date=to_check_date+"-"

	

##########################################for breakfast ends here 
	count=0
	lunch=[]
	for j in range(0,7):
		for i in data.loc[:,"Lunch"][j]:
			if(i==","):
				if(a==dislike):
					count=count+1
				

				lunch.append(a)
				a=""
				continue
			a=a+i
	for k in range(0,(count+1)):
		if(k==count):
			actual_date=list(data.loc[k,"Day"])

	to_check_date=""
	for t in actual_date:
		if((ord(t)>=48) and (ord(t)<=57)):
			to_check_date=to_check_date+t
		if(t=="."):
			to_check_date=to_check_date+"-"

	
#############################################################for lunch ends here
	count=0
	dinner=[]
	for j in range(0,7):
		for i in data.loc[:,"Dinner"][j]:
			if(i==","):
				if(a==dislike):
					count=count+1

				dinner.append(a)
				a=""
			a=a+i
	for k in range(0,(count+1)):
		if(k==count):
			actual_date=list(data.loc[k,"Day"])

	to_check_date=""
	for t in actual_date:
		if((ord(t)>=48) and (ord(t)<=57)):
			to_check_date=to_check_date+t
		if(t=="."):
			to_check_date=to_check_date+"-"

	return(to_check_date)


def cal_main():
	global doe1,doe2,doe4,doe3
	to_check_date=cal_date()
	if ((to_check_date==doe1) or (to_check_date==doe2) or (to_check_date==doe3) or (to_check_date==doe4)):
		mon_amo=mon_amo-800
		budget_allocated=800
		return budget_allocated
	











