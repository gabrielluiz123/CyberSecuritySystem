from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from django.utils import timezone
from system.models import Usuario, Categoria, Jogos, Url
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import *
import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='sitedjango',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()


class Index(View):
    model = 'jogo'
    template_name = 'sidebar_left.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
            desafios_aceito_1 = len(Jogos.objects.filter(aceite=True, user_defense=user_request, desafiado=request.user, Finalizado=False))
            desafios_aceito_noti = Jogos.objects.filter(aceite=True, user_defense=user_request, desafiado=request.user, Finalizado=False)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
            desafios_aceito_1 = len(Jogos.objects.filter(aceite=True, user_attack=user_request, desafiado=request.user, Finalizado=False))
            desafios_aceito_noti = Jogos.objects.filter(aceite=True, user_attack=user_request, desafiado=request.user, Finalizado=False)
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        print("ATAQUE")
        print(desafios_aceito_1)
        self.contexto = {
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



class IndexBrute(View):
    model = 'jogo'
    template_name = 'brute_jogo_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_aceito_noti,
            'desafios_aceito': desafios_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexSQL(View):
    model = 'jogo'
    template_name = 'sql_jogo_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
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
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class IndexDdos(View):
    model = 'jogo'
    template_name = 'ddos_jogo_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        self.contexto = {
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


class Desafiar(View):
    model = 'jogo'
    template_name = 'jogar_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        print("AQUII")
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)

        pk = self.kwargs.get('pk')
        cat = self.kwargs.get('cat')
        if url == 'defesa':
            defense_user = Usuario.objects.get(user=request.user)
            attack_user = Usuario.objects.get(pk=pk)
        elif url == 'ataque':
            attack_user = Usuario.objects.get(user=request.user)
            defense_user = Usuario.objects.get(user__pk=pk)
        else:
            defense_user = None
            attack_user = None
        desafiado = User.objects.get(pk=pk)
        categoria = Categoria.objects.get(pk=cat)
        jogo = Jogos(user_attack=attack_user, user_defense=defense_user, categoria=categoria, desafiado=desafiado)
        jogo.save()
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
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
        }

    def get(self, request, *args, **kwargs):
        messages.success(request, "Oponente desafiado com Sucesso!! Aguarde a resposta dele!")
        return render(request, self.template_name, self.contexto)



class AceitarDesafio(View):
    model = 'jogo'
    template_name = 'desafio_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        pk_desafio = self.kwargs.get('pk')
        desafio = Jogos.objects.get(pk=pk_desafio)
        if not desafio.aceite:
            desafio.aceite = True
            desafio.iniciado = True
            desafio.inicio_jogo = datetime.now()
            desafio.fim_jogo = datetime.now() + timedelta(minutes=1)
            desafio.save()
            cursor.execute(f'INSERT INTO contatos_contato (desafio_id, nome, sobrenome, telefone) values ({pk_desafio}, "DEsafio", "Ataque", "1222")')
            conexao.commit()
        categoria = desafio.categoria
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'desafio_id': desafio.id,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
            'categoria': categoria,
            'desafio': desafio,
        }

    def get(self, request, *args, **kwargs):
        messages.success(request, "Oponente desafiado com Sucesso!! Aguarde a resposta dele!")
        return render(request, self.template_name, self.contexto)


class IrParaDesafio(View):
    model = 'jogo'
    template_name = 'desafio_index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        pk_desafio = self.kwargs.get('pk')
        desafio = Jogos.objects.get(pk=pk_desafio)
        categoria = desafio.categoria
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'desafio_id': desafio.id,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
            'categoria': categoria,
            'desafio': desafio,
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)


class TestarDesafio(View):
    model = 'jogo'
    template_name = 'sidebar_left.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        url = Url.objects.get(url=request.META['HTTP_HOST']).nome
        user_request = Usuario.objects.get(user=request.user)
        if url == 'defesa':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_defense=user_request, desafiado=request.user)
        elif url == 'ataque':
            desafios_1 = len(Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user))
            desafios_noti = Jogos.objects.filter(aceite=False, user_attack=user_request, desafiado=request.user)
        pk_desafio = self.kwargs.get('pk')
        desafio = Jogos.objects.get(pk=pk_desafio)
        categoria = desafio.categoria
        if request.user.is_authenticated:
            nome = request.user.first_name.strip().split(' ')[0]
        else:
            nome = None

        cursor.execute(f'SELECT sql_desafio FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        self.resultado1 = cursor.fetchall()
        print('Resultado')
        for resultado in self.resultado1:
            for key in resultado:
                self.resultado_sql = resultado[key] = int(resultado[key])

        cursor.execute(f'SELECT login FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        self.resultado1 = cursor.fetchall()
        print('Resultado')
        for resultado in self.resultado1:
            for key in resultado:
                self.resultado_login = resultado[key] = int(resultado[key])
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.contexto = {
            'desafio_id': desafio.id,
            'users': request.user.is_authenticated,
            'nome': nome,
            'url': url,
            'number': desafios_1,
            'number_aceito': desafios_aceito_1,
            'desafios': desafios_noti,
            'desafios_aceito': desafios_aceito_noti,
            'categoria': categoria,
            'desafio': desafio,
        }

    def get(self, request, *args, **kwargs):
        if self.resultado_sql == 0:
            messages.success(request, 'Defesa Ganhou!!')
        else:
            messages.success(request, 'Ataque Ganhou!!')
        return render(request, self.template_name, self.contexto)
