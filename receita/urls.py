from django.urls import path

from receita.views import index

urlpatterns = [
    path('',index),
]