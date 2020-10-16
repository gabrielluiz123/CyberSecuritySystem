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
    host='18.219.154.84',
    user='admin',
    password='Maria@1601',
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
    template_name = 'brute_jogo_index_cop.html'

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
            'categoria_id': 2,
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


class IndexSQL(View):
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
        usuarios = Usuario.objects.all().exclude(pk=request.user.id)
        self.contexto = {
            'code':'<p> aa </p>',
            'categoria_id':2,
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
    template_name = 'xss_jogo_index.html'

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
            'code':'<p> aa </p>',
            'categoria_id':1,
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
            cursor = conexao.cursor()
            print('INSERT INTO sitedjango.contatos_contato (desafio_id, nome, sobrenome, telefone, email, data_criacao, descricao, mostrar, foto, login, sql_desafio, new_code, new_header2) values ('+str(pk_desafio)+', "DEsafio", "Ataque", "1222", "g@g.com", "2020-01-01 00:00:00", "aa", 1, "1", 0, 0, "contatos = Contato.objects.raw(f\'SELECT * FROM contatos_contato WHERE nome LIKE \'{termo[0]}\'\')" )')
            cursor.execute('INSERT INTO sitedjango.contatos_contato (desafio_id, nome, sobrenome, telefone, email, data_criacao, descricao, mostrar, foto, login, sql_desafio, new_code, new_header, new_header2) values ('+str(pk_desafio)+', "DEsafio", "Ataque", "1222", "g@g.com", "2020-01-01 00:00:00", "aa", 1, "1", 0, 0, "dsadsadsadadgfdg", "sdaoijfda", "dsiojfads")')
            conexao.commit()
            cursor.close()
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
        self.resultado_login = self.resultado_sql = 0
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
        cursor = conexao.cursor()
        cursor.execute(f'SELECT sql_desafio FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        self.resultado1 = cursor.fetchall()
        print('Resultado')
        for resultado in self.resultado1:
            for key in resultado:
                self.resultado_sql = resultado[key] = int(resultado[key])
        self.usuario_user_ataque = User.objects.get(pk=desafio.user_attack.id)
        self.usuario_user_defesa = User.objects.get(pk=desafio.user_defense.id)
        self.jogador_defesa = Usuario.objects.get(user=self.usuario_user_defesa)
        self.jogador_ataque = Usuario.objects.get(user=self.usuario_user_ataque)
        cursor.execute(f'SELECT login FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        self.resultado1 = cursor.fetchall()
        cursor.close()

        self.resultado_header_r = ''
        for resultado in self.resultado1:
            for key in resultado:
                self.resultado_login = resultado[key] = int(resultado[key])
        cursor = conexao.cursor()
        cursor.execute(f'SELECT new_header2 FROM contatos_contato WHERE desafio_id = {pk_desafio}')
        self.resultado_header = cursor.fetchall()
        cursor.close()
        for resultado in self.resultado_header:
            for key in resultado:
                self.resultado_header_r = resultado[key] = str(resultado[key])
        self.res_xss_bool = True
        if '<script' in self.resultado_header_r and '</script>' in self.resultado_header_r:
            self.res_xss_bool = False
        print('Resultado')
        desafios_aceito_noti = Jogos.objects.filter(Q(aceite=True),
                                                    Q(user_defense=user_request) | Q(user_attack=user_request),
                                                    Q(Finalizado=False))
        desafios_aceito_1 = len(desafios_aceito_noti)
        self.category = categoria.id

        print('SQL')
        print(self.resultado_sql)

        if not desafio.Finalizado:
            if categoria.id == 1:
                if self.res_xss_bool:
                    self.jogador_defesa.pontos_defesa = self.jogador_defesa.pontos_defesa + 10
                    self.jogador_defesa.pontos = self.jogador_defesa.pontos + 10
                    self.jogador_defesa.save()
                    messages.success(request, 'Defesa Ganhou!!')
                else:
                    self.jogador_ataque.pontos_ataque = self.jogador_ataque.pontos_ataque + 10
                    self.jogador_ataque.pontos = self.jogador_ataque.pontos + 10
                    self.jogador_ataque.save()
                    messages.success(request, 'Ataque Ganhou!!')
            elif categoria.id == 2:
                if self.resultado_sql == 0:
                    self.jogador_defesa.pontos_defesa = self.jogador_defesa.pontos_defesa + 10
                    self.jogador_defesa.pontos = self.jogador_defesa.pontos + 10
                    self.jogador_defesa.save()
                    messages.success(request, 'Defesa Ganhou!!')
                else:
                    self.jogador_ataque.pontos_ataque = self.jogador_ataque.pontos_ataque + 10
                    self.jogador_ataque.pontos = self.jogador_ataque.pontos + 10
                    self.jogador_ataque.save()
                    messages.success(request, 'Ataque Ganhou!!')
            elif categoria.id == 3:
                if self.resultado_login == 0:
                    self.jogador_defesa.pontos_defesa = self.jogador_defesa.pontos_defesa + 10
                    self.jogador_defesa.pontos = self.jogador_defesa.pontos + 10
                    self.jogador_defesa.save()
                    messages.success(request, 'Defesa Ganhou!!')
                else:
                    self.jogador_ataque.pontos_ataque = self.jogador_ataque.pontos_ataque + 10
                    self.jogador_ataque.pontos = self.jogador_ataque.pontos + 10
                    self.jogador_ataque.save()
                    messages.success(request, 'Ataque Ganhou!!')
        desafio.Finalizado = True
        desafio.save()


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
        if self.category == 1:
            if self.res_xss_bool:
                messages.success(request, 'Defesa Ganhou!!')
            else:
                messages.success(request, 'Ataque Ganhou!!')
        elif self.category == 2:
            if self.resultado_sql == 0:
                messages.success(request, 'Defesa Ganhou!!')
            else:
                messages.success(request, 'Ataque Ganhou!!')
        elif self.category == 3:
            if self.resultado_login == 0:
                messages.success(request, 'Defesa Ganhou!!')
            else:
                messages.success(request, 'Ataque Ganhou!!')
        return render(request, self.template_name, self.contexto)


class InserirCode(View):
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
        code = str(request.POST.get('new_code'))
        code.replace("'", "\\'")
        code.replace('"', "\\\\")
        print(code)
        self.pk_desafio = self.kwargs.get('pk')
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE contatos_contato set new_code = "{code}" where desafio_id = {self.pk_desafio}')
        conexao.commit()
        cursor.close()

        messages.success(request, 'Codigo inserido com sucesso')
        return redirect('irpara_desafio', self.pk_desafio)
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Codigo inserido com sucesso')
        return redirect('irpara_desafio', self.pk_desafio)


class ChangePass(View):
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
        code = str(request.POST.get('new_pass'))
        code.replace("'", "\\'")
        code.replace('"', "\\\\")
        print(code)
        self.pk_desafio = self.kwargs.get('pk')
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE contatos_contato set new_senha = "{code}" where desafio_id = {self.pk_desafio}')
        conexao.commit()
        cursor.close()

        messages.success(request, 'Senha modificada com sucesso')
        return redirect('irpara_desafio', self.pk_desafio)
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Senha modificada com sucesso')
        return redirect('irpara_desafio', self.pk_desafio)



class ChangeHeader(View):
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
        code = str(request.POST.get('new_header'))
        code.replace("'", "\\'")
        code.replace('"', "\\\\")
        code2 = str(request.POST.get('new_header2'))
        code2.replace("'", "\\'")
        code2.replace('"', "\\\\")
        print(code)
        self.pk_desafio = self.kwargs.get('pk')
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE contatos_contato set new_header = "{code}", new_header2 = "{code2}" where desafio_id = {self.pk_desafio}')
        conexao.commit()
        cursor.close()

        messages.success(request, 'Senha modificada com sucesso')
        return redirect('irpara_desafio', self.pk_desafio)
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Senha modificada com sucesso')
        return redirect('irpara_desafio', self.pk_desafio)