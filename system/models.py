from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Usuario(models.Model):
    pontos = models.IntegerField(default=0, verbose_name='Pontos')
    pontos_ataque = models.IntegerField(default=0, verbose_name='Pontos de Ataque')
    pontos_defesa = models.IntegerField(default=0, verbose_name='Pontos de Defesa')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    nome = models.CharField(max_length=255, verbose_name='Nome')

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Categoria")

    def __str__(self):
        return self.nome


class Jogos(models.Model):
    name = models.CharField(max_length=255, default='Game', verbose_name="Nome")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Data de criação")
    user_attack = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='user_attack', verbose_name="Usuário de Ataque")
    user_defense = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='user_defense', verbose_name="Usuário de Defesa")
    ganhador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='user_ganhador', verbose_name="Ganhador", null=True, blank=True)
    pontos = models.IntegerField(default=0, verbose_name="Pontos Recebidos", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name="Categoria", null=True, blank=True)
    aceite = models.BooleanField(default=False, verbose_name="Aceite")
    iniciado = models.BooleanField(default=False, verbose_name="Iniciado")
    inicio_jogo = models.DateTimeField(null=True, blank=True, verbose_name="Inicio do Game")
    fim_jogo = models.DateTimeField(null=True, blank=True, verbose_name="Fim do Game")
    Finalizado = models.BooleanField(default=False, verbose_name="Finalizado")

    def __str__(self):
        return self.name


class Url(models.Model):
    url = models.CharField(max_length=255, verbose_name="URL")
    nome = models.CharField(max_length=255, verbose_name="Nome")

    def __str__(self):
        return self.nome