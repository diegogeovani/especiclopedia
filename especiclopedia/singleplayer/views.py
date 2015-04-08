from pyramid.response import Response
from pyramid.view import view_config, view_defaults

class VersionCheckerView:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='check_version')
    def check_version_view(request):
        return Response('<h1>200 HTTP Status')
