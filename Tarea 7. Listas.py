# encoding: UTF-8
# Autor: Ángel Guillermo Ortiz González A01745998
# Práctica sobre listas

def sumarNumeros(lista):
    suma = []
    s = 0
    for numero in lista:
        s += numero
        suma.append(s)

    return suma

def eliminarPrimeroYUltimo(lista):
    nueva = []
    penultimo = len(lista) - 1
    for elemento in lista[1:penultimo]:
        nueva.append(elemento)

    return nueva

def identificarOrdenados(lista):
    ordenada = sorted(lista)
    if ordenada == lista:
        return True
    else:
        return False

def identificarAnagramas(cadena1,cadena2):
    cadena1 = cadena1.upper()
    cadena2 = cadena2.upper()
    lista1 = list(cadena1)
    lista2 = list(cadena2)
    ordenada1 = sorted(lista1)
    ordenada2 = sorted(lista2)
    if ordenada1 == ordenada2:
        return True
    else:
        return False

def identificarDuplicado(lista):
    repetido = []
    unico = []
    for dato in lista:
        if dato not in unico:
            unico.append(dato)
        elif dato not in repetido:
            repetido.append(dato)

    if len(repetido)>0:
        return True
    else:
        return False

def eliminarDuplicado(lista):
    lista = sorted(lista)
    for dato in lista:
        if lista.count(dato) > 1:
            lista.remove(dato)
    return lista



def main():
    print("Ejercicio 1:")
    lista1 = [1,2,3,4,5]
    suma1 = sumarNumeros(lista1)
    lista2 = [23]
    suma2 = sumarNumeros(lista2)
    lista3 = []
    suma3 = sumarNumeros(lista3)
    print("La lista",lista1,"regresa la lista acumulada",suma1)
    print("La lista",lista2,"regresa la lista acumulada",suma2)
    print("La lista",lista3,"regresa la lista acumulada",suma3)

    print()

    print("Ejercicio 2:")
    lista4 = [1,2,3,4,5]
    elimina4 = eliminarPrimeroYUltimo(lista4)
    lista5 = [1, 2, 3]
    elimina5 = eliminarPrimeroYUltimo(lista5)
    lista6 = []
    elimina6 = eliminarPrimeroYUltimo(lista6)
    print("Lista original",lista4,"regresa",elimina4)
    print("Lista original",lista5,"regresa",elimina5)
    print("Lista original",lista6,"regresa",elimina6)

    print()

    print("Ejercicio 3:")
    lista7 = [1,2,3]
    ordenada7 = identificarOrdenados(lista7)
    lista8 = ["A","X","B"]
    ordenada8 = identificarOrdenados(lista8)
    lista9 = []
    ordenada9 = identificarOrdenados(lista9)
    print("¿La lista",lista7,"está ordenada?",ordenada7)
    print("¿La lista",lista8,"está ordenada?",ordenada8)
    print("¿La lista",lista9,"está ordenada?",ordenada9)

    print()

    print("Ejercicio 4:")
    cadena1 = "Amor"
    cadena2 = "Roma"
    comparacion1 = identificarAnagramas(cadena1,cadena2)
    cadena3 = "Abelardo"
    cadena4 = "adorable"
    comparacion2 = identificarAnagramas(cadena3,cadena4)
    cadena5 = "Japón"
    cadena6 = "China"
    comparacion3 = identificarAnagramas(cadena5,cadena6)
    print("¿",cadena1,"y",cadena2,"son anagramas?",comparacion1)
    print("¿",cadena3,"y",cadena4,"son anagramas?",comparacion2)
    print("¿",cadena5,"y",cadena6,"son anagramas?",comparacion3)

    print()

    print("Ejercicio 5:")
    lista10 = [1,8,3,4,2,7]
    duplicado10 = identificarDuplicado(lista10)
    lista11 = [1,2,3,1,4,5]
    duplicado11 = identificarDuplicado(lista11)
    lista12 = [5]
    duplicado12 = identificarDuplicado(lista12)
    print("¿La lista",lista10,"tiene algún duplicado?",duplicado10)
    print("¿La lista",lista11,"tiene algún duplicado?",duplicado11)
    print("¿La lista",lista12,"tiene algún duplicado?",duplicado12)

    print()

    print("Ejercicio 6:")
    lista13 = [1,8,3,4,3,1,8,2,7]
    sinDuplicado13 = eliminarDuplicado(lista13)
    lista14 = [1,2,3,1,4,5]
    sinDuplicado14 = eliminarDuplicado(lista14)
    lista15 = []
    sinDuplicado15 = eliminarDuplicado(lista15)
    print("La lista",lista13,"sin duplicados es",sinDuplicado13)
    print("La lista",lista14,"sin duplicados es",sinDuplicado14)
    print("La lista",lista15,"sin duplicados es",sinDuplicado15)

main()