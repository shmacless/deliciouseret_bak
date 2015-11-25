import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("DeliciouSeret")


class Collector(tornado.web.RequestHandler):
    def get(self):
        # items = ["Item 1", "Item 2", "Item 3"]
        self.render("front/html/collector.html")  # , title="My title", items=items)


def make_app():
    return tornado.web.Application([
        (r"/", Collector),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
