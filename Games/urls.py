from django.urls import path, include
from Games import views

urlpatterns = [

    path('', views.Index.as_view(), name='game'),
    path('/DDoS', views.IndexDdos.as_view(), name='jogar_ddos'),
    path('/SQL', views.IndexSQL.as_view(), name='jogar_sql'),
    path('/Brute', views.IndexBrute.as_view(), name='jogar_brute'),
    path('/Desafio_sql/<int:pk>,<int:cat>', views.Desafiar.as_view(), name='desafiar'),
    path('/Aceitar_Desafio/<int:pk>', views.AceitarDesafio.as_view(), name='aceitar_desafio'),
    path('/Inserir_Code/<int:pk>', views.InserirCode.as_view(), name='inser_line'),
    path('/Desafio/<int:pk>', views.IrParaDesafio.as_view(), name='irpara_desafio'),
    path('/testar/desafio/<int:pk>', views.TestarDesafio.as_view(), name='testar_desafio'),
    path('/Inserir_Senha/<int:pk>', views.ChangePass.as_view(), name='mudar_senha'),
    path('/Inserir_Header/<int:pk>', views.ChangeHeader.as_view(), name='mudar_header'),

]