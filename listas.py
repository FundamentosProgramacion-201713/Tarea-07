#Encoding UTF-8
#Anaid Fernanda Labat González,A01746289

LISTA = [1, 2, 3, 4 ,5,6]
LISTA1 = []
LISTA2 = [6]
LISTA3 = [1, 2, 3,4]
LISTA4 = [1, 2,3]
LISTA5 = ["A", "X", "B"]
LISTA6 = "Roma"
LISTA7 = "Mora"
LISTA8 = "Hola"
LISTA9 = "Hello"
LISTA10 = [1, 2, 3, 1, 4, 6,5]
LISTA11 = [6,5, 4, 3, 2, 1]
LISTA12 = [1, 8, 3, 4, 3, 1, 9, 2, 7,8,5]
LISTA13 = [1,1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]
LISTA14 = [3, 1, 5, 2, 2, 6,8]
LISTA15 = [4, 5, 4, 2, 3, 1, 2]
LISTA16 = "Caza"
LISTA17 = "Casa"

#Descripción: Suma los datos de una lista y regresa una nueva
def sumarDatos(lista):
    list = []
    resultado = 0
    for d in range(0,len(lista)):
        resultado += lista[d]
        list.append(resultado)
    return list

#Descripción-2: Elimina los datos ubicados en los extremos de una lista
def eliminarExtremos(lista):
    sinDatosExtremos = lista[:]
    if len(sinDatosExtremos) != 0:
        sinDatosExtremos.remove(sinDatosExtremos[0])
        sinDatosExtremos.remove(sinDatosExtremos[-1])
    else:
        sinDatosExtremos = lista[:]
    return sinDatosExtremos

#Descripción3: Regresa true si los valores de una lista estan ordenados
def ordernarValores(lista):
    nuevalista= lista[:]
    nuevalista.sort()
    if nuevalista == lista:
        mensaje= True
    else:
        mensaje= False
    return  mensaje
#DEscripción4: recibe dos cadenas, regresa true si son anagramas y de lo contrario, false
def anagrama(lista1, lista2):
    listaM1 = list(lista1)
    listaM2 = list(lista2)
    listaM1.sort()
    listaM2.sort()
    if listaM1 == listaM2:
        mensaje=True
    else:
        mensaje=False
    return mensaje
#DEscripción5: Regresa true si los datos de una lista están duplicados
def calcularSinDuplicados(lista):
    sinduplicados = lista[:]
    for n in sinduplicados:
        if sinduplicados.count(n) > 1:
            mensaje = True
        else:
            mensaje = False
        return mensaje
#Descripción6: Regresa los valores repetidos de una lista
def eliminarRepetidos(lista):
    for n in lista:
            while lista.count(n)>1:
                lista.remove(n)
    return lista

def main():
    print("Ejercicio 1: ")
    print("La lista ", LISTA, "regresa la lista acumulada ", sumarDatos(LISTA))
    print("La lista ", LISTA1, "regresa la lista acumulada ", sumarDatos(LISTA1))
    print("La lista ", LISTA11, "regresa la lista acumulada ", sumarDatos(LISTA11))
    print("La lista ", LISTA2, "regresa la lista acumulada ", sumarDatos(LISTA2))
    print("")

    print("Ejercicio 2: ")
    print("La lista original ", LISTA1, "regresa ", eliminarExtremos(LISTA1))
    print("La lista original ", LISTA, "regresa ", eliminarExtremos(LISTA))
    print("La lista original ", LISTA14, "regresa ", eliminarExtremos(LISTA14))
    print("La lista original ", LISTA4, "regresa ", eliminarExtremos(LISTA4))
    print("")

    print("Ejercicio 3: ")
    print("Los valores de la lista ", LISTA5, "estan ordenados? ", ordernarValores(LISTA5))
    print("Los valores de la lista ", LISTA14, "estan ordenados? ", ordernarValores(LISTA14))
    print("Los valores de la lista ", LISTA13, "estan ordenados? ", ordernarValores(LISTA13))
    print("Los valores de la lista ", LISTA, "estan ordenados? ", ordernarValores(LISTA))
    print("")

    print("Ejercicio 4: ")
    print("La palabra ", LISTA6, "y la palabra ", LISTA7, "forman un anagrama? ",anagrama(LISTA6, LISTA7))
    print("La palabra ", LISTA8, "y la palabra ", LISTA9, "forman un anagrama? ",anagrama(LISTA8, LISTA9))
    print("La palabra ", LISTA16, "y la palabra ", LISTA17, "forman un anagrama? ",anagrama(LISTA16, LISTA17))
    print("")

    print("Ejercicio 5: ")
    print("De la lista ", LISTA, "hay duplicados? ", calcularSinDuplicados(LISTA))
    print("De la lista ", LISTA10, "hay duplicados? ", calcularSinDuplicados(LISTA10))
    print("De la lista ", LISTA11, "hay duplicados? ", calcularSinDuplicados(LISTA11))
    print("De la lista ", LISTA15, "hay duplicados? ", calcularSinDuplicados(LISTA15))
    print("")

    print("Ejercicio 6: ")
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA13))
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA15))
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA))
    print("La lista final sin valores repetidos es: ", eliminarRepetidos(LISTA11))
main()