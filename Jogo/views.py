from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from system.models import Usuario, Categoria, Jogo
from django.contrib.auth.models import User


class Index(View):
    model = 'jogo'
    template_name = 'sidebar_left.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)