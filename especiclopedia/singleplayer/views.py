from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from .models import DatabaseVersion, DBSession

from collections import OrderedDict


class VersionView:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='get_version', renderer='json')
    def version_view(request):
        version = DBSession.query(DatabaseVersion).get(1)

        json = OrderedDict([
            ('mode', 'singleplayer'),
            ('version', version.number),
        ])

        return json
