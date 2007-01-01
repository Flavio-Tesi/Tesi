import tornado.httpserver
import tornado.ioloop
import tornado.web
import client
import db_query

class stamp(tornado.web.RequestHandler):
	def get(self):
		x = client.stampa() 
		self.write(x)		
		testo = self.get_argument('txt')
		self.write(testo)
		client.ricicla(testo)
		

application = tornado.web.Application([
	(r"/stamp", stamp),
	(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"}),
])

if __name__ == "__main__":
	application.listen(80,"0.0.0.0")
	tornado.ioloop.IOLoop.instance().start()
