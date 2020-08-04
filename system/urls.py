from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('/login', views.Index.as_view(), name='login'),
    path('/reset', views.Index.as_view(), name='user_reset'),
]