import falcon
from ddtrace import tracer, patch

patch(falcon=True)

class className:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  
        resp.content_type = falcon.MEDIA_TEXT  
        resp.text = ('\nHello World\n')

app = falcon.App()

falcon_app = className()

app.add_route('/falcon_app', falcon_app)
