import tornado.httpserver
import tornado.ioloop
import tornado.web
import json
import db_query

class stamp(tornado.web.RequestHandler):
	def get(self):
		x = client.stampa() 
		self.write(x)		
		testo = self.get_argument('txt')
		self.write(testo)
		client.ricicla(testo)

class execute(tornado.web.RequestHandler):
	def get(self):
		if self.get_argument('cmd')=="read_users":
			rtc=db_query.read_users()
			print "Read users"
			self.write(json.dumps(rtc))
		
application = tornado.web.Application([
	(r"/execute", execute),
	(r"/stamp", stamp),
	(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"}),
])

if __name__ == "__main__":
	application.listen(80,"0.0.0.0")
	tornado.ioloop.IOLoop.instance().start()
