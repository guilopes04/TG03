import datetime

class Sala:
    Codigo = ""
    Nome = ""
    Capacidade = int
    Tipo_Exibicao = ""
    Acessibilidade = bool

class Filme:
    Codigo = ""
    Nome = ""
    Ano_Lancamento = int
    Genero = ""
    Atores = ""

class Sessao:
    Codigo_Filme = ""
    Codigo_Sala = ""
    Data = str
    Horario = ""
    Preco_Ingresso = float

def Filtro_Cap_Sala(Lista):
    anuncio = print("Filtrar Salas entre a capacidade de X até Y pessoas")
    limite1 = int(input("X: "))
    limite2 = int(input("Y: "))
    Buscar_Cap_Sala(Lista,limite1,limite2)

def Imprimir_Sala(Sala):
    print(f"Codigo: {Sala.Codigo} | Nome: {Sala.Nome} | Capacidade: {Sala.capacidade} pessoas | Tipo de exibição: {Sala.Tipo_Exibicao} | Acessibilidade: {Sala.Acessibilidade}")

def Buscar_Cap_Sala(lista,limite1,limite2):
    Existe = False
    for sala in lista:
        if sala.capacidade >= limite1 and sala.capacidade <= limite2:
            Imprimir_Sala(sala)
            Existe = True
    if not Existe:
        print("Nenhuma sala encontrada com essa capacidade")

def Imprimir_Filme(Filme):
    print(f"Codigo: {Filme.Codigo} | Nome: {Filme.Nome} | Ano de lançamento: {Filme.Ano_Lancamento} | Genêro: {Filme.Genero} | Atores: {Filme.Atores}")

def Filtro_gen_Filme(lista):
    genêro = input("Qual genêro cinematográfico voce deseja filtrar? ")
    Existe = False
    for filme in lista:
        if filme.Genero == genêro.lower():
            Imprimir_Filme(filme)
            Existe = True
    if not Existe:
        print("Nenhum filme encontrado com esse genêro")

def Filtro_Exib_Sala(Lista):
    anuncio = print("Filtrar Filmes entre a data de exibição X até Y.")
    limite1 = int(input("X: "))
    limite2 = int(input("Y: "))
    Buscar_Cap_Sala(Lista,limite1,limite2)

def Filtro_data_Filme(Filmes,Salas,Sessoes):
    print("Filtrar a data definindo entre a data X e data Y")

    DataX = input("X: ")
    DataX = DataX.split("/")
    DiaX = int(DataX[0])
    MesX = int(DataX[1])
    AnoX = int(DataX[2])

    DataY = input("Y: ")
    DataY = DataY.split("/")
    DiaY = int(DataY[0])
    MesY = int(DataY[1])
    AnoY = int(DataY[2])


    Data = []
    for sessao in Sessoes:
        Data = sessao.Data
        Data = Data.split("/")
        Dia = int(Data[0])
        Mes = int(Data[1])
        Ano = int(Data[2])
        if int(Ano) > int(AnoX) and int(Ano) < int(AnoY):
            if Mes >= MesX and Mes <= MesY:
                if Dia >= DiaX and Dia <= DiaY:
                    Filme_da_Sessao = Filme()
                    Filme_da_Sessao = Buscar_Filme_Cod_Sessao(sessao,Filmes)
                    Sala_da_Sessao = Sala()
                    Sala_da_Sessao = Buscar_Sala_Cod_Sessao(sessao,Salas)
                    Imprimir_Filme_Data(Filme_da_Sessao,Sala_da_Sessao,sessao)


def Imprimir_Filme_Data(Filme,Sala,Sessao):

    print(f"Codigo do Filme: {Filme.Codigo} | Nome do Filme: {Filme.Nome} | Atores: {Filme.Atores} | Código da Sala: {Sala.Codigo} | Nome da Sala: {Sala.Nome} | Data da Sessão: {Sessao.Data} | Horário da Sessão: {Sessao.Horario} | Preço do Ingresso: {Sessao.Preco_Ingresso}")


def Buscar_Filme_Cod_Sessao(sessao, Filmes):
    Existe = False
    for filme in Filmes:
        if filme.Codigo == sessao.Codigo_Filme:
            return filme

def Buscar_Sala_Cod_Sessao(sessao, Salas):
    Existe = False
    for sala in Salas:
        if sala.Codigo == sessao.Codigo_Sala:
            return sala