from django.urls import path

from receita.views import index,lista_produto

urlpatterns = [
    path('',index),
    path('produtos/',lista_produto),
]