from django.http import JsonResponse
from django.shortcuts import render

def index(request):
  return render(request, 'global/index.html')

def lista_produto(request):
    lista = [
            {'produto':'Café'},
            {'valor':'R$ 12.0'}
            ]
    return JsonResponse(lista, safe=False)