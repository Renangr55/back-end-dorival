'''

exercício 1

primeiroNumero = float(input("Digite um número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
print(soma)

exercicio 2

nome = input("Digite seu nome: ")
ano_de_nascimento = int(input("Digite o ano de nascimento: "))

print(f'seu nome é {nome},você nasceu em {ano_de_nascimento} e sua idade é {2025 - ano_de_nascimento } ')


exercicio 3
numeroUsuario = int(input("Digite um número: "))

if numeroUsuario % 2 == 0:
    print("esse número e par")
else:
    print("Esse número é impar")


exercicio 4
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite  sua terceira nota: "))
nota4 = float(input("digite sua qufloata nota: "))
nota5 = float(input("digite sua qufloata nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if media >= 2.5 and media < 5:
    print("Recuperação")
elif media < 2.5:
    print("reprovado")
elif media >= 5:
    print("APROVADO")
else:
    print("insira uma nota válida")

exercicio 5

numeroPositivo = int(input("Digite um número: "))

for i in range (0,numeroPositivo + 1,1):
    print(i)

contador = []

exercicio 6

num = 0

while num >= 0:
    num = int(input("Digite um número: "))
    contador.append(num)
    if num < 0:
        print("Você digitou um número negativo")
        break
    
print(max(contador))


def inverterString (s):
    for i in s:
        print(i)
          
print(inverterString(reversed("renan")))




def contar_letras(string):

    for char in string:
        if char in dicionario_string:
            dicionario_string[char] += 1
        else:
            dicionario_string[char] = 1

dicionario_string = {}

string = input('digite alguma coisa: ')

contar_letras(string)

print(dicionario_string)






print("-------------------------------------")
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
'''

def insertionSort (arr):
    n = len(arr)

    if n <= 1:
        return n

    

