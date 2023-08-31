from rest_framework import viewsets
from .models import TodoList, Pessoa
from .serializers import TodolistSerializers, PessoasSerializers

class TodolistViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodolistSerializers

class PessoaViewset(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoasSerializers