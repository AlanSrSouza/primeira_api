from django.shortcuts import render
from rest_framework import viewsets
from .models import Biblioteca
from .serializers import BibliotecaSerializer
# Create your views here.
class BibliotecaViewSet(viewsets.ModelViewSet):
    # Faz uma requisição pro banco de dados e vai procurar todos os objetos do todolist
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer