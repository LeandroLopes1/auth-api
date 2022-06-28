from django.urls import path
from .view import TesteView

urlpatterns = [
    path(
        'teste/',
        TesteView.as_view({'get': 'list'}),
        name='teste'
    )
]