from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

class TesteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = datetime.now()