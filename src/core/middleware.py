from datetime import datetime
from xml.dom.minidom import TypeInfo
from django.utils.deprecation import MiddlewareMixin

class TesteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = datetime.now()