# encoding: UTF-8
# Autor: Luis Alfonso Alcántara

# Función para crear una lista con la suma acumulada
def acumularSuma(lista):
    suma = 0
    nuevaLista = lista[:]
    for x in range(len(nuevaLista)):
        suma += nuevaLista[x]
        nuevaLista[x] = suma
    return nuevaLista

# Función para eliminar el primer y último elemento de una lista
def eliminarPrimerUltimoElemento(lista):
    nuevaLista = lista[:]
    nuevaLista.remove(nuevaLista[0])
    nuevaLista.remove(nuevaLista[len(nuevaLista)-1])
    return nuevaLista

# Función para verificar si una lista está ordenada
def estarOrdenados(lista):
    ordenado = True
    menor = lista[0]
    for dato in lista:
        if dato < menor:
            ordenado = False
        menor = dato
    return ordenado

# Función para verificar si dos palabras son anagramas
def serAnagrama(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    listaCadena1 = list(cadena1)
    listaCadena2 = list(cadena2)
    anagrama = True
    for letter2 in listaCadena2:
        if not letter2 in listaCadena1 or listaCadena1.count(letter2) != listaCadena2.count(letter2):
            anagrama = False

    return anagrama

# Función para verificar si hay datos duplicados
def estarDuplicado(lista):
    duplicado = False
    for dato in lista:
        if lista.count(dato) > 1:
            duplicado = True
    return duplicado

#Función para verificar si hay datos duplicados y crear una lista con valores únicos
def eliminarDuplicados(lista):
    for dato in lista:
        if lista.count(dato) > 1:
            lista.remove(dato)
    return lista

# Función para mostrar varios ejemplos de las funciones hechas
def main():
    print("Ejercicio 1:")
    lista = [1, 2, 3, 4]
    print("     La lista",lista, "regresa la lista acumulada", acumularSuma(lista))
    print("     La lista",[9,8,7,6], "regresa la lista acumulada", acumularSuma([9,8,7,6]))

    print("\nEjercicio 2:")
    lista = [1, 2, 3, 4]
    print("     Lista original", lista, "regresa", eliminarPrimerUltimoElemento(lista))
    print("     Lista original", [2,3,1,9], "regresa", eliminarPrimerUltimoElemento([2,3,1,9]))

    print("\nEjercicio 3:")
    lista = [1, 2, 3, 4]
    print("     ",lista,"está ordenada:",estarOrdenados(lista))
    print("     ",[3, 4, 1, 2],"está ordenada:",estarOrdenados([3, 4, 1, 2]))

    print("\nEjercicio 4:")
    str1 = "hola"
    str2 = "aloh"

    print("     ",str1,"y",str2,"son anagramas:", serAnagrama(str1, str2))
    print("     ","hOla","y","hola","son anagramas:", serAnagrama("hOla", "hola"))
    print("     ", "hola","y","hello","son anagramas:", serAnagrama("hola", "hello"))

    print("\nEjercicio 5:")
    lista = [1,2,3,4,5]
    print("     ", lista,"está duplicado:",estarDuplicado(lista))
    print("     ",[1,1,2,3,4,5],"está duplicado:",estarDuplicado([1,1,2,3,4,5]))

    print("\nEjercicio 6:")
    lista = [1, 2, 3, 4, 5]
    print("     ", lista, "se convierte en", eliminarDuplicados(lista))
    print("     ", [1,1,2,3,2,7,9], "se convierte en", eliminarDuplicados([1,1,2,3,2,7,9]))

main()