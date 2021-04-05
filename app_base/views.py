from django.shortcuts import render

from .models import DadoProduto


def index(request):
    dados_produtos = DadoProduto.objects.values()

    print(dados_produtos)
    produtos = {
        'nome':dados_produtos,
    }


    return render(request, 'index.html', produtos)


def infor(request):
    return render(request, 'infor.html')