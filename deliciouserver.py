import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("DeliciouSeret")


class Collector(tornado.web.RequestHandler):
    def get(self):
        # items = ["Item 1", "Item 2", "Item 3"]
        self.render("front/html/collector.html")  # , title="My title", items=items)


class getPair(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return


class postRating(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        return


def make_app():
    return tornado.web.Application([
        (r"/", Collector),
        (r"/getPair", getPair),
        (r"/postRating", postRating),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
