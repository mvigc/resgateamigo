from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Gato

@require_POST
def cadastrar_gato(request):
    try:
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        castracao = request.POST.get('castracao')
        saude = request.POST.get('saude')
        pelagem = request.POST.get('pelagem')
        imagem = request.FILES.get('imagem-gato')

        # Cria uma nova instância do modelo Gato e salva no banco de dados
        gato = Gato(nome=nome, sexo=sexo, idade=idade, castracao=castracao, saude=saude, pelagem=pelagem, imagem=imagem)
        gato.save()

        messages.success(request, "Gato cadastrado com sucesso!")
        return redirect('cadastrar_gato')
    except Exception as e:
        messages.error(request, f"Ocorreu um erro: {e}")
        return redirect('cadastrar_gato')
