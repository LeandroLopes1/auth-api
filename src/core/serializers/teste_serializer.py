from rest_framework import serializers
from ..models import TesteModel, TesteModelCamelCase

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesteModel
        fields = "__all__"

class TesteModelCamelCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesteModelCamelCase
        fields = "__all__"