from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class helloUser(RequestHandler):
    def get(self):
        userName = self.get_argument('user')
        self.write("Hello, ")
        self.write(userName)


if __name__ == "__main__":
    handler_mapping = [
                        (r'/$', helloUser),
                        ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
