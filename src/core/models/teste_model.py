from statistics import mode
from django.db import models

class TesteModel(models.Model):
    teste = models.CharField(max_length=255)