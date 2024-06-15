# models.py
from django.db import models

class Gato(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=[('macho', 'Macho'), ('femea', 'Fêmea')])
    idade = models.PositiveIntegerField()
    castracao = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    saude = models.TextField()
    pelagem = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='gatos/')

    def __str__(self):
        return self.nome
