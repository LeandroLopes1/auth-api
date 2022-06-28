from email.policy import default
from pkg_resources import require
from rest_framework import serializers

class NotificationsSerializer(serializers.Serializer):
    message = serializers.CharField(default=""),
    property_name = serializers.CharField(default="")