import os
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.options

# application settings and handle mapping info
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Heroku from mivi!")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("main.html", title="Super title", items=items)
        self.render("template.html", title="Super title", items=items)
        
def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()
