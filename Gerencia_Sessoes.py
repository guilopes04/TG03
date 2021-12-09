from Comum import *
import os
from relatorios import *

class Sessao:
    Codigo_Filme = str
    Codigo_Sala = str
    Data = str
    Horario = str
    Preco_Ingresso = float

def Alterar_Sessao(Sessoes):
    os.system("cls")
    os.system("clear")
    Listar_Sessoes(Sessoes)
    posicao = int(input("Escreva qual Sessão deseja alterar: "))
    codigo_filme = input("Informe o código do novo filme: ")
    codigo_sala = input("Informe o código da nova sala: ")
    data = input("Informe a nova data (0/0/0000): ")
    horario = input("Informe o novo horário (00:00): ")
    preco_ingresso = input("Informe o novo preço do ingresso: ")
    if  Buscar_Sessao_Repetida(Sessoes, codigo_filme, codigo_sala, data, horario) == -1:
        print("Não foi possível aterar a sessão! Nova sessão informada já estava cadastrada.")
    s = Sessoes[posicao]
    s.Codigo_Filme = codigo_filme
    s.Codigo_Sala = codigo_sala
    s.Data = data
    s.Horario = horario
    s.Preco_Ingresso = preco_ingresso
    os.system("cls")
    os.system("clear")
    print("Sessão alterada com sucesso!")

def Buscar_Sessao_Repetida(Sessoes, codigo_filme, codigo_sala, data, horario):
    i = 0
    while i < len(Sessoes):
        L = Sessoes[i]
        if L.Codigo_Filme == codigo_filme and L.Codigo_Sala == codigo_sala and L.Data == data and L.Horario == horario:
            return -1
        else:
            return 1

def Listar_Sessoes(Sessoes):
    i = 0
    while i < len(Sessoes):
        print(f"Sessão {i}: ")
        s = Sessoes[i]
        Imprimir_Sessao(s)
        i += 1

def Imprimir_Sessao(s):
    print(s.Codigo_Filme, s.Codigo_Sala, s.Data, s.Horario, s.Preco_Ingresso)

def Remover_Sessao(Sessoes):
    os.system("cls")
    os.system("clear")
    Listar_Sessoes(Sessoes)
    Posicao_Remover = int(input("Escreva o código da sessão a excluir: "))
    Remover(Sessoes, Posicao_Remover)
    os.system("cls")
    os.system("clear")
    print(f"Sessão removida com sucesso!")

def Escreve_Arquivo_Sessao(Sessoes, Nome_Arquivo):
    arq = open(Nome_Arquivo, 'w')
    for s in Sessoes:
        arq.write(s.Codigo_Filme + ';' + s.Codigo_Sala + ';' + s.Data + ';' + s.Horario + ';' + s.Preco_Ingresso + '\n')
    arq.close()

def Le_Arquivo_Sessao(Nome_Arquivo):
    Sessoes = []
    arq = open(Nome_Arquivo, 'r')
    for linha in arq:
        texto = linha.split(';')
        s = Sessao()
        s.Codigo_Filme = texto[0]
        s.Codigo_Sala = texto[1]
        s.Data = texto[2]
        s.Horario = texto[3]
        s.Preco_Ingresso = texto[4]
        Sessoes.append(s)
    arq.close()
    return Sessoes

def Imprimir_Sessao(Sessao):
    print(f"Código do filme: {Sessao.Codigo_Filme} | Código da sala: {Sessao.Codigo_Sala} | Data: {Sessao.Data} | Horário: {Sessao.Horario} | Preço do ingresso: {Sessao.Preco_Ingresso}")


def Inserir_Sessao(Sessoes):
    os.system("cls")
    os.system("clear")
    Codigo_Filme = input("Informe o código do filme: ")
    Codigo_Sala = input("Informe o código da sala: ")
    if Buscar(Sessoes, Codigo_Filme) == -1:
        Data = input("Informe a data da sessão (0/0/0000): ")
        Horario = input("Informe o horário da sessão (00:00): ")
        Preco_Ingresso = input("Informe o preço do ingresso: ")
        sessao = Sessao()
        sessao.Codigo_Filme = Codigo_Filme
        sessao.Codigo_Sala = Codigo_Sala
        sessao.Data = Data
        sessao.Horario = Horario
        sessao.Preco_Ingresso = Preco_Ingresso
        Sessoes.append(sessao)
        os.system("cls")
        os.system("clear")
        print(f"Sessão da sala {sessao.Codigo_Sala} inserida com sucesso.")
    else:
        print(f"Sessão da sala {Codigo_Sala} já cadastrada.")


def Listar_Sessao(Sessao):
    os.system("cls")
    os.system("clear")
    if len(Sessao) == 0:
        print("Não há sessões cadastradas.")
    else:
        for sessao in Sessao:
            Imprimir_Sessao(sessao)

def Pesquisar_Sessao(Sessao):
    os.system("cls")
    os.system("clear")
    Data = input("Informe a data da sessão: ")
    Horario = input("Informe o horário da sessão: ")
    posicao_encontrado_data = Buscar_Sessao_Data(Sessao, Data)
    posicao_encontrado_horario = Buscar_Sessao_Horario(Sessao, Horario)
   
    if posicao_encontrado_data == -1 and posicao_encontrado_horario == -1:
        print(f"Sessão do dia {Data} e horário {Horario} não encontrada.")
    elif posicao_encontrado_data == 0 and posicao_encontrado_horario == -1:
        print(f"Sessão do dia {Data} e horário {Horario} não encontrada.")
    elif posicao_encontrado_data == -1 and posicao_encontrado_horario == 0:
        print(f"Sessão do dia {Data} e horário {Horario} não encontrada.")
    elif posicao_encontrado_data == 0 and posicao_encontrado_horario == 0:
        sessao = Sessao[posicao_encontrado_data]
        Imprimir_Sessao(sessao)
