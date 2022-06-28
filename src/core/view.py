from pyexpat import model
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from core.models.teste_model import TesteModel

from .serializers.core_reponse_serializer import ResponseSerializer

class TesteView(mixins.ListModelMixin, viewsets.GenericViewSet):
    class Meta:
        model = TesteModel

    serializer_class = ResponseSerializer

    def get_queryset(self):
        return TesteModel.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        data = serializer.data

        return Response(
            data,
            status.HTTP_200_OK
        )