from Comum import *
import os

class Filme:
    Codigo = ""
    Nome = ""
    Ano_Lancamento = int
    Genero = ""
    Atores = ""

def Alterar_Filme(Filmes):
    os.system("cls")
    codigo = input("Escreva o código do Filme: ")
    posicao = Buscar(Filmes, codigo)
    if posicao == -1:
        print(f"Filme {codigo} não encontrado.")
    else:
        f = Filmes[posicao]
        f.Nome = input("Informe o novo nome: ")
        f.Ano_Lancamento = int(input("Informe o novo ano de lançamento: "))
        f.Genero = input("Informe o novo gênero: ")
        f.Atores = input("Informe os novos atores: ")
        os.system("cls")
        print(f"Filme {f.Nome} alterado com sucesso!")

def Remover_Filme(Filmes):
    os.system("cls")
    codigo = input("Escreva o código do Filmes: ")
    Posicao_Remover = Buscar(Filmes, codigo)
    if Posicao_Remover == -1:
        print(f"Filme {codigo} não encontrado.")
    else:
        Remover(Filmes, Posicao_Remover)
        os.system("cls")
        print(f"Filme código {codigo} removido com sucesso!")

def Escreve_Arquivo_Filme(Filmes, Nome_Arquivo):
    arq = open(Nome_Arquivo, 'w')
    for f in Filmes:
        arq.write(f.Codigo + ';' + f.Nome + ';' + str(f.Ano_Lancamento) + ';' + f.Genero + ';' + f.Atores + '\n')
    arq.close()

def Le_Arquivo_Filme(Nome_Arquivo):
    Filmes = []
    arq = open(Nome_Arquivo, 'r')
    for linha in arq:
        texto = linha.split(';')
        f = Filmes()
        f.Codigo = texto[0]
        f.Nome = texto[1]
        f.Ano_Lancamento = texto[2]
        f.Genero = texto[3]
        f.Atores = texto[4]
        Filmes.append(f)
    arq.close()
    return Filmes