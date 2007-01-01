import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", port=3306, db="mydb", user="root", passwd="ariag25")

cur = db.cursor()


def read_users():
	cur.execute("SELECT * FROM users;")
	return cur.fetchall()
		
def read_userCode (i):
	cur.execute("SELECT code FROM users WHERE id=%d;" %i)
	return cur.fetchone()
		
def read_userName (i):
	cur.execute("SELECT name FROM users WHERE id=%d;" %i)
	return cur.fetchone()



#def set_userCode (i, passwd):
i = 1
passwd = 584728
s = "UPDATE users SET code=%d WHERE code=%d;" %(passwd,i) 
s = "SELECT code FROM users WHERE id=1;"
print s
x = cur.execute(s)
rows = cur.fetchall()
for row in rows:
	print row


	
def read_temperatures():
	cur.execute ("SELECT * FROM temperatures;")
	return cur.fetchall()
		
def read_temperature(room):
	cur.execute ("SELECT val FROM temperatures WHERE room=%s;" %room)
	return cur.fetchone()
		
def set_temperature(room, val):
	cur.execute ("UPDATE temperatures SET val=%d WHERE room=%s;" %(val,room))
	
def read_lights():
	cur.execute ("SELECT * FROM lights;")
	return cur.fetchall()

def read_light(room):
	cur.execute ("SELECT status FROM lights WHERE room=%s;" %room)
	return cur.fetchone()
	
def change_light(room, status):
	cur.execute ("UPDATE lights SET status=1 WHERE room=%s;" %room)
	
def read_intrusions():
	cur.execute ("SELECT * FROM intrusions;")
	return cur.fetchall()

def read_intrusion(room):
	cur.execute ("SELECT status FROM intrusions WHERE room=%s;" %room)
	return cur.fetchone()
	
def change_intrusion(room, status):
	cur.execute ("UPDATE intrusions SET status=1 WHERE room=%s;" %room)







