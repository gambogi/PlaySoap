from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=1)
    config.add_route('home', '/')
    config.add_route('tab','/tab')
    config.add_route('login','/login')
    config.add_route('uc','/usercenter')
    config.add_route('lounge','/lounge')
    config.add_route('research','/research')
    config.scan()
    return config.make_wsgi_app()
