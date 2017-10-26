#Autor: Leonardo Castillejos Vite
#encode: UTF-8
#Descripción:

'''
Función que suma los números de una lista, en una serie.
'''
def sumarLista(lista):
    listasum = []
    suma = 0
    for i in lista:
        suma += i
        listasum.append(suma)
    return listasum

'''
Función que quita los extremos de una lista
'''

def quitarExtremos(lista):
    if lista == []:
        return []
    elif len(lista) == 1:
        lista.remove(lista[0])
        return lista
    else:
        lista.remove(lista[0])
        lista.remove(lista[len(lista)-1])
        return lista

'''
Le dice al usuario si una lista dada por el usuario está de menor a mayor
'''
def comprobarOrden(lista):
    listaOrden = []
    for i in lista:
        listaOrden.append(i)
    listaOrden.sort()
    if listaOrden == lista:
        return True
    else:
        return False

'''
Ld dice al usuario si 2 cadenas comparten las mismas letras
'''
def esAnagrama(cadena1,cadena2):
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    palabra1 = list(cadena1)
    palabra2 = list(cadena2)
    palabra1.sort()
    palabra2.sort()
    if palabra1 == palabra2:
        return True
    else:
        return False

'''
Función que le dice al usuario si hay dos o más de un dígito en una lista
'''
def esDuplicado(lista):
    listaUnica = []
    for i in lista:
        if i not in listaUnica:
            listaUnica.append(i)
    if listaUnica == lista:
        return False
    else:
        return True

'''
Función que elimina los dígitos repetidos en una lista
'''
def eliminarRepetido(lista):
    lista.reverse()
    for k in lista:
        if lista.count(k) > 1:
            lista.remove(lista[lista.index(k)])
    lista.reverse()
    return lista



'''
Función que prueba las funciones anteriores en diferentes escenarios
'''
def main():
    print("Ejercicio 1")
    print(" ", u'\u2022', "La lista [1,2,3,4,5] regresa la lista acumulada ", sumarLista([1,2,3,4,5]))
    print(" ", u'\u2022', "La lista [] regresa la lista acumulada ", sumarLista([]))
    print(" ", u'\u2022', "La lista [1,3,5,7] regresa la lista acumulada ", sumarLista([1, 3, 5, 7]))
    print("Ejercicio 2")
    print(" ", u'\u2022', "Lista original [1,2,3,4,5], regresa ", quitarExtremos([1,2,3,4,5]))
    print(" ", u'\u2022', "Lista original [1,2,3], regresa ", quitarExtremos([1, 2, 3]))
    print(" ", u'\u2022', "Lista original [], regresa ", quitarExtremos([]))
    print("Ejercicio 3")
    print(" ", u'\u2022', "La lista original [1,2,3,4,5] ¿ Está ordenada? ", comprobarOrden([1,2,3,4,5]))
    print(" ", u'\u2022', "La lista original [1,2,4,3,5] ¿ Está ordenada? ", comprobarOrden([1, 2, 4, 3, 5]))
    print(" ", u'\u2022', "La lista original [1,2,3,2,5] ¿ Está ordenada? ", comprobarOrden([1, 2, 3, 2, 5]))
    print("Ejercicio 4")
    print(" ", u'\u2022', "Las palabras Roma y Mora ¿ Son anagramas? ", esAnagrama("Roma","Mora"))
    print(" ", u'\u2022', "Las palabras Roma y Mora ¿ Son anagramas? ", esAnagrama("Hola", "Hello"))
    print("Ejercicio 5")
    print(" ", u'\u2022', "La lista original [1,2,3,4,5] ¿ Tiene duplicados? ", esDuplicado([1,2,3,4,5]))
    print(" ", u'\u2022', "La lista original [1,2,2,4,5] ¿ Hay duplicados? ", esDuplicado([1,2,2,4,5]))
    print("Ejercicio 6")
    print(" ", u'\u2022', "La lista original [1,2,3,3,5,2,6] , sin duplicados ", eliminarRepetido([1,2,3,3,5,2,6]))
    print(" ", u'\u2022', "La lista original [1,8,3,4,3,1,8,2,7] , sin duplicados ", eliminarRepetido([1,8,3,4,3,1,8,2,7]))
main()


