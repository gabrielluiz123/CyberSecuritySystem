from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
    pontos = models.IntegerField(default=0, verbose_name='Pontos')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    nome = models.CharField(max_length=255, verbose_name='Nome')

    def __str__(self):
        return self.nome