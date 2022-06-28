from pyexpat import model
from rest_framework import mixins, viewsets, status
from .utils import get_response

from core.models.teste_model import TesteModel

from .serializers.core_reponse_serializer import ResponseSerializer

class TesteView(mixins.ListModelMixin, viewsets.GenericViewSet):
    class Meta:
        model = TesteModel

    serializer_class = ResponseSerializer

    def get_queryset(self):
        return TesteModel.objects.all()

    def list(self, request, *args, **kwargs):
        return get_response(
            content=[],
            status=status.HTTP_200_OK,
            timestamp=request.start_time
        )