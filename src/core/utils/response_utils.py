def get_response(
    request,
    response,
    ):
    notifications = []

    if hasattr(request, 'trace'):
        for trace_router in request.trace:
            notifications.append({
                'message': trace_router,
                'propertyName': getattr(request, 'property_name', "")
            })

    if hasattr(response, 'data') and type(response.data) is dict and 'message' in response.data.keys():
        notifications.append({
            'message': response.data.get('message', '')
        })
        del response.data['message']

    data = {
        'content': getattr(response, 'data', []),
        'notifications': notifications or "",
        'traceId': "",
        'timestamp': request.start_time.isoformat()
    }

    return data
