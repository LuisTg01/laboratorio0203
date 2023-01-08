import random

def desordenar_lista(lista_original):
    
    lista = lista_original[:]
    
    longitud_lista = len(lista)

    for i in range(longitud_lista):

        indice_aleatorio = random.randint(0, longitud_lista - 1)
        # Intercambiar
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
        
    return lista


lista = [3, 4, 5, 6, 7]
lista_mezclada = desordenar_lista(lista)

print(lista_mezclada)