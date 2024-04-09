from django.contrib import admin
from django.urls import path
from aplicativo import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('editarUsuario/<int:id>', views.editarUsuarios, name='editarUsuario'),
    path('deletarUsuario/<int:id>', views.deletarUsuario, name='deletarUsuario')
]

