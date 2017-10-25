#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que realiza diferentes tipos de preubas con listas


#Funcion que suma los elemenos de una lista acumulandolos
def sumaracumuladoslistas(lista):
    sumaacumulada = 0
    listasumas = []
    for x in lista:
         sumaacumulada += x
         listasumas.append(sumaacumulada)
    return listasumas

#Funcion que elimina el primer y último elemento
def eliminarextremoslistas(lista):
    if len(lista) >=2 :
        lista.pop()
        listanueva = lista[::-1]
        listanueva.pop()
        listasinext = listanueva[::-1]
        return listasinext
    else:
        return []

#funcion que compueba si los elementos de una lista estan en orden
def comprobarordenlistas(lista):
    lista2 = lista[:]
    lista2.sort()
    if lista == lista2:
        return True
    else:
        return False

#Funcion que comprueba si una cadena es una anagrama de otra
def comprobaranagramas(cadena1,cadena2):
    listacad1 = list(cadena1.lower())
    listacad2 = list(cadena2.lower())
    listacad1.sort()
    listacad2.sort()
    if listacad1 == listacad2:
        return True
    else:
        return False

#Funcion que determina si la lista contiene duplicados
def determinarduplicados(lista):
    lista2 = []
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    if lista == lista2:
        return False
    else:
        return True

#Funcion que elimina los duplicados en una lista
def removerduplicados(lista):
    lista2 = []
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    lista = lista2
    return lista




def main():
    #Ejercicio 1
    print("---EJERCICIO 1---")
    print("la lista", [1,2,3,4,5],",regresa la lista acumulada", sumaracumuladoslistas([1,2,3,4,5]))
    print("la lista", [1,3,5,7,9], ",regresa la lista acumulada", sumaracumuladoslistas([1,3,5,7,9]))
    print("la lista", [5], ",regresa la lista acumulada", sumaracumuladoslistas([5]))
    print("la lista", [], ",regresa la lista acumulada", sumaracumuladoslistas([]))
    #Ejercicio 2
    print("---EJERCICIO 2---")
    print("la lista", [1, 2, 3, 4, 5], ",regresa la lista", eliminarextremoslistas([1, 2, 3, 4, 5]))
    print("la lista", [1, 3, 5, 7, 9], ",regresa la lista", eliminarextremoslistas([1, 3, 5, 7, 9]))
    print("la lista", [5], ",regresa la lista", eliminarextremoslistas([5]))
    print("la lista", [], ",regresa la lista", eliminarextremoslistas([]))
    #Ejercicio 3
    print("---EJERCICIO 3---")
    print("la lista", [1, 2, 3, 4, 5], "está ordenada:", comprobarordenlistas([1, 2, 3, 4, 5]))
    print("la lista", ["A","X","B"], "está ordenada:", comprobarordenlistas(["A","X","B"]))
    print("la lista", [2,4,6,8,12,34], "está ordenada:", comprobarordenlistas([2,4,6,8,12,34]))
    print("la lista", [25,4,12,64], "está ordenada:", comprobarordenlistas([25,4,12,64]))
    #Ejercicio 4
    print("---EJERCICIO 4---")
    print("La cadena %s y %s son anagramas:" % ("Roma", "Mora"), comprobaranagramas("Roma", "Amor"))
    print("La cadena %s y %s son anagramas:" % ("Hola", "Hello"), comprobaranagramas("Hola", "Hello"))
    print("La cadena %s y %s son anagramas:" % ("Sacar", "Casar"), comprobaranagramas("Sacar", "Casar"))
    print("La cadena %s y %s son anagramas:" % ("papel", "paper"), comprobaranagramas("papel", "paper"))
    #Ejercicio 5
    print("---EJERCICIO 5---")
    print("La lista", [1,2,3,1,4,5], "contiene elementos repetidos:", determinarduplicados([1,2,3,1,4,5]))
    print("La lista", [5,4,3,2,1], "contiene elementos repetidos:", determinarduplicados([5,4,3,2,1]))
    print("La lista", [1,1,2,2,3,3,4,5,6,7,7], "contiene elementos repetidos:", determinarduplicados([1,1,2,2,3,3,4,5,6,7,7]))
    #Ejercicio 6
    print("---EJERCICIO 6---")
    print("La lista", [1, 2, 3, 1, 4, 5], "sin elementos repetidos es:", removerduplicados([1, 2, 3, 1, 4, 5]))
    print("La lista", [1,8,3,4,3,1,8,2,7], "sin elementos repetidos es:", removerduplicados([1,8,3,4,3,1,8,2,7]))
    print("La lista", [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7], "sin elementos repetidos es:",removerduplicados([1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7]))








main()