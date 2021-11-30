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
    opcao_relatorio = int(input("Escolha uma opçao: "))

    if opcao_relatorio == 1:
        Filtro_Cap_Sala(Salas)
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


Main()