from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from .models import Jogos, Categoria, Url
from .models import Usuario
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.validators import validate_email


class IndexJogar(View):
    model = 'system'
    template_name = 'jogar_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_1 = None
        desafios_noti = None
        categorias = Categoria.objects.all()
        if request.user.is_authenticated:
            user_request = Usuario.objects.get(user=request.user)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
                desafios_aceito_1 = len(
                    Jogos.objects.filter(aceite=True, user_defense=user_request, desafiado=request.user,
                                         Finalizado=False))
                desafios_aceito_noti = Jogos.objects.filter(aceite=True, user_defense=user_request,
                                                            desafiado=request.user, Finalizado=False)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
                desafios_aceito_1 = len(
                    Jogos.objects.filter(aceite=True, user_attack=user_request, desafiado=request.user,
                                         Finalizado=False))
                desafios_aceito_noti = Jogos.objects.filter(aceite=True, user_attack=user_request,
                                                            desafiado=request.user, Finalizado=False)
            if request.user.is_authenticated:
                nome = request.user.first_name.strip().split(' ')[0]
            else:
                nome = None
            desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                        Q(user_defense=user_request) | Q(user_attack=user_request),
                                                        Q(Finalizado=False))
            desafios_aceito_1 = len(desafios_aceito_noti)

        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'categorias': categorias,
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexXss(View):
    model = 'system'
    template_name = 'xss_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_noti = None
        desafios_1 = None
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
            user_request = Usuario.objects.get(user=request.user)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'number_aceito': desafios_aceito_1,
            'desafios_aceitos': desafios_aceito_noti,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'desafios': desafios_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)



class IndexBrute(View):
    model = 'system'
    template_name = 'brute_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_noti = None
        desafios_1 = None
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
            user_request = Usuario.objects.get(user=request.user)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'number_aceito': desafios_aceito_1,
            'desafios_aceitos': desafios_aceito_noti,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'desafios': desafios_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexDdos(View):
    model = 'system'
    template_name = 'ddos_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_noti = None
        desafios_1 = None
        if request.user.is_authenticated:
            user_request = Usuario.objects.get(user=request.user)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_aatack=user_request, desafiado=request.user)
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'number_aceito': desafios_aceito_1,
            'desafios_aceitos': desafios_aceito_noti,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'desafios': desafios_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexSql(View):
    model = 'system'
    template_name = 'sql_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_noti = None
        desafios_1 = None
        if request.user.is_authenticated:
            user_request = Usuario.objects.get(user=request.user)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'number_aceito': desafios_aceito_1,
            'desafios_aceitos': desafios_aceito_noti,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'desafios': desafios_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)



class Index(View):
    model = 'system'
    template_name = 'sidebar_left.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_noti = None
        desafios_1 = None
        desafios_aceito_noti = None
        desafios_aceito_1 = None
        nome = None
        if request.user.is_authenticated:
            user_request = Usuario.objects.get(user=request.user)
            print("ALII")
            print(desafios_noti)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
                print(desafios_noti)
            desafios_aceito_1 = len(
                Jogos.objects.filter(Q(aceite=True), Q(user_defense=user_request) | Q(user_attack=user_request),
                                     Q(Finalizado=False)))
            if request.user.is_authenticated:
                nome = request.user.first_name.strip().split(' ')[0]
                desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                            Q(user_defense=user_request) | Q(user_attack=user_request),
                                                            Q(Finalizado=False))
                desafios_aceito_1 = len(desafios_aceito_noti)
            else:
                nome = None
                desafios_aceito_noti = None
                desafios_aceito_1 =  None
            print("ATAQUE")
            print(desafios_aceito_1)
        self.contexto = {
            'number_aceito': desafios_aceito_1,
            'desafios_aceitos': desafios_aceito_noti,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        desafios_1 = None
        if request.user.is_authenticated:
            user_request = Usuario.objects.get(user=request.user)
            if url == 'defesa':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            elif url == 'ataque':
                desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
                desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None

        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'number_aceito': desafios_aceito_1,
            'desafios_aceitos': desafios_aceito_noti,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'desafios': desafios_noti,
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
