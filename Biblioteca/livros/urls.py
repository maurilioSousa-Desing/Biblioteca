from django.urls import path
from . import views

app_name = 'livros'


urlpatterns =[

    path(r'', views.index, name='index'),

    path(r'lista/', views.lista, name='lista'),

    path(r'cria/', views.cria, name='cria'),

    path(r'atualizar/', views.atualizar, name='atualizar'),

    path(r'detalhes/', views.detalhes, name='detalhes'),

]