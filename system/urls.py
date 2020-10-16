from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('/login', views.login, name='login'),
    path('/logout', views.logout, name='logout'),
    path('/reset', views.logout, name='user_reset'),
    path('/busca', views.logout, name='post_busca'),
    path('/detalhes', views.logout, name='detalhes'),
    path('/renovacoes', views.logout, name='detalhes'),
    path('/jogar', views.IndexJogar.as_view(), name='jogar_index'),
    path('/ddos', views.IndexDdos.as_view(), name='ddos_index'),
    path('/sql', views.IndexSql.as_view(), name='sql_index'),
    path('/brute', views.IndexBrute.as_view(), name='brute_index'),
    path('/xss', views.IndexXss.as_view(), name='xss_index'),
]