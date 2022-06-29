from .models import TesteModel, TesteModelCamelCase
from rest_framework.request import Request
from rest_framework import mixins, viewsets
from .serializers.teste_serializer import TesteSerializer, TesteModelCamelCaseSerializer
from .view_core import ViewCore


class TesteView(ViewCore, mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = TesteModelCamelCaseSerializer

    def get_queryset(self):
        return TesteModelCamelCase.objects.all()

    def list(self, request, *args, **kwargs):
        return super(TesteView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TesteView, self).create(request, *args, **kwargs)