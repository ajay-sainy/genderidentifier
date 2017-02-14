from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import sqlite3 as sqlite
import tornado.web
import os
from genderPredictor import genderPredictor

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print ("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        
    def get(self,name):
        print(name)
        self.set_header("Access-Control-Allow-Origin", "*")
        gp = genderPredictor()        
        self.write(gp.predict(name))

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/([^/]+)", MainHandler),            
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    
    app = Application()
    port = os.environ.get("PORT",7531)
    app.listen(port)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()