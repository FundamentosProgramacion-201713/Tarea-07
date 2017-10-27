#encouding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#Tarea 7 : Utilizar las listas y demostrar diferentes cosas con ellas.

#Constantes para realizar pruebas con los ejercicios:
LISTA = [1, 2, 3, 4 ,5]
LISTA1= []
LISTA2= [5]
LISTA3= [1,2,3]
LISTA4= [1,2]
LISTA5= ["A","X", "B"]
LISTA6= "Roma"
LISTA7= "Mora"
LISTA8= "Hola"
LISTA9= "Hello"
LISTA10= [1,2, 3, 1, 4, 5]
LISTA11= [5, 4, 3, 2 ,1]
LISTA12= [1, 8, 3, 4, 3, 1, 8, 2, 7]
LISTA13= [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9]
LISTA14= [3, 1, 5, 3, 2, 6]
LISTA15= [4, 5, 4, 2, 3, 1, 2]
LISTA16= "Gato"
LISTA17= "Gota"

#Funcion que guarda los datos en una lista, a los datos nuevos se le suman los ya guardados.
def sumarAcumuladosLista(lista):
    numAcumulados=0
    listaNueva= []
    for x in range (len(lista)):
        numAcumulados += lista[x]
        listaNueva.append(numAcumulados)
    return listaNueva

#Funcion que quita de una lista los indices 0 y -1 (extremos).
def removerExtremos(lista):
    sinExtremos= lista[:]
    if len(sinExtremos) != 0:
        sinExtremos.remove(sinExtremos[0])
        sinExtremos.remove(sinExtremos[-1])
    else:
        sinExtremos= lista[:]
    return  sinExtremos

#Funcion que te dice si los datos dentro de una lista se encuentran ordenados.
def ordernarValores(lista):
    nuevalista= lista[:]
    nuevalista.sort()
    if nuevalista == lista:
        mensaje= True
    else:
        mensaje= False
    return  mensaje

#Funcion que dice si dos palabras forman un anagrama, osea que tienen las mismas letras.
def resolverAnagramas(lista, lista2):
    listaMayusculas= list(lista.upper())
    listaMayusculas2= list(lista2.upper())
    listaMayusculas.sort()
    listaMayusculas2.sort()
    if listaMayusculas == listaMayusculas2:
        mensaje= True
    else:
        mensaje= False
    return mensaje

#Funcion que determina si hay valores duplicados en una lista.
def calcularListaUnica(lista):
    listaunica= lista[:]
    for n in listaunica:
        if listaunica.count(n)>1:
            mensaje=True
        else:
            mensaje= False

        return mensaje

#Funcion que elimina los numeros repetidos dejando uno que cada uno.
def eliminarRepetidos(lista):
    for n in lista:
            while lista.count(n)>1:
                lista.remove(n)
    return lista

#Funcion principal donde se imprimen todas las funciones(ejemplos).
def main():

    #Ejemplos de la funcion sumarAcumuladosLista.
    print("Ejercicio 1: ")
    print("La lista ", LISTA, "regresa la lista acumulada ", sumarAcumuladosLista(LISTA))
    print("La lista ", LISTA1, "regresa la lista acumulada ", sumarAcumuladosLista(LISTA1))
    print("La lista ", LISTA11, "regresa la lista acumulada ", sumarAcumuladosLista(LISTA11))
    print("La lista ", LISTA2, "regresa la lista acumulada ", sumarAcumuladosLista(LISTA2))
    print("")

    #Ejemplos de la funcion removerExtremos.
    print("Ejercicio 2: ")
    print("La lista original ", LISTA1, "regresa ", removerExtremos(LISTA1))
    print("La lista original ", LISTA, "regresa ", removerExtremos(LISTA))
    print("La lista original ", LISTA14, "regresa ", removerExtremos(LISTA14))
    print("La lista original ", LISTA4, "regresa ", removerExtremos(LISTA4))
    print("")

    #Ejemplos de la funcion ordenarValores
    print("Ejercicio 3: ")
    print("Los valores de la lista ", LISTA5, "estan ordenados? ", ordernarValores(LISTA5))
    print("Los valores de la lista ", LISTA14, "estan ordenados? ", ordernarValores(LISTA14))
    print("Los valores de la lista ", LISTA13, "estan ordenados? ", ordernarValores(LISTA13))
    print("Los valores de la lista ", LISTA, "estan ordenados? ", ordernarValores(LISTA))
    print("")

    #Ejemplos de la funcion resolverAnagramas.
    print("Ejercicio 4: ")
    print("La palabra ", LISTA6, "y la palabra ",LISTA7, "forman un anagrama? ", resolverAnagramas(LISTA6, LISTA7))
    print("La palabra ", LISTA8, "y la palabra ", LISTA9, "forman un anagrama? ", resolverAnagramas(LISTA8, LISTA9))
    print("La palabra ", LISTA16, "y la palabra ", LISTA17, "forman un anagrama? ", resolverAnagramas(LISTA16, LISTA17))
    print("")

    #Ejemplos de la funcion calcularListaUnica.
    print("Ejercicio 5: ")
    print("De la lista ", LISTA, "hay duplicados? ", calcularListaUnica(LISTA))
    print("De la lista ", LISTA10, "hay duplicados? ", calcularListaUnica(LISTA10))
    print("De la lista ", LISTA12, "hay duplicados? ", calcularListaUnica(LISTA12))
    print("De la lista ", LISTA15, "hay duplicados? ", calcularListaUnica(LISTA15))
    print("")

    #Ejemplos de la funcion eliminarRepetidos.
    print("Ejercicio 6: ")
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA13))
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA15))
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA))
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA11))


main()
