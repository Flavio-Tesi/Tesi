import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", port=3306, db="mydb", user="root", passwd="V&F")

cur = db.cursor()

def leggiUsers():

	cur.execute("SELECT * FROM users;")

	rows = cur.fetchall()

	for row in rows:
		print row

#def modificaPassword (i, passwd):
i = 1
passwd = 584728
s = "UPDATE users SET code=%d WHERE id=%d;" %(passwd,i) 
s = "SELECT * FROM users;"
print s
x = cur.execute(s)
rows = cur.fetchall()
for row in rows:
	print row
	
