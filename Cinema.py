import os
from Gerencia_Salas import *
from Gerencia_Filmes import *
from Gerencia_Sessoes import *

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
    print("Menu de Sessões:")
    print("1: Inserir Sessão")
    print("2: Listar Todas as Sessões")
    print("3: Pesquisar Sessões")
    print("4: Alterar Sessão")
    print("5: Remover Sessão")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Submenu_Relatorios():
    os.system("cls")
    print("Menu de Relatórios:")
    print("1: Filtrar por capacidade da sala")
    print("2: Filtrar por gênero de filme")
    print("3: Filtrar por data de Filmes")
    opcao_relatorio = int(input("Escolha uma opçao: "))

    if opcao_relatorio == 1:
        Filtro_Cap_Sala()
    elif opcao_relatorio == 2:
        Filtro_gen_Filme()
    elif opcao_relatorio == 3:
        Filtro_data_Filme()

def Filtro_Cap_Sala(Lista):
    anuncio = print("Filtrar Salas entre a capacidade de X até Y pessoas, escreva: 'X Y'")
    limite1 = int(input("X: "))
    limite2 = int(input("Y: "))
    Buscar_Cap_Sala(Lista,limite1,limite2)

def Imprimir_Sala(Sala):
    print(f"Codigo: {Sala.Codigo} | Nome: {Sala.Nome} | Capacidade: {Sala.capacidade} pessoas | Genêro: {Sala.Tipo_Exibicao} | Acessibilidade: {Sala.Acessibilidade}")

def Buscar_Cap_Sala(lista,limite1,limite2):
    Existe = False
    for sala in lista:
        if sala.capacidade >= limite1 and sala.capacidade <= limite2:
            Imprimir_Sala(sala)
            Existe = True
    if not Existe:
        print("Nenhuma sala encontrada nesses parâmetros")
        
def Filtro_gen_Filme():
    pass

def Filtro_data_Filme():
    pass

def Main():
    Arquivo_Sala = "Dados_Salas.txt"
    Salas = Le_Arquivo_Sala(Arquivo_Sala)   #colocar maiusculas

    Arquivo_Filme = "Dados_Filmes.txt"
    Filmes = Le_Arquivo_Filme(Arquivo_Filme)

    Arquivo_Sessao = "Dados_Sessao.txt"
    Sessoes = Le_Arquivo_Sessao(Arquivo_Sessao)

    opcao = 7
    while opcao != 0:   
        opcao = Menu()
        if opcao == 1:
            opcao = Submenu_Salas()
            if opcao == 1:
                print("1: Inserir Salas")
            elif opcao == 2:
                print("2: Listar Salas")
            elif opcao == 3:
                print("3: Pesquisar Salas")
            elif opcao == 4:
                Alterar_Sala(Salas)
            elif opcao == 5:
                Remover_Sala(Salas)
            else:
                print(f"Opção {opcao} inválida. Escolha uma nova opção!")
        elif opcao == 2:
            opcao = Submenu_Filmes()
            if opcao == 1:
                inserir_filme(Filmes)
            elif opcao == 2:
                listar_filmes(Filmes)
            elif opcao == 3:
                print("3: Pesquisar Filmes")
            elif opcao == 4:
                Alterar_Filme(Filmes)
            elif opcao == 5:
                Remover_Filme(Filmes)
            else:
                print(f"Opção {opcao} inválida. Escolha uma nova opção!")
        elif opcao == 3:
            opcao = Submenu_Sessao()
            if opcao == 1:
                inserir_sessao(Sessoes)
            elif opcao == 2:
                listar_sessoes(Sessoes)
            elif opcao == 3:
                print("3: Pesquisar Sessão")
            elif opcao == 4:
                Alterar_Sessao(Sessoes)
            elif opcao == 5:
                Remover_Sessao(Sessoes)
            else:
                print(f"Opção {opcao} inválida. Escolha uma nova opção!")
        elif opcao == 4:
            Submenu_Relatorios()
        elif opcao == 0:
            Escreve_Arquivo_Sala(Salas, Arquivo_Sala)
            Escreve_Arquivo_Filme(Filmes, Arquivo_Filme)
            Escreve_Arquivo_Sessao(Sessoes, Arquivo_Sessao)
            print("Obrigado por usar o programa!")
        else:
            print(f"Opção {opcao} inválida. Escolha uma nova opção!")


Main()