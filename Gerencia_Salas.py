from Comum import *
import os

class Sala:
    Codigo = ""
    Nome = ""
    Capacidade = int
    Tipo_Exibicao = ""
    Acessibilidade = ""

def Alterar_Sala(Salas):
    os.system("cls")
    codigo = input("Escreva o código da sala: ")
    posicao = Buscar(Salas, codigo)
    if posicao == -1:
        print(f"Sala {codigo} não encontrada.")
    else:
        s = Salas[posicao]
        s.Nome = input("Informe o novo nome: ")
        s.Capacidade = int(input("Informe a nova capacidade: "))
        s.Tipo_Exibicao = input("Informe o novo tipo de exibição: ")
        s.Acessibilidade = input("Informe 'Sim' ou 'Não' para acessibilidade: ")
        os.system("cls")
        print(f"Sala código {s.Codigo} alterada com sucesso!")

def Remover_Sala(Salas):
    os.system("cls")
    codigo = input("Escreva o código da sala: ")
    Posicao_Remover = Buscar(Salas, codigo)
    if Posicao_Remover == -1:
        print(f"Sala {codigo} não encontrada.")
    else:
        Remover(Salas, Posicao_Remover)
        os.system("cls")
        print(f"Sala código {codigo} removida com sucesso!")

def Escreve_Arquivo_Sala(Salas, Nome_Arquivo):
    arq = open(Nome_Arquivo, 'w')
    for s in Salas:
        arq.write(s.Codigo + ';' + s.Nome + ';' + str(s.Capacidade) + ';' + s.Tipo_Exibicao + ';' + s.Acessibilidade + '\n')
    arq.close()

def Le_Arquivo_Sala(Nome_Arquivo):
    Salas = []
    arq = open(Nome_Arquivo, 'r')
    for linha in arq:
        texto = linha.split(';')
        s = Sala()
        s.Codigo = texto[0]
        s.Nome = texto[1]
        s.Capacidade = texto[2]
        s.Tipo_Exibicao = texto[3]
        s.Acessibilidade = texto[4]
        Salas.append(s)
    arq.close()
    return Salas