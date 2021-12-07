from Comum import *
from datetime import *
import os

class Sessao:
    Codigo_Filme = ""
    Codigo_Sala = ""
    Data = ""
    Horario = ""
    Preco_Ingresso = ""

def Alterar_Sessao(Sessoes):
    os.system("cls")
    Repeticao = True
    while Repeticao:
        Listar_Sessoes(Sessoes)
        posicao = int(input("Escreva qual Sessão deseja alterar: "))
        codigo_filme = input("Informe o código do novo filme: ")
        codigo_sala = input("Informe o código da nova sala: ")
        ano = int(input("Informe o novo ano: "))
        mes = int(input("Informe o novo mês: "))
        dia = int(input("Informe o novo dia: "))
        data = date(ano, mes, dia)
        hora = int(input("Informe somente a hora: "))
        minutos = int(input("Informe somente os minutos: "))
        horario = time(hora, minutos)
        preco_ingresso = input("Informe o novo preço do ingresso: ")
        if  Buscar_Sessao_Repetida(Sessoes, codigo_filme, codigo_sala, data, horario) == -1:
            print("Não foi possível aterar a sessão! Nova sessão informada já estava contida.")
        else:
            Repeticao = False
    s = Sessoes[posicao]
    s.Codigo_Filme = codigo_filme
    s.Codigo_Sala = codigo_sala
    s.Data = date(ano, mes, dia)
    s.Horario = time(hora, minutos)
    s.Preco_Ingresso = preco_ingresso
    os.system("cls")
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
    codigo = input("Escreva o código da sessão: ")
    Posicao_Remover = Buscar(Sessoes, codigo)
    if Posicao_Remover == -1:
        print(f"Sessão {codigo} não encontrada.")
    else:
        Remover(Sessoes, Posicao_Remover)
        os.system("cls")
        print(f"Sessão código {codigo} removida com sucesso!")

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