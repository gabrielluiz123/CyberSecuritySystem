from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from system.models import Usuario, Categoria, Jogos, Url
from django.contrib.auth.models import User


class Index(View):
    model = 'jogo'
    template_name = 'sidebar_left.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)



class IndexBrute(View):
    model = 'jogo'
    template_name = 'brute_jogo_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexSQL(View):
    model = 'jogo'
    template_name = 'sql_jogo_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        usuarios = Usuario.objects.all().exclude(pk=request.user.id)
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'usuarios': usuarios,
            'url': url,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexDdos(View):
    model = 'jogo'
    template_name = 'ddos_jogo_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class Desafiar(View):
    model = 'jogo'
    template_name = 'jogar_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        print("AQUII")
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        pk = self.kwargs.get('pk')
        cat = self.kwargs.get('cat')
        if url == 'defesa':
            defense_user = Usuario.objects.get(user=request.user)
            attack_user = Usuario.objects.get(user__pk=pk)
        elif url == 'ataque':
            attack_user = Usuario.objects.get(user=request.user)
            defense_user = Usuario.objects.get(user__pk=pk)
        else:
            defense_user = None
            attack_user = None
        categoria = Categoria.objects.get(pk=cat)
        jogo = Jogos(user_attack=attack_user, user_defense=defense_user, categoria=categoria)
        jogo.save()
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
        }

    def get(self, request, *args, **kwargs):
        messages.success(request, "Oponente desafiado com Sucesso!! Aguarde a resposta dele!")
        return render(request, self.template_name, self.contexto)
