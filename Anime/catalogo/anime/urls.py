from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_animes, name='lista_animes'),
    path('novo/', views.criar_anime, name='criar_anime'),
    path('editar/<int:pk>/', views.atualizar_anime, name='atualizar_anime'),
    path('deletar/<int:pk>/', views.deletar_anime, name='deletar_anime'),
]
