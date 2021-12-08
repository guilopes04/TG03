def Remover(Lista, Posicao_Remover):
    i = Posicao_Remover
    while i < len(Lista):
        Lista[i] = Lista[i - 1]
        i += 1
        Lista.pop()

def Buscar(Lista, codigo):
    i = 0
    while i < len(Lista):
        L = Lista[i]
        if L.Codigo == codigo:
            return i
        i += 1
    return -1

def Buscar_Sessao_Data(Lista, data):
    i = 0
    while i < len(Lista):
        L = Lista[i]
        if L.Data == data:
            return i
        i += 1
    return -1

def Buscar_Sessao_Horario(Lista, horario):
    i = 0
    while i < len(Lista):
        L = Lista[i]
        if L.Horario == horario:
            return i
        i += 1
    return -1
