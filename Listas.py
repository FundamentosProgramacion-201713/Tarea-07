#encoding: UTF-8
#Autor: Omar Israel Galván García A01745810
#Este programa consiste en varias funciones en las que se usan listas

def sumarValores (lista01):  #crea la función para sumar valores
    lista11 = []  #lista vacía
    contador = 0  #contador inicializado en cero
    for i in lista01:     #ciclo for para visitar cada valor de la lista
        contador += i      # contador aumenta en 1 cada vez que pasa
        lista11.append(contador)  #se agrega el valor de contador a la nueva lista vacía
    return lista11  #regresa la lista con los nuevos valores

def eliminarExtremos(lista02):
    lista22 = list(lista02)  #se asigna una nueva variable a la lista
    lista22.remove(lista02[0])   #remueve la posición inicial 0
    lista22.remove(lista02[-1])   # remueve la posición final -1
    return lista22  #regresa la lista ya modificada


def ordenarValores(lista03):
    valor = True     #variable de estado
    lista33 = list(lista03)  #asignación a una nueva lista vacía
    lista30 = list(lista33)  #asignación a una nueva lista vacía
    lista30.sort()           #ordena los valores en orden creciente
    if lista33 == lista30:   #condicional
        valor = True        #valor verdadero
    else:
        valor = False       #valor falso
    return valor   #regresa el estado de la función

def analizarAnagramas(cadena00,cadena01):

    palabra1 = cadena01.upper()   #convierte la cadena a mayúsculas
    palabra2 = cadena00.upper()
    lista04 = list(palabra1)  #se asigna a una nueva lista vacía
    lista44 = list(palabra2)
    lista04.sort()   # ordena los valores en orden creciente
    lista44.sort()

    if lista04 == lista44:
        valor = True
    else:
        valor = False
    return valor

def verificarDuplicado(lista05):
    nuevaLista = list(lista05)   #asignación a una nueva lista
    for i in nuevaLista:
        if nuevaLista.count(i)>1:   #cuenta en el índice i si se repite algún número o valor
            valor = True
        else:
            valor = False
    return valor      #regresa el estado




def eliminarRepetido(lista06):
    for i in lista06:               #se examina toda la lista
        while lista06.count(i)>1:    #mientras que haya un número repetido
            lista06.remove(i)       #elimina los repetidos
    return lista06



def main():
    print("\n")
    print("Ejercicio 1...")
    print("La lista [1,2,3,4,5] regresa la lista acumulada",sumarValores([1,2,3,4,5]) )
    print("La lista [] regresa la lista acumulada", sumarValores([]))
    print("La lista [5] regresa la lista acumulada", sumarValores([5]))
    print("La lista [10,9,8,7,6,5] regresa la lista acumulada", sumarValores([10,9,8,7,6,5]))
    print("\n")

    print("Ejercicio 2...")
    print("Lista original [1,2,3,4,5], regresa",eliminarExtremos([1,2,3,4,5]))
    print("Lista original [10,11,12,13,14], regresa", eliminarExtremos([10,11,12,13,14]))
    print("Lista original [7,1,2,5,8], regresa", eliminarExtremos([7,1,2,5,8]))
    print("Lista original [20,35,2,1], regresa", eliminarExtremos([20,35,2,1]))
    print("\n")

    print("Ejercicio 3...")
    print("La lista [1,2,3,4,5]) está en orden: ",ordenarValores([1,2,3,4,5]))
    print("La lista [7,10,5,2,8]) está en orden: ", ordenarValores([7,10,5,2,8]))
    print("La lista ['a','z','c']) está en orden: ", ordenarValores(["a","z","c"]))
    print("La lista ['a','b','c']) está en orden: ", ordenarValores(["a","b","c"]))
    print("\n")

    print("Ejercicio 4...")
    print("La palabra 'mora' y 'roma' son anagramas: ",analizarAnagramas("mora","roma"))
    print("La palabra 'ciruela' y 'relucia' son anagramas: ", analizarAnagramas("ciruela", "relucia"))
    print("La palabra 'comida' y 'cena'son anagramas: ", analizarAnagramas("comida", "cena"))
    print("La palabra 'ancestro' y 'cartones son anagramas: ", analizarAnagramas("ancestro", "cartones"))
    print("\n")

    print("Ejercicio 5...")
    print("En la lista [1,2,3,4,5] hay números repetidos: ",verificarDuplicado([1,2,3,4,5]))
    print("En la lista [1,2,2,2,3,4,5,5] hay números repetidos: ", verificarDuplicado([1,2,2,2,3,4,5,5]))
    print("En la lista [10,11,12,13,14] hay números repetidos: ", verificarDuplicado([10,11,12,13,14]))
    print("En la lista [2,8,8,7,5,6,6] hay números repetidos: ", verificarDuplicado([2,8,8,7,5,6,6]))
    print("\n")

    print("Ejercicio 6...")
    print("La lista original [1,5,8,9,10] regresa",eliminarRepetido([1,5,8,9,10]))
    print("La lista original [1,5,5,5,8,9,10] regresa", eliminarRepetido([1,5,5,5,8,9,10]))
    print("La lista original [1,2,2,2,2,4,5] regresa", eliminarRepetido([1,2,2,2,2,4,5]))
    print("La lista original [2,3,10,9,8] regresa", eliminarRepetido([2,3,10,9,8]))

    print("\n")
    '''
    print("Pruebas generales: ")
    print(sumarValores([1, 2, 3]))
    print(eliminarExtremos([1, 2, 3, 4, 5]))
    print(ordenarValores([1, 2, 3, 4, 5, 6, 7, 8]))
    print(analizarAnagramas("hola", "hello"))
    print(verificarDuplicado([1, 2, 3, 4, 4]))
    print(eliminarRepetido([2, 3, 3, 4, 5, 5, 5, 6]))
    '''

main()
