from Comum import *
import os
from relatorios import *


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

def Imprimir_Sala(Sala):
    print(f"Código: {Sala.Codigo} | Nome: {Sala.Nome} | Capacidade: {Sala.Capacidade} pessoas | Tipo de Exibição: {Sala.Tipo_Exibicao} | Acessibilidade: {Sala.Acessibilidade}")

def Inserir_Sala(Salas):
    Codigo = input("Informe o código da sala: ")
    if Buscar(Salas, Codigo) == -1:
        Nome = input("Informe o nome da sala: ")
        Capacidade = int(input("Informe a capacidade da sala: "))
        Tipo_Exibicao = input("Informe o tipo de exibição: ")
        Acessibilidade = bool(input("Informe se a sala possui acessibilidade: "))
        sala = Sala()
        sala.Codigo = Codigo
        sala.Nome = Nome
        sala.Capacidade = Capacidade
        sala.Tipo_Exibicao = Tipo_Exibicao
        sala.Acessibilidade = Acessibilidade
        Salas.append(sala)
        print(f"Sala {sala.Nome} inserida com sucesso.")
    else:
        print(f"Sala código {Codigo} ja cadastrada.")

def Listar_Sala(Sala):
    if len(Sala) == 0:
        print("Não há salas cadastradas.")
    else:
        print("Código, Nome, Capacidade, Gênero e Acessibilidade")
        for sala in Sala:
            Imprimir_Sala(sala)

def Pesquisar_Sala(Sala):
    Codigo = input("Informe o código da sala: ")
    posicao_encontrado = Buscar(Sala, Codigo)
    if posicao_encontrado == -1:
        print(f"Sala código {Codigo} não encontrada.")
    else:
        sala = Sala[posicao_encontrado]
        Imprimir_Sala(sala)