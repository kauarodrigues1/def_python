
lista = []
i = 0
while i < 5:
    p = str(input('Digite uma palavra: '))
    lista.append(p)
    i += 1

def longa(lista):
    palavras_curtas = []
    palavras_longas = []
    
    for palavra in lista:
        if len(palavra) < 5:
            palavras_curtas.append(palavra)
        else:
            palavras_longas.append(palavra)
    return palavras_curtas, palavras_longas
pcurta, plonga = longa(lista)
            
print('Lista de palavras curtas: ',pcurta)
print('Lista de palavras longas: ',plonga)
            
#O codigo inicia com um loop para fazer o input e dar append na lista,
# depois a função separa as palavras curtas(menor que 5 caracteres)
# das palavras longas(maior que 5 caracteres) e da print nas duas listas
