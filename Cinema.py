import os
class Sala:
    Codigo = int
    Nome = ""
    Capacidade = int
    Tipo_Exibicao = ""
    Acessibilidade = bool

class Filme:
    Codigo = int
    Nome = ""
    Ano_Lancamento = int
    Genero = ""
    Atores = []

class Sessao:
    Codigo_Filme = int
    Codigo_Sala = int
    Data = ""
    Horario = ""
    Preco_Ingresso = ""

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
    print("3: Filtrar por data de filmes")
    opcao = int(input("Escolha uma opçao: "))
    return opcao

def Main():
    opcao = 0
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

Main()