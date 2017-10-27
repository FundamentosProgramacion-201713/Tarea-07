#encoding: UTF-8
#Autor: Daniel Sahuer
#Programa que resuelve 6 ejercicios usando listas


def sumaAcumulada (lista1): #Ejercicio 1: se calcula la suma de números acumulados en una lista

    listaSum = []
    suma = 0
    for i in lista1:
        suma = suma + i
        listaSum.append(suma)

    return listaSum


def listaSinExtremos(lista): #Ejercicio 2: se regresa una nueva lista sin el valor inicial y el final

    if len(lista) > 1:

        del lista[0]
        del lista[len(lista)-1]

    else:
        return[]

    return lista


def listasTrue(lista): #Ejercicio 3: analiza si los valores de la lista están en orden

    orden = lista[:]

    orden.sort()

    if lista == orden:
        return True
    else:
        return False


def listasAnagrama(palabra1,palabra2): #Ejercicio 4: se verifica si dos cadenas son anagramas
    palabra1 = palabra1.upper()
    palabra2 = palabra2.upper()

    pal1 = list(palabra1)
    pal2 = list(palabra2)

    pal1.sort()
    pal2.sort()

    if pal1 == pal2:
        return True
    else:
        return False


def listaDuplicados(lista): #Ejercicio 5: se verifica si hay valores repetidos en la lista

    for i in lista:

        if lista.count(i) > 1:
            return True
        else:
            return False


def listaEliminarDuplicados(lista): #Ejercicio 6: se eliminan valores repetidos en la lista
    for i in lista:

        if lista.count(i) > 1:

            lista.remove(i)

    return lista



def main():

    lista = [1,2,3,4,5]
    lista1 = []
    lista2 = [5]
    lista3 = ['a','x','b']
    lista4 = ['a','b','c']
    lista5 = [1,4,5,2]
    lista6 = [1,2,3,1,4,5]
    lista7 = [1,8,3,4,3,1,8,2,7]

    palabra1 = ("Amor")
    palabra2 = ("Roma")
    palabra3 = ("Hola")
    palabra4 = ("Hello")

    print("Ejercicio 1:\n   La lista %s regresa la lista acumulada %s" % (lista,sumaAcumulada([1,2,3,4,5])))
    print("   La lista %s regresa la lista acumulada %s" % (lista1,sumaAcumulada(lista1)))
    print("   La lista %s regresa la lista acumulada %s" % (lista2, sumaAcumulada(lista2)))

    print("\nEjercicio 2:\n   La lista %s regresa %s" % (lista,listaSinExtremos([1,2,3,4,5])))
    print("   La lista %s regresa %s" % (lista1,listaSinExtremos(lista1)))
    print("   La lista %s regresa %s" % (lista2, listaSinExtremos(lista2)))

    print("\nEjercicio 3:\n   La lista %s regresa %s" % (lista3,listasTrue(lista3)))
    print("   La lista %s regresa %s" % (lista4,listasTrue(lista4)))
    print("   La lista %s regresa %s" % (lista, listasTrue([1,2,3,4,5])))
    print("   La lista %s regresa %s" % (lista5,listasTrue(lista5)))

    print("\nEjercicio 4:\n   La cadenas %s y %s ¿son anagramas? %s" % (palabra1,palabra2,listasAnagrama(palabra1,palabra2)))
    print("   La cadenas %s y %s ¿son anagramas? %s" % (palabra3,palabra4,listasAnagrama(palabra3,palabra4)))

    print("\nEjercicio 5:\n   La lista %s regresa %s" % (lista6,listaDuplicados(lista6)))
    print("   La lista %s regresa %s" % (lista,listaDuplicados([1,2,3,4,5])))

    print("\nEjercicio 6:\n   La lista %s regresa %s" % ([1,8,3,4,3,1,8,2,7],listaEliminarDuplicados(lista7)))
    print("   La lista %s regresa %s" % (lista,listaEliminarDuplicados([1,2,3,4,5])))


main()