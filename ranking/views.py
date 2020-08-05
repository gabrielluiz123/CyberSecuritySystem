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
        usuarios = Usuario.objects.all().order_by('-pontos')[:10]
        usuarios_u = Usuario.objects.all().order_by('-pontos')
        eu = Usuario.objects.get(user=request.user)
        i = 0
        for u in usuarios_u:
            i = i + 1
            if u.user == request.user:
                break

        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'usuarios':usuarios,
            'eu':eu,
            'i':i,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)
