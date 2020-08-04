from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import validate_email


class Index(View):
    model = 'Registro'
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

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None

        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
        }

        if request.POST.get('email_cadastro'):
            nome = request.POST.get('name')
            email = request.POST.get('email_cadastro')
            senha = request.POST.get('pwd')
            senha2 = request.POST.get('pwd2')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já existe')
            user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
            try:
                user.save()
            except:
                messages.error(request, 'Falha ao se cadastrar! Contacte o administrador do site!')
                return render(request, self.template_name, self.contexto)


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('email')
    senha = request.POST.get('pwd')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return redirect('index')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')