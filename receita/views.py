from django.http import JsonResponse
from django.shortcuts import render

def index(request):
  return render(request, 'global/index.html')

