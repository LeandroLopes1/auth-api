from django.db import models

class TesteModel(models.Model):
    teste = models.CharField(max_length=255)

class TesteModelCamelCase(models.Model):
    teste_camel = models.CharField(max_length=255)