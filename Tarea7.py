#Autor: Ernesto Ibhar Guevara Gomez
#enconding :UTF-8
#A01746121
#Programa que sirve para resolver diferentes ejercicios con listas.
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

def sumarAcumuladosLista(lista): #Funcion que realizan la operacion de sumar los datos acumulados con los datos d ela lista normal
    numAcumulados=0
    listaNueva= []
    for k in range (len(lista)):
        numAcumulados += lista[k]
        listaNueva.append(numAcumulados)
    return listaNueva

def removerExtremos(lista): #Funcion que quita el primer y ultimo valor
    quitaExtremos= lista[:]
    if len(quitaExtremos) != 0:
        quitaExtremos.remove(quitaExtremos[0])
        quitaExtremos.remove(quitaExtremos[-1])
    else:
        quitaExtremos= lista[:]
    return  quitaExtremos

def ordernarValores(lista): #Funcion que dice si los valores estan ordenados de manera correcta
    nuevalista= lista[:]
    nuevalista.sort()
    if nuevalista == lista:
        mensaje= True
    else:
        mensaje= False
    return  mensaje

def resolverAnagramas(lista, lista2): #Funcion que te dice si las palabras que estan en las listas son anagramas o no
    listaMayusculas= list(lista.upper())
    listaMayusculas2= list(lista2.upper())
    listaMayusculas.sort()
    listaMayusculas2.sort()
    if listaMayusculas == listaMayusculas2:
        mensaje= True
    else:
        mensaje= False
    return mensaje

def calcularListaUnica(lista): #Funcion que te dice si hay fuplicados en la lista
    listaunica= lista[:]
    for n in listaunica:
        if listaunica.count(n)>1:
            mensaje=True
        else:
            mensaje= False

        return mensaje

def eliminarRepetidos(lista): #Funcon que elimina los numeros duplicados de la lista.
    for n in lista:
            while lista.count(n)>1:
                lista.remove(n)
    return lista


def main():
    #Ejemplos de como el programa funciona
    print("Ejercicio 1: ")
    print("La lista ", LISTA, "regresa la lista acumulada ", sumarAcumuladosLista(LISTA))
    print("Ejercicio 2: ")
    print("La lista original ", LISTA1, "regresa ", removerExtremos(LISTA1))
    print("La lista original ", LISTA, "regresa ", removerExtremos(LISTA))
    print("La lista original ", LISTA14, "regresa ", removerExtremos(LISTA14))
    print("La lista original ", LISTA4, "regresa ", removerExtremos(LISTA4))
    print("Ejercico 3: ")
    print("Los valores de la lista ", LISTA5, "estan ordenados? ", ordernarValores(LISTA5))
    print("Los valores de la lista ", LISTA14, "estan ordenados? ", ordernarValores(LISTA14))
    print("Los valores de la lista ", LISTA13, "estan ordenados? ", ordernarValores(LISTA13))
    print("Ejercicio 4: ")
    print("La palabra ", LISTA6, "y la palabra ",LISTA7, "forman un anagrama? ", resolverAnagramas(LISTA6, LISTA7))
    print("La palabra ", LISTA8, "y la palabra ", LISTA9, "forman un anagrama? ", resolverAnagramas(LISTA8, LISTA9))
    print("La palabra ", LISTA16, "y la palabra ", LISTA17, "forman un anagrama? ", resolverAnagramas(LISTA16, LISTA17))
    print("Ejercico 5: ")
    print("De la lista ", LISTA, "hay duplicados? ", calcularListaUnica(LISTA))
    print("De la lista ", LISTA10, "hay duplicados? ", calcularListaUnica(LISTA10))
    print("Ejercicio 6: ")
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA13))
main()