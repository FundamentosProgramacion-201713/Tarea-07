# Autor: Saúl Rodrigo Toral Luna
# Matrícula: A01745007

# El porgrama resuelve diferentes ejercicios usando listas mostrando las opciones por medio  de un menu.

#Definimos listas de prueba (constantes)
# Ejercicio 1
LISTA_1 = [1,2,3,4,5]
LISTA_2 = []
LISTA_3 =[5]
#Ejercicio 2
LISTA_4 = [1,2,3,4,5]
LISTA_5 = [1,2,3]
LISTA_6 = [1,2]
LISTA_7 = []
# Ejercicio 3
LISTA_8 = [1,2,3]
LISTA_9 = ["A", "X", "B"]
# Ejercicio 4
PALABRA_10 = "Roma"
PALABRA_11 = "Mora"
PALABRA_12 = "Hola"
PALABRA_13 = "Hello"
PALABRA_14 = "Toga"
PALABRA_15 = "Gato"
# Ejercicio 5
LISTA_14 = [1,2,3,1,4,5]
LISTA_15 = [5,4,3,2,1]
# Ejercicio 6
LISTA_16 = [1,8,3,4,3,1,8,2,7]
LISTA_17 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9]


# 1.-  La función calcula la suma de los números acumulados de la lista
def calcularSumaAcumulados(lista):
    #Se crea una nueva lista para que en esta se le vayan agregando los elementos de la suma
    nueva_lista = []
    #Acumulador
    suma = 0
    # Se hace un ciclo "FOR" para recorrer cada elemento de la lista
    for n in range(0, len(lista)):
        #Se le ira sumando "n" elemento a la variable para modificarla por cada "n" elemento
        suma += lista[n]
        #A la nueva lista se le va agregando cada valor que se guarda en "suma" y asi sucesivamente
        nueva_lista.append(suma)
    return nueva_lista

# 2.- La función regresa una nueva lista sin el valor inicial y el valor final
def calcularSinExtremos(lista):
    # Se crea una nueva lista en base a la anterior, y para eso se crea una sublista con [:] la cual la guarda en una variable
    nueva_Lista_Sin_Extremos = lista[:]
    # toma de desición: sin en la cantidad de valores de la nueva lista es igual a 0, entonces se regresa la lista sin elementos
    if len(nueva_Lista_Sin_Extremos)  == 0:
        nueva_Lista_Sin_Extremos = lista[:]
    else:
        # Si la lista tiene más de 0 elementos entonces se elimina el primer valor (0) y el ultimo valor, el cual está ordenado en (-1)
        nueva_Lista_Sin_Extremos.remove(nueva_Lista_Sin_Extremos[0])
        nueva_Lista_Sin_Extremos.remove(nueva_Lista_Sin_Extremos[-1])
    return nueva_Lista_Sin_Extremos

# 3.- La función analiza si están ordenados los valores en la lista.
def calcularValoresOrdenados(lista):
    # Se crea una nueva lista en base a la anterior, y para eso se crea una sublista con [:] la cual la guarda en una variable
    nuevaLista = lista[:]
    # Se modifica la nueva lista ordenando sus datos
    nuevaLista.sort()
    # Toma de decisión: si en la nueva lista que está ordenada está igual que la lista original entonces si están ordenados
    if nuevaLista == lista:
        mensaje = True
    else:
        mensaje = False
    return mensaje


# 4.-  La función analiza dos palabras y verifica si son anagramas o no.
def resolverAnagramas(cadena1, cadena2):
    #En una nueva variable se guarda la lista que se crea de una palabra la cual es convertida a mayusculas para comparar valores iguales.
    lista_1_Mayuscula = list(cadena1.upper())
    lista_2_Mayuscula = list(cadena2.upper())
    # Se ordenan los datos de las anteriores variables
    lista_1_Mayuscula.sort()
    lista_2_Mayuscula.sort()
    # Toma de decisión: Si la primera lista está igual de ordenada que la segunda lista entonces son anagramas
    if lista_1_Mayuscula == lista_2_Mayuscula:
        mensaje = True
    else:
        mensaje = False
    return mensaje


# 5.- La función indica si existen valores repetidos en una lista.
def indicarSiHayDuplicados(lista):
    # Inicia el mensaje como falso para despues evaluar y analizar si cambia de valor
    mensaje = False
    # Se hace un for para evaluar en cada elemento de la lista
    for elemento in range(0,len(lista)):
        #  En la lista se hace count para analizar el numero de veces que esta el objeto en la lista
        # Y si en la lista hay más de un elemento significa que se repiten valores
        if lista.count(elemento) > 1:
            mensaje= True
    return mensaje

#6.- La función elimina de la lista original los elementos que tenga repetidos.
def eliminarRepetidos(lista):
    # Se hace un ciclo "FOR" para recorrer cada elemento de la lista
    for elemento in range(0,len(lista)):
    # Se hace un ciclo while, si en la lista existe más de un elemento que se repite, este se elimina con remove.
        while lista.count(elemento) > 1:
            lista.remove(elemento)
    return lista



def main():

    # Mientras el ejercicio siga teniendo el valor de verdadero este seguira repitiendo procesos hasta que se vuelva falso
    ejercicio = True
    # Ciclo "while" permite repetir los procesos "n" cantidad de veces hasta que deje de cumplir la condición
    while ejercicio == True:
        # Se muestran los ejercicios a resolver
        print("Tarea 7. Seleccione que quiere hacer.")
        print("")
        print("1. Suma acumulada de los datos")
        print("2. Lista sin primer y ultimo valor")
        print("3. Valores ordenados")
        print("4. Resolver anagramas")
        print("5. Valores duplicados")
        print("6. Eliminar valores repetidos")
        print("0. Salir")

        # Ingresa lo que el usuario desea hacer
        hacer = int(input("¿Qué desea hacer?: "))
        print("")

        # Por medio de decisiones se evalua y muestra el ejercicio deseado
        if hacer == 1:
            print("EJERCICIO 1.")
            print("")
            print("La lista",LISTA_1, "regresa la lista acumulada",calcularSumaAcumulados(LISTA_1))
            print("La lista",LISTA_2, "regresa la lista acumulada",calcularSumaAcumulados(LISTA_2))
            print("La lista",LISTA_3, "regresa la lista acumulada",calcularSumaAcumulados(LISTA_3))
            print("---------------------------------------------------------")
            print("")

        elif hacer == 2:
            print("EJERCICIO 2.")
            print("")
            print("La lista original", LISTA_4, "regresa", calcularSinExtremos(LISTA_4))
            print("La lista original", LISTA_5, "regresa", calcularSinExtremos(LISTA_5))
            print("La lista original", LISTA_6, "regresa", calcularSinExtremos(LISTA_6))
            print("La lista original", LISTA_7, "regresa", calcularSinExtremos(LISTA_7))
            print("---------------------------------------------------------")
            print("")

        elif hacer == 3:
            print("EJERCICIO 3.")
            print("")
            print("Los valores de la lista", LISTA_8, "estan ordenados: ", calcularValoresOrdenados(LISTA_8))
            print("Los valores de la lista", LISTA_9, "estan ordenados: ", calcularValoresOrdenados(LISTA_9))
            print("Los valores de la lista", LISTA_16, "estan ordenados: ", calcularValoresOrdenados(LISTA_16))
            print("---------------------------------------------------------")
            print("")

        elif hacer == 4:
            print("EJERCICIO 4.")
            print("")
            print("La palabra", PALABRA_10, "y la palabra", PALABRA_11, "son anagramas: ", resolverAnagramas(PALABRA_10, PALABRA_11))
            print("La palabra", PALABRA_12, "y la palabra", PALABRA_13, "son anagrama: ",resolverAnagramas(PALABRA_12, PALABRA_13))
            print("La palabra", PALABRA_14, "y la palabra", PALABRA_15, "son anagrama: ",resolverAnagramas(PALABRA_14, PALABRA_15))
            print("---------------------------------------------------------")
            print("")

        elif hacer == 5:
            print("EJERCICIO 5.")
            print("")
            print("En la lista", LISTA_14, "existen valores repetidos: ", indicarSiHayDuplicados(LISTA_14))
            print("En la lista", LISTA_15, "existen valores repetidos: ", indicarSiHayDuplicados(LISTA_15))
            print("En la lista", LISTA_17, "existen valores repetidos: ", indicarSiHayDuplicados(LISTA_17))
            print("---------------------------------------------------------")
            print("")
        elif hacer == 6:
            print("EJERCICIO 6.")
            print("")
            print("La lista sin valores repetidos es: " , eliminarRepetidos(LISTA_16))
            print("La lista sin valores repetidos es: " , eliminarRepetidos(LISTA_17))
            print("---------------------------------------------------------")
            print("")
        elif hacer > 6 or hacer < 0:
            print("ERROR: ")
            print("La opción %d es invalida, escoge un número del menú" % hacer)
            print("")
        else:
            ejercicio = False
            print("Gracias por participar")


main()







