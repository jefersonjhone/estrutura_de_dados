"""
bubble sort é um dos métodos de ordenacao mais simples caracterizado por realizar sucessivas ordenações de pares


grau de complexidade = O(N²)


"""
def bubble_sort(lista:list ) -> list :
    for b in range(len(lista)):
        mudou = False
        for c in range(len(lista)-1):
            if lista[c] > lista[c+1]:
                lista[c], lista[c+1] = lista[c+1], lista[c]
                mudou = True
        else:
            if not (mudou):
                print(b+1)
                return lista
    else:
        return lista

