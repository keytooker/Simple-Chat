import os
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.options

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Heroku from mivi!")
        
def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()
