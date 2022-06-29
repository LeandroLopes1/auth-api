import json
from django import http
from datetime import datetime
from django.conf import settings
from ..utils.response_utils import get_response
from django.utils.deprecation import MiddlewareMixin
from djangorestframework_camel_case.render import camelize

class ResponseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = datetime.now()

    def process_response(self, request, response):
        debug = settings.DEBUG

        if response.status_code == 404:
            if debug:
                return http.HttpResponse(
                    "<h1>404 Not Found</h1>",
                    status = 404,
                    content_type="text/html"
                )

            return response

        response.content = json.dumps(
            camelize(get_response(request, response)),
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        )
        return response

    def process_exception(self, request, exception):
        request.trace = exception.args
