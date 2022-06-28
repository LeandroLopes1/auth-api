from datetime import datetime
from rest_framework import status
from rest_framework.response import Response

def get_response(
    content=[],
    status=status.HTTP_204_NO_CONTENT,
    timestamp=datetime.now(),
    notifications=None,
    trace_id=""
    ):

    if not notifications:
        notifications = [
            {
                "message": "",
                "propertyName": ""
            }
        ]

    data = {
        'content': content,
        'notifications': notifications,
        'trace_id': trace_id,
        'timestamp': timestamp
    }

    return Response(data, status)
