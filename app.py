from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def _start_wsgi_server(app):
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

if __name__ == '__main__':
    config = Configurator()
    config.add_route('root', '/')
    config.add_route('singleplayer', '/singleplayer')
    config.add_route('hello', '/howdy')
    config.add_route('redirect', '/goto')
    config.add_route('exception', '/problem')
    config.scan('views')

    # represents a Pyramid application ready to be lauched
    app = config.make_wsgi_app()
    _start_wsgi_server(app)
