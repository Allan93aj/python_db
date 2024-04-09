from django.shortcuts import get_object_or_404, redirect, render
from .models import Usuarios


# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

def usuarios(request):
    if request.method == "POST":
        novo_usuario = Usuarios()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.setor = request.POST.get('setor')
        novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }


    return render(request, 'usuarios/usuarios.html', usuarios)


# deletar usuarios
def deletarUsuario(request, id):
    delete_user = get_object_or_404(Usuarios, pk=id)
    delete_user.delete()
    return redirect('../usuarios/')

# editar usuarios
def editarUsuarios(request, id):

    user = get_object_or_404(Usuarios, pk=id)
    editarUser = {
        'editarUser': user
    }

    if(request.method == "POST"):
        edit_usuario = Usuarios()
        edit_usuario.nome = request.POST.get('nome')
        edit_usuario.email = request.POST.get('email')
        edit_usuario.setor = request.POST.get('setor')
        edit_usuario.save()
        return redirect('../usuarios')
    else:
        return render(request, 'editarUsuario/index.html', editarUser)