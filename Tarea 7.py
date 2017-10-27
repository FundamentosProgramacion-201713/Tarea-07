# Autor: Mónica Monserrat Palacios Rodríguez
# A01375137
# UTF-8

def regresarSumaAcumulada(lista): #Función que regresa un acumulador y la mete a una lista con un for
    nuevaLista = []
    acumulador = 0
    for i in (lista):
        acumulador += i
        nuevaLista.append(acumulador)

    return nuevaLista


def regresarSinPrimeroNiUltimo(lista): #Función que regresa los valores de una lista sin el primero ni el último valor con un ciclo for
    nuevaLista = []
    for i in range(1,(len(lista)-1)):
        nuevaLista.append(lista[i])

    return nuevaLista

def verificarOrden(lista): #Función que verifica que la lista se encuentre en orden, se crea una lista
    nuevaLista = lista[:]
    nuevaLista.sort()

    if lista == nuevaLista:
        respuesta = True
    else:
        respuesta = False

    return respuesta

def verificarAnagrama(cadena1, cadena2): #Función que verifica si una cadena es anagrama
    lista1 = list(cadena1.lower())
    lista2 = list(cadena2.lower())
    #lista1 = []
    #lista2 = []
    lista1.sort()
    lista2.sort()

    if lista1 == lista2:
        respuesta = True

    else:
        respuesta = False

    return respuesta

def verificarDuplicado(lista): # Función Verifica quela lista tenga duplicados
    nuevaLista = lista[:]
    for i in nuevaLista:
        if nuevaLista.count(i) > 1:
            respuesta = True
        elif nuevaLista.count(i) <= 1:
            respuesta = False

    return respuesta


def eliminarRepetidos(lista): #Función que elimina los elementos repetidos de la misma lista
    nuevaLista = lista[:]
    for k in range(0, len(nuevaLista)):
            while nuevaLista.count(k)>1:
                nuevaLista.remove(k)
    return nuevaLista

def main(): #Main que llama a todas las funciones e imprime los resultados, probando distintos valores
    pruebaA1 = [1,2,3,4,5]
    pruebaA2 = [1,2,3]
    pruebaA3 = [1,4,6,12]

    pruebaB1 = [1,2,3,4,5]
    pruebaB2 = [1,2]
    pruebaB3 = []

    pruebaC1 = [1,2,3]
    pruebaC2 = ["A", "X", "B"]
    pruebaC3 = [3,5,7]

    pruebaD1 = ("Roma"), ("Mora")
    pruebaD2 = ("Hola"), ("Hello")
    pruebaD3 = ("Monse"), ("Esnom")

    cadenaD1 = "Roma"
    cadena_D1 = "Mora"
    cadenaD2 = "Hola"
    cadena_D2 = "Hello"
    cadenaD3 = "Monse"
    cadena_D3 = "Esnom"

    pruebaE1 = [1,2,3,1,4,5,4,4,1]
    pruebaE2 = [1,1,4,5,6,1]
    pruebaE3 = [1,2,5,7,3]

    pruebaF1 = [1,4,4,4,5,6,7,8,8,8]
    pruebaF2 = [1,2,4,5,5,6,7,5]
    pruebaF3 = [1,5,5,7,7,2,2,2,2,4,4,5,3,3,4]

#Ejercicio 1
    print ("Ejercicio 1: ")
    print ("La lista", pruebaA1, "regresa la lista acumulada", regresarSumaAcumulada(pruebaA1))
    print ("La lista", pruebaA2, "regresa la lista acumulada", regresarSumaAcumulada(pruebaA2))
    print ("La lista", pruebaA3, "regresa la lista acumulada", regresarSumaAcumulada(pruebaA3))
    print(" ")
#Ejercicio 2
    print("Ejercicio 2: ")
    print("Lista original", pruebaB1, "regresa", regresarSinPrimeroNiUltimo(pruebaB1))
    print("Lista original", pruebaB2, "regresa", regresarSinPrimeroNiUltimo(pruebaB2))
    print("Lista original", pruebaB3, "regresa", regresarSinPrimeroNiUltimo(pruebaB3))
    print(" ")
#Ejercicio 3
    print("Ejercicio 3: ")
    print("Lista original", pruebaC1, "regresa valor", verificarOrden(pruebaC1))
    print("Lista original", pruebaC2, "regresa valor", verificarOrden(pruebaC2))
    print("Lista original", pruebaC3, "regresa valor", verificarOrden(pruebaC3))
    print(" ")
#Ejercicio 4
    print("Ejercicio 4: ")
    print("Las cadenas", pruebaD1, "¿Son un anagrama?", verificarAnagrama(cadenaD1, cadena_D1))
    print("Las cadenas", pruebaD2, "¿Son un anagrama?", verificarAnagrama(cadenaD2, cadena_D2))
    print("Las cadenas", pruebaD3, "¿Son un anagrama?", verificarAnagrama(cadenaD3, cadena_D3))
    print(" ")
#Ejercicio 5
    print("Ejercicio 5: ")
    print("La lista", pruebaE1, "¿Tiene datos duplicados?", verificarDuplicado(pruebaE1))
    print("La lista", pruebaE2, "¿Tiene datos duplicados?", verificarDuplicado(pruebaE2))
    print("La lista", pruebaE3, "¿Tiene datos duplicados?", verificarDuplicado(pruebaE3))
    print(" ")
#Ejercicio 6
    print("Ejercicio 6: ")
    print("Lista original", pruebaF1, "Lista sin valores repetidos", eliminarRepetidos(pruebaF1))
    print("Lista original", pruebaF2, "Lista sin valores repetidos", eliminarRepetidos(pruebaF2))
    print("Lista original", pruebaF3, "Lista sin valores repetidos", eliminarRepetidos(pruebaF3))
    print(" ")



main()