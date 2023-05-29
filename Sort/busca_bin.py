import time

lista = [c for c in range(10000)]

def timer(func):
    inicio = time.time()
    func(9990,lista)
    print((time.time() - inicio)*10**4)

def busca_sequencial(iten,lista):
    for i in range(len(lista)):
        if lista[i] == iten:
            return i


def busca_binaria(iten,lista):
    meio = len(lista) // 2
    if iten > lista[meio]:
        return busca_binaria(iten,lista[meio:])
    elif iten < meio:
        return busca_binaria(iten,lista[:meio])
    else:
        return meio

timer(busca_binaria)
timer(busca_sequencial)