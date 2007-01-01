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

def set_userCode (i, code):
	cur.execute("UPDATE users SET code=%d WHERE id=%d;" %(code,i))
	db.commit()
	
def read_temperatures():
	cur.execute ("SELECT * FROM temperatures;")
	return cur.fetchall()
		
def read_temperature(room):
	cur.execute ("SELECT val FROM temperatures WHERE room=%s;" %room)
	return cur.fetchone()
		
def set_temperature(room, val):
	cur.execute ("UPDATE temperatures SET val=%d WHERE room=%s;" %(val,room))
	db.commit()
	
def read_lights():
	cur.execute ("SELECT * FROM lights;")
	return cur.fetchall()

def read_light(room):
	cur.execute ("SELECT status FROM lights WHERE room=%s;" %room)
	return cur.fetchone()
	
def change_light(room):
	i = read_intrusion(room)
	if i == 0:
		i = 1
	elif i == 1
		i = 0
	cur.execute ("UPDATE lights SET status=%d WHERE room=%s;" %(i,room))
	db.commit()
	
def read_intrusions():
	cur.execute ("SELECT * FROM intrusions;")
	return cur.fetchall()

def read_intrusion(room):
	cur.execute ("SELECT status FROM intrusions WHERE room=%s;" %room)
	return cur.fetchone()
	
def change_intrusion(room):
	i = read_intrusion(room)
	if i == 0:
		i = 1
	elif i == 1
		i = 0
	cur.execute ("UPDATE intrusions SET status=%d WHERE room=%s;" %(i,room))
	db.commit()
