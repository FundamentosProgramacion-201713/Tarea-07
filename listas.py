# encoding: utf-8
# autor: Iván Alejandro Dumas Martínez
# descripción:


def accumulateList(listA):
    listB = []
    a = 0
    for i in range (len(listA)):
        a += listA[i]
        listB.append(a)
    return listB


def deleteFrstAndLst(listA):
    return listA[1:(len(listA)-1)]


def checkIfOrdered(listA):
    result = False
    for i in range (len(listA)-1):
        if listA[i] < listA[i+1]:
            result = True
        else:
            result = False
    return result


def checkAnagram(listA, listB):
    listA = sorted(listA.upper())
    listB = sorted(listB.upper())
    result = False
    if listA == listB:
        result = True
    else:
        result = False
    return result


def checkIfRepeated(listA):
    result = True
    if listA == list(set(listA)):
        result = False
    return result


def cleanLists(listA):
    return list(set(listA))


def main():
    print("Ejercicio 1:")
    print("• La lista [1, 2, 3] regresa la lista acumulada", accumulateList([1, 2, 3]))
    print("• La lista [1, 2, 3, 4,5] regresa la lista acumulada", accumulateList([1, 2, 3, 4, 5]))
    print("• La lista [5] regresa la lista acumulada", accumulateList([5]))

    print("\nEjercicio 2:")
    print("• La lista origital [1, 2, 3, 4, 5], regresa", deleteFrstAndLst([1, 2, 3, 4, 5]))
    print("• La lista origital [1, 2, 3], regresa", deleteFrstAndLst([1, 2, 3]))
    print("• La lista origital [1, 2], regresa", deleteFrstAndLst([1, 2]))

    print("\nEjercicio 3:")
    print("• La lista [1, 2, 3] está ordenada de menor a mayor:", checkIfOrdered([1, 2, 3]))
    print("""• La lista ["A", "X", "A"] está ordenada de menor a mayor:""", checkIfOrdered(["A", "X", "A"]))
    print("""• La lista ["A", "B", "C"] está ordenada de menor a mayor:""", checkIfOrdered(["A", "B", "C"]))

    print("\nEjercicio 4:")
    print("""• Las cadenas "Roma" y "Mora" son anagramas:""", checkAnagram("Roma", "Mora"))
    print("""• Las cadenas "Hola" y "Hello" son anagramas:""", checkAnagram("Hola", "Hello"))
    print("""• Las cadenas "Brasil" y "Silbar" son anagramas:""", checkAnagram("Brasil", "Silbar"))

    print("\nEjercicio 5:")
    print("• La lista [1, 2, 3, 1, 4, 5] tiene algún digito duplicado:", checkIfRepeated([1, 2, 3, 1, 4, 5]))
    print("• La lista [1, 2, 3, 4, 5] tiene algún digito duplicado:", checkIfRepeated([1, 2, 3, 4, 5]))
    print("""• La lista ["A", "B", "A", "C", "D", "E"] tiene algún digito duplicado:""", checkIfRepeated(["A", "B", "A", "C", "D", "E"]))

    print("\nEjercicio 6:")
    print("• La lista [1, 8, 3, 4, 3, 1, 8, 2, 7] queda así después de eliminar los datos repetidos:", cleanLists([1, 8, 3, 4, 3, 1, 8, 2, 7]))
    print("• La lista [1, 8, 3, 4, 3, 1, 8, 2, 7, 9] queda así después de eliminar los datos repetidos:", cleanLists([1, 8, 3, 4, 3, 1, 8, 2, 7, 9]))
    print("• La lista [1, 1, 1, 1, 2, 3] queda así después de eliminar los datos repetidos:", cleanLists([1, 1, 1, 1, 2, 3]))


main()