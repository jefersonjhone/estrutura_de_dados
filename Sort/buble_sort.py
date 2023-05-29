"""
bubble sort é um dos métodos de ordenacao mais simples caracterizado por realizar sucessivas ordenações de pares


grau de complexidade = O²


"""


lista = [5,4,9,2,1,9,4,3,2,54,12,32,5,6,8,12]
for c in range(len(lista)):
    ordered = False
    for c in range(len(lista)-1):
        if lista[c] > lista[c+1]:
            lista[c], lista[c+1] = lista[c+1], lista[c]
        else:
            pass

print(lista)