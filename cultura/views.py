from django.shortcuts import render, redirect

from cultura.models import Tb_armazem, Tb_culturas

def home(request):

    lista_culturas = Tb_culturas.objects.all().values('nome', 'tipo') # lista tabela culuras

    culturas = [{lista['nome'], lista['tipo']} for lista in lista_culturas] # varre por nome
    print(f'Culturas: {culturas}') # mostra nome varridos
    print('') # quebra linha

    lista_armazem = Tb_armazem.objects.all().values('nome', 'tipo')

    armazem = [{ lista['nome'], lista['tipo']} for lista in lista_armazem]
    print(f'Armazem: {armazem}')

    context = {    
    }
    return render(request, 'index.html', context = context)
