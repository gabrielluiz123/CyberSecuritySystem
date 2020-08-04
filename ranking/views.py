from django.shortcuts import redirect, render
from django.views import View
from system.models import Usuario

class Index(View):
    model = 'system'
    template_name = 'ranking.html'

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
