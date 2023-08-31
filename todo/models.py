from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 30)

    def __srt__(self):
        return f"Nome: {self.nome}"

class TodoList(models.Model):
    tarefa = models.CharField(max_length = 30)
    choices_status = [
        #um é pro usuario e outro pro BD
        ('F', 'Menina'),
        ('M', 'Menino'),

    ]
    status = models.CharField(choices = choices_status, max_length = 12)
    pessoa = models.ForeignKey(
        Pessoa,
        max_length= 30,
        on_delete= models.CASCADE
    )