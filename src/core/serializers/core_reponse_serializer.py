from email.policy import default
from pkg_resources import require
from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    content = serializers.ListField(required=True, default=list)
    notifications = serializers.ListField(
        message = serializers.CharField(required=False, allow_null=True, allow_blank=True),
        property_name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    )
    trace_id = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    timestamp = serializers.CharField(required=False, allow_null=True, allow_blank=True)
