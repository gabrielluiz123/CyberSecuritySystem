from django.urls import path, include
from Games import views

urlpatterns = [

    path('', views.Index.as_view(), name='game'),
    path('/DDoS', views.IndexDdos.as_view(), name='jogar_ddos'),
    path('/SQL', views.IndexSQL.as_view(), name='jogar_sql'),
    path('/Brute', views.IndexBrute.as_view(), name='jogar_brute'),
    path('/Desafio_sql/<int:pk>,<int:cat>', views.Desafiar.as_view(), name='desafiar'),
]