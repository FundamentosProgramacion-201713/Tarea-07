# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripción: Tarea 7, listas

def sumarNumsLista():
    listaX = [1,2,3,4,5]
    listaY = []
    y = 0
    for x in range(1, len(listaX)):
        y = x + y
        listaY.append(y)
    return listaY

def regresaLista():
    lista = [1,2,3,4,5]
    lista.remove(1)
    lista.remove(len(lista)+1)
    return lista

def verificaOrden():
    x = -1
    lista = []
    listaO = []
    while x != 0:
        x = int(input("escribe números enteros(0 para salir):", ))
        if x == 0:
            break
        lista.append(x)
        listaO.sort()
    return (lista == listaO)

def verificaAnagramas():
    palabra1 = "roma"
    palabra2 = "mora"
    lista1 = []
    lista2 = []
    for letrasP1 in palabra1:
        lista1.append(letrasP1)
        lista1.sort

    for letrasP2 in palabra2:
        lista2.append(letrasP2)
        lista2.sort

    return (lista1 == lista2)





def verificaDuplicados():
    lista = [1,2,3,4,2,4,5]
    for x in range(len(lista-1):
        if(lista.count(x) > 1):






        if x == 0:
            break
        lista.append(x)

    #y = lista.index(range(0, len(lista))

    #print(y)



def eliminaRepetidos():
    lista = [1,2,4,3,2,4,6]
    for x in lista:
        while lista.count(x)> 1:
            lista.remove(x)
    return lista


def main():
    sumarNumsLista()




main()
print("Ejercicio1")
print(sumarNumsLista())
print("Ejercicio2")
print(regresaLista())
print("Ejercicio3")
print(verificaOrden())
print("Ejercicio4")
print(verificaAnagramas())
print("Ejercicio5")

print("Ejercicio6")
print(eliminaRepetidos())

