from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def infor(request):
    return render(request, 'infor.html')