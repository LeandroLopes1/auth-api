from rest_framework.response import Response
from rest_framework import status

def get_response(
    content=None,
    status=status.HTTP_204_NO_CONTENT,
    timestamp=None,
    notifications=None,
    trace_id=None
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
