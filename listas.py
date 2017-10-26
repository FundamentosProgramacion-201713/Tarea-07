def sumarLista(lista):
    listaSumada = 0
    nueva_lista = []
    for i in lista:
        listaSumada+= i
        nueva_lista.append(listaSumada)
    return nueva_lista

def eliminarPrimeroUltimo(lista):
    nueva_lista = lista [::-1]
    nueva_lista.pop()
    nueva_lista.reverse()
    nueva_lista = nueva_lista[0::]
    nueva_lista.pop()
    return nueva_lista

def comprobarOrden(lista):
    lista_original = lista [::]
    lista.sort()
    nueva_lista = lista
    if lista_original == nueva_lista:
        return True
    else:
        return False

def esAnagrama(cadena1, cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    original1 = list(cadena1)
    original2 = list(cadena2)
    original1.sort()
    original2.sort()
    if original1 == original2:
        return True
    else:
        return False

def detectarDuplicado(lista):
    for i in lista:
        repetido = lista.count(i)
        if repetido > 1:
            return True
        else:
            return False

def eliminarDuplicado(lista):
   for dato in lista:
       if lista.count(dato) > 1:
           lista.remove(dato)
   return lista

def main():
    print("Ejercicio 1")
    lista = [1,2,3,4]
    lista2 = [9,8,7,6]
    print("La lista",lista, "regresa la lista acumulada", sumarLista(lista))
    print("La lista", lista2, "regresa la lista acumulada", sumarLista(lista2))
    print()
    print("Ejercicio 2")
    lista = [5,6,7,8]
    lista2 = [11,12,13,14,15]
    print("La lista", lista, "regresa la lista sin extremos", eliminarPrimeroUltimo(lista))
    print("La lista", lista2, "regresa la lista sin extremo", eliminarPrimeroUltimo(lista2))
    print()
    print("Ejercicio 3")
    lista = [1,2,3,4]
    lista2 = [5,1,2,4,3]
    print("La lista", lista, "¿esta ordenada?", comprobarOrden(lista))
    print("La lista", lista2, "¿esta ordenda?", comprobarOrden(lista2))
    print()
    print("Ejercicio 4")
    lista = "Amor"
    lista2 = "Roma"
    lista3 = "Hola"
    lista4 = "Hello"
    print("Las listas", lista, lista2, "¿son anagramas?", esAnagrama(lista,lista2))
    print("Las listas", lista3, lista4, "¿son anagramas?", esAnagrama(lista3,lista4))
    print()
    print("Ejercicio 5")
    lista = [1, 2, 3, 4]
    lista2 = [1,2,3,2,4,5,6,1]
    print("La lista", lista, "¿tiene duplicados?", detectarDuplicado(lista))
    print("La lista", lista2, "¿tiene duplicados?", detectarDuplicado(lista2))
    print()
    print("Ejercicio 6")
    lista = [1, 2, 3, 4]
    lista2 = [1, 2, 3, 2, 4, 5, 6, 1]
    print("La lista", lista, "sin su duplicados es", eliminarDuplicado(lista))
    print("La lista", lista2, "¿tiene duplicados?", eliminarDuplicado(lista2))
    print()

main()



