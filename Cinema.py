import os
from relatorios import *
from datetime import date

def Menu():
    print("Menu de Opções:")
    print("1: Submenu de Salas")
    print("2: Submenu de Filmes")
    print("3: Submenu de Sessões")
    print("4: Submenu Relatórios")
    print("0: Sair")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Submenu_Salas():
    os.system("cls")
    os.system("clear")
    print("Menu de Salas:")
    print("1: Inserir Sala")
    print("2: Listar Todas as Salas")
    print("3: Pesquisar Salas")
    print("4: Alterar Salas")
    print("5: Remover Sala")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Submenu_Filmes():
    os.system("cls")
    os.system("clear")
    print("Menu de Filmes:")
    print("1: Inserir Filme")
    print("2: Listar Todas os Filmes")
    print("3: Pesquisar Filmes")
    print("4: Alterar Filme")
    print("5: Remover Filme")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Submenu_Sessao():
    os.system("cls")
    os.system("clear")
    print("Menu de Sessões:")
    print("1: Inserir Sessão")
    print("2: Listar Todas as Sessões")
    print("3: Pesquisar Sessões")
    print("4: Alterar Sessão")
    print("5: Remover Sessão")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Submenu_Relatorios():
    os.system("cls") #windows
    os.system("clear") #linux
    print("Menu de Relatórios:")
    print("1: Filtrar por capacidade da sala")
    print("2: Filtrar por gênero de filme")
    print("3: Filtrar por data de Sessões")
    opcao_relatorio = int(input("Escolha uma opçao: "))

    if opcao_relatorio == 1:
        Filtro_Cap_Sala(Salas)
    elif opcao_relatorio == 2:
        Filtro_gen_Filme(Filmes)
    elif opcao_relatorio == 3:
        Filtro_data_Filme(Filmes,Salas,Sessoes)

def Main():
    opcao = 7
    while opcao != 0:   
        opcao = Menu()
        if opcao == 1:
            Submenu_Salas()
        elif opcao == 2:
            Submenu_Filmes()
        elif opcao == 3:
            Submenu_Sessao()
        elif opcao == 4:
            Submenu_Relatorios()
        elif opcao == 0:
            print("Obrigado por usar o programa")
        else:
            print("Valor Incorreto, digite novamente!")

#testes
Salas = []
sala = Sala()
sala.Codigo = 3
sala.Nome = 'sexo'
sala.capacidade = 400
sala.Tipo_Exibicao = 'romance'
sala.Acessibilidade = True
Salas.append(sala)

sala = Sala()
sala.Codigo = 2
sala.Nome = 'bilada'
sala.capacidade = 300
sala.Tipo_Exibicao = 'terror'
sala.Acessibilidade = False
Salas.append(sala)

Filmes = []
filme = Filme()
filme.Codigo = 777
filme.Nome = 'bilada molenga'
filme.Ano_Lancamento = 2013
filme.Genero = 'terror'
filme.Atores = "Jose, kiko, thigas"
Filmes.append(filme)

Sessoes = []
sessao = Sessao()
sessao.Codigo_Filme = 777
sessao.Codigo_Sala = 2
sessao.Data = "20/6/2019"
sessao.Horario = "4:20"
sessao.Preco_Ingresso = 16.50
Sessoes.append(sessao)

Main()