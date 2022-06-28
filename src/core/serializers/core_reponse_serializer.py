from email import message
from email.policy import default
from rest_framework import serializers

from core.serializers.notifications_serializer import NotificationsSerializer

class ResponseSerializer(serializers.Serializer):
    content = serializers.ListField(required=True)
    notifications = serializers.ListField(
        child = NotificationsSerializer()
    )
    trace_id = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    timestamp = serializers.CharField(required=False, allow_null=True, allow_blank=True)
