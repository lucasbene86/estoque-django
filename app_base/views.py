from django.shortcuts import render

from .models import DadoProduto
from .forms import CadastroForms
from django.contrib import messages


def index(request):
    dados_produtos = DadoProduto.objects.values()

    form = CadastroForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            print(nome)

        else:
            messages.error(request, 'Dados não foram enviados!')

    produtos = {
        'nome':dados_produtos,
    }


    return render(request, 'index.html', produtos)


def infor(request):
    form = CadastroForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            print(nome)
            messages.success(request, 'Dados enviados!!!')
            form = CadastroForms()
        else:
            messages.error(request, 'Dados não foram enviados!')

    context = {
        'form':form,
    }
    return render(request, 'infor.html', context)