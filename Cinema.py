import os
from relatorios import *
from Comum import *
from Gerencia_Salas import *
from Gerencia_Filmes import *
from Gerencia_Sessoes import *

def Menu():
    print("Menu de Opções:")
    print("1: Submenu de Salas")
    print("2: Submenu de Filmes")
    print("3: Submenu de Sessões")
    print("4: Submenu Relatórios")
    print("5: Salvar")
    print("0: Sair")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Submenu_Salas(Salas):
    os.system("cls")
    os.system("clear")
    print("Menu de Salas:")
    print("1: Inserir Sala")
    print("2: Listar Todas as Salas")
    print("3: Pesquisar Salas")
    print("4: Alterar Salas")
    print("5: Remover Sala")
    opcao = int(input("Escolha uma opçao: "))
    
    if opcao == 1:
        Inserir_Sala(Salas)  
    elif opcao == 2:
        Listar_Sala(Salas)  
    elif opcao == 3:
        Pesquisar_Sala(Salas)
    elif opcao == 4:
        Alterar_Sala(Salas) 
    elif opcao == 5:
        Remover_Sala(Salas)
    else:
        print(f"Opção {opcao} inválida. Escolha uma nova opção!")


def Submenu_Filmes(Filmes):
    os.system("cls")
    os.system("clear")
    print("Menu de Filmes:")
    print("1: Inserir Filme")
    print("2: Listar Todos os Filmes")
    print("3: Pesquisar Filmes")
    print("4: Alterar Filme")
    print("5: Remover Filme")
    opcao = int(input("Escolha uma opçao: "))
    
    if opcao == 1:
        Inserir_Filme(Filmes)
    elif opcao == 2:
        Listar_Filme(Filmes)
    elif opcao == 3:
        Pesquisar_Filme(Filmes)
    elif opcao == 4:
        Alterar_Filme(Filmes)
    elif opcao == 5:
        Remover_Filme(Filmes)
    else:
        print(f"Opção {opcao} inválida. Escolha uma nova opção!")

def Submenu_Sessao(Sessoes):
    os.system("cls")
    os.system("clear")
    print("Menu de Sessões:")
    print("1: Inserir Sessão")
    print("2: Listar Todas as Sessões")
    print("3: Pesquisar Sessões")
    print("4: Alterar Sessão")
    print("5: Remover Sessão")
    opcao = int(input("Escolha uma opçao: "))
    
    if opcao == 1:
        Inserir_Sessao(Sessoes)
    elif opcao == 2:
        Listar_Sessao(Sessoes)
    elif opcao == 3:
        Pesquisar_Sessao(Sessoes)
    elif opcao == 4:
        Alterar_Sessao(Sessoes)
    elif opcao == 5:
        Remover_Sessao(Sessoes)
    else:
        print(f"Opção {opcao} inválida. Escolha uma nova opção!")

def Submenu_Relatorios(Filmes,Salas,Sessoes):
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
    Arquivo_Sala = "Dados_Salas.txt"
    Salas = Le_Arquivo_Sala(Arquivo_Sala)

    Arquivo_Filme = "Dados_Filmes.txt"
    Filmes = Le_Arquivo_Filme(Arquivo_Filme)

    Arquivo_Sessao = "Dados_Sessao.txt"
    Sessoes = Le_Arquivo_Sessao(Arquivo_Sessao)

    opcao = 7
    while opcao != 0:   
        opcao = Menu()
        if opcao == 1:
            Submenu_Salas(Salas)
        elif opcao == 2:
            Submenu_Filmes(Filmes)
        elif opcao == 3:
            Submenu_Sessao(Sessoes)
        elif opcao == 4:
            Submenu_Relatorios(Filmes,Salas,Sessoes)
        elif opcao == 5:
            Escreve_Arquivo_Sala(Salas, Arquivo_Sala)
            Escreve_Arquivo_Filme(Filmes, Arquivo_Filme)
            Escreve_Arquivo_Sessao(Sessoes, Arquivo_Sessao)
            print("Salvo!")
        elif opcao == 0:
            Escreve_Arquivo_Sala(Salas, Arquivo_Sala)
            Escreve_Arquivo_Filme(Filmes, Arquivo_Filme)
            Escreve_Arquivo_Sessao(Sessoes, Arquivo_Sessao)
            print("Obrigado por usar o programa!")
        else:
            print(f"Opção {opcao} inválida. Escolha uma nova opção!")


Main()