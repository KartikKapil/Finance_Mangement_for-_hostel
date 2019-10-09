import sqlite3

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
def cal_main(login_id,password):
	global mon_amo,mon_sav,doe1
	conn=sqlite3.connect("Main_database.db")
	cur=conn.cursor()
	for row in cur.execute("SELECT * FROM info WHERE login_id=? and password=?",(login_id,password)):
		mon_amo=row[2]
		mon_sav=row[3]
		doe1=row[4]
		doe2=row[5]
		doe3=row[6]
		doe4=row[7]
		

	

	conn.commit()
	conn.close()

cal_main(19103246,"kapil@343")






















								