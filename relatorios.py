import datetime

def Filtro_Cap_Sala(Lista):
    anuncio = print("Filtrar Salas entre a capacidade de X até Y pessoas, escreva: 'X Y'")
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
        print("Nenhuma sala encontrada nesses parâmetros")

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
    anuncio = print("Filtrar Filmes entre a data de exibição X até Y, escreva: 'X Y'")
    limite1 = int(input("X: "))
    limite2 = int(input("Y: "))
    Buscar_Cap_Sala(Lista,limite1,limite2)

def Filtro_data_Filme(Filme,Sala,Sessao):
    print("Filtrar a data definindo entre a data X e data Y")
    DataX = input("X: ")
    DataX = DataX.split("/")
    print(DataX)
    DiaX = int(DataX[0])
    print(DiaX)
    MesX = int(DataX[1])
    print(MesX)
    AnoX = int(DataX[2])
    print(AnoX)
    
    DataPrimeira = datetime.date(AnoX, MesX, DiaX)
    print(DataPrimeira)

    DataY = input("Y: ")
    DataY = DataY.split("/")
    DiaY = int(DataY[0])
    MesY = int(DataY[1])
    AnoY = DataY[2]
    print(AnoY)
    Data = []
    for sessao in Sessao:
        print("Entrei Aqui")
        Data = sessao.Data
        Data = Data.split("/")
        print(Data)
        Dia = int(Data[0])
        Mes = int(Data[1])
        Ano = Data[2]
        print(Ano)
        if Ano > AnoX and Ano < AnoY:
            print("primeiro if")
            if Mes >= MesX and Mes <= MesY:
                print("segundo if")
                if Dia >= DiaX and Dia <= DiaY:
                    print("terceiro if")
                    Imprimir_Filme_Data(Filme,Sala,Sessao)
        print("saindo")

def Imprimir_Filme_Data(Filme,Sala,Sessao):
    print(f"Codigo do Filme: {Filme.Codigo} | Nome do Filme: {Filme.Nome} | Atores: {Filme.Atores} | Código da Sala: {Sala.Codigo} | Nome da Sala: {Sala.Nome} | Data da Sessão: {Sessao.Data} | Horário da Sessão: {Sessao.Horario} | Preço do Ingresso: {Sessao.Preco_Ingresso}")

