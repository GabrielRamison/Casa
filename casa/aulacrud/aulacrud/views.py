from django.shortcuts import render
from .models import Pessoa, Casa

def index(request):
    context = {
        'nome': 'Gabriel',
    }
    return render(request, 'conteudo.html', context)

def pessoa_lista(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas': pessoas
    }
    return render(request, 'aula/pessoa_lista.html', context)

def casa_lista(request):
    casas = Casa.objects.all()
    context = {
        'casas': casas
    }
    return render(request, 'aula/casa_lista.html', context)
