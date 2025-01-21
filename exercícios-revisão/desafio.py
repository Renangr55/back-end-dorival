'''
def mergeSort (lista):
    if len(lista) <= 1:
        return lista

    

    metade = len(lista) // 2

    parteEsquerda = lista[:metade]
    parteDireita = lista[-metade:]

    sorteandoEsquerda = mergeSort(parteEsquerda)
    sorteandoDireita = mergeSort(parteDireita)

    print(sorteandoEsquerda)
    print(sorteandoDireita)
    

    
    return merge (sorteandoEsquerda , sorteandoDireita)


def merge (esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(direita[j])
            j += 1
        else:
            resultado.append(esquerda[i])
            i += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

    
    
test = [2,1,51,5]
Sorteando = mergeSort(test)
print(Sorteando)
print("-------------------------------------")


def insertionSort (arr):
    n = len(arr)

    if n <= 1:
        return n
    
    for i in range (1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        return key



segundoTeste = [2,3,4,1,5,7,6,8,9,10]
insert = insertionSort(segundoTeste)
print(segundoTeste)


def bubleshots(arr):
    n = len(arr)


    for i in range (n):
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                
    return arr

test = [7,3,5,8,9,4]
aplly = bubleshots(test)
print(aplly)
'''

def procura (lista,element):
    for i in range(len(lista)):
        if (lista == element):
            return i

    return -1


def typing():
    kaka = []
    tamanho = int(input("Digite o tamanho: "))
    for i in range(tamanho):
        lista = int(input("Digite os numeros que você deseja "))
        kaka.append(lista)


def elemento ():
    tamanhoo = int(input("Digite o elemento que você deseja: "))
    return tamanhoo


test = procura(typing() ,elemento())
print(test)





        
