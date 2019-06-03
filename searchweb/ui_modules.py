
import tornado

class Card(tornado.web.UIModule):
    def render(self, **kwargs):
        return self.render_string('_card.html',
            **kwargs
        )


class Uploader(tornado.web.UIModule):
    def render(self, **kwargs):
        return self.render_string('_uploader.html',
            **kwargs
        )


class Bar(tornado.web.UIModule):
    def render(self, **kwargs):
        return self.render_string('_bar.html',
            **kwargs
        )


class Charjs(tornado.web.UIModule):
    def render(self,type='horizontalBar', **kwargs):
        return self.render_string('_charjs.html',
            type='horizontalBar',
            **kwargs
        )



class Textcard(tornado.web.UIModule):
    def render(self, **kwargs):
        if 'title' not in kwargs:
            kwargs['title'] = 'No title'
        return self.render_string('_textcard.html', 
            **kwargs
        )

