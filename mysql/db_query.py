import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", port=3306, db="mydb", user="root", passwd="ariag25")

cur = db.cursor()

def leggiUsers():

	cur.execute("SELECT * FROM users;")
	rows = cur.fetchall()
	for row in rows:
		print row
		
def return_PWD (i):
	cur.execute("SELECT code FROM users WHERE id=%d;" %i)
	rows = cur.fetchall()
	for row in rows:
		return row[0]

#def modificaPassword (i, passwd):
i = 1
passwd = 584728
s = "UPDATE users SET code=%d WHERE code=%d;" %(passwd,i) 
s = "SELECT code FROM users WHERE id=1;"
print s
x = cur.execute(s)
rows = cur.fetchall()
for row in rows:
	print row
