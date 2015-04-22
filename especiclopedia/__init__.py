from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from singleplayer.models import DBSession, Base


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
            root_factory='especiclopedia.models.Root')
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('get_version', '/singleplayer/version')
    config.scan()
    return config.make_wsgi_app()
