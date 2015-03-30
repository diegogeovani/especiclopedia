from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='root')
def root_view(request):
    return Response('<h1>Backend do aplicativo Especificidade')

@view_config(route_name='singleplayer')
def singleplayer_view(request):
    return Response('<h1>Backend do aplicativo Especificidade')

# /howdy?name=alice which links to the next view
@view_config(route_name='hello')
def hello_view(request):
    name = request.params.get('name', 'No Name')
    body = '<p>Hi %s, this <a href="/goto">redirects</a></p>'
    return Response(body % name)

# /goto which issues HTTP redirect to the last view
@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")

# /problem which causes an site error
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()
