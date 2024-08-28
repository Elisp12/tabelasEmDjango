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

def update(request):
     
    lista_culturas = Tb_culturas.objects.all().values('nome', 'tipo') # lista tabela de culturas
    
    lista_armazem = Tb_armazem.objects.all() # lista tabela de armazem
    
    # não consigo salvar o proximo dado sem que o anterior a este não seja modificado   (histórico)
    # for armazem in lista_armazem:
    #     armazem.old_nome = armazem.nome
    #     armazem.old_tipo = armazem.tipo
    #     armazem.save()

    for cultura in lista_culturas:
        # tenta buscar um objeto da tb_armazem com o mesmo nome 
        dados_armazem = Tb_armazem.objects.filter(nome =cultura['nome']).first()

        if dados_armazem: # se existe objeto com o mesmo nome  

            dados_armazem.tipo = cultura['tipo'] # atualiza o tipo
            dados_armazem.save() # salva na tabela


    context = {    
    }
    return redirect('home')