from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from .models import Usuario
from django.contrib.auth.models import User
from django.core.validators import validate_email


class IndexJogar(View):
    model = 'system'
    template_name = 'jogar_index.html'

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


class IndexBrute(View):
    model = 'system'
    template_name = 'brute_index.html'

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


class IndexDdos(View):
    model = 'system'
    template_name = 'ddos_index.html'

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


class IndexSql(View):
    model = 'system'
    template_name = 'sql_index.html'

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



class Index(View):
    model = 'system'
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

            if senha != senha2:
                messages.error(request, 'Senhas não correspondem!')
                return render(request, self.template_name, self.contexto)
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já existe')
                return render(request, self.template_name, self.contexto)
            user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
            user_u = Usuario(nome=nome, user=user, pontos=0)
            try:
                user.save()
                user_u.save()
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
