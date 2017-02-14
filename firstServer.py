from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import os
import socket

 
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() }
        self.write(response)
 
class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                     'name': 'Crazy Game',
                     'release_date': date.today().isoformat() }
        self.write(response)
 
application = tornado.web.Application([
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":
    port = os.environ.get("PORT",7564)
    application.listen(port)    
    tornado.ioloop.IOLoop.instance().start()
    