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


def procura (lista,element,index=0):
    if index >= len(lista):
        return -1
    if lista[index] == element:
        return index
        
    return  procura (lista, element, index + 1 ) 
    
    

lista = [4,3,5,6,7,8]
elemento = 8

test = procura(lista,elemento)
print(lista)


def buscaLInear (arr,elemento):
    n = elemento
    ponteiroInferior = 0
    ponteiroSuperior = len(arr) - 1

    while ponteiroInferior <= ponteiroSuperior:
        ponteiroMeio = (ponteiroInferior + ponteiroSuperior) // 2
        if (arr[ponteiroMeio] == n):
            return ponteiroMeio
        else:
            ponteiroSuperior != elemento
            return False

lista = [20,31,40,45,51]

elemento = int(input("Digite elemento que você deseja: "))

testUser = buscaLInear(lista,elemento)
print(testUser)
'''






        
