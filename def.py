#Ex 1 - Cálculo de média

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

lista = [10, 5, 3, 4, 10]

print(calcular_media(lista))

##########################################

#Ex 2 - Determinar man e min 

def min_max(lista):
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo

print(min_max(lista))

x, y = min_max(lista)

print(f"O valor minimo é {x}")

###########################################

#Ex 3 - 

def contar_elementos(lista, elemento):
    contar = lista.count(elemento)
    
    return contar

numeros = [1, 2, 3, 4, 5, 1, 2, 3]
alvo = 3

print(contar_elementos(numeros, alvo))
#############################################
#Ex 4 
def inverter_lista(lista):
    inverter = lista[::-1]
    return inverter

numeros = [1, 2, 3, 4, 5]
print(inverter_lista(numeros))
############################################
#Ex 5 
def ordenar_lista(lista):
    return lista == sorted(lista)

numeros = [1, 2, 3, 4, 5]
print(ordenar_lista(numeros))

############################################

#Ex 6 
def remover_numeros_duplicados(lista):
    remover = list(set(lista))
    return remover

numeros = [6, 1, 2, 1, 3, 2, 4, 5, 5]
sem_valores_duplicados = remover_numeros_duplicados(numeros)
print(sem_valores_duplicados)

###########################################
#Ex 7 retornar numeros positivos e negativos de uma lista

def positivo_negativo(lista):
    positivos = [num for num in lista if num > 0]
    negativos = [num for num in lista if num < 0]

    return positivos, negativos
    #return devolve em tupla

numeros = [10, -1, -2, 3, 2, -4, 5]

print(positivo_negativo(numeros))

lista_positivos, lista_negativos = positivo_negativo(numeros)

print(lista_positivos)
print(lista_negativos)
##########################################

#Ex 8 - calcular a soma dos quadrados de uma lista 
lista2 = [2, 2, 2, 2]
def soma_quadrado(lista):
    eleva_quadrado = sum(num ** 2 for num in lista)
    return eleva_quadrado
print(soma_quadrado(lista))

#Ex 9 - separa palavras curtas

def separar_palavras(lista):
    palavras_curtas = []
    palavras_longas = []
    
    for palavra in lista:
        if len(palavra) < 5:
            palavras_curtas.append(palavra)
        else:
            palavras_longas.append(palavra)
    return palavras_curtas, palavras_longas
    
lista_palavras = ['sol', 'montanha', 'neve', 'lua', 'floresta', 'ceu']

print(separar_palavras(lista_palavras))
##########################################

#ex10 - Função calcular soma de 3 numeros ao quadrado

#subalgoritimos

#criar função quadrado

def quadrado(x):
    quadrado = x*x
    return quadrado

def soma_quadrados(x, y, z):
    a = quadrado(x)
    b = quadrado(y)
    c = quadrado(z) 
    soma = a + b + c
    return soma

print(soma_quadrados(2, 3, 5))
    
    
    
    
    
    
    
    
    
    
    
    
    










































