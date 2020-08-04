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
]