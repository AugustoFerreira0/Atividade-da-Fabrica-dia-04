from rest_framework import serializers
from todo.models import TodoList, Pessoa

class TodolistSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

class PessoasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome']