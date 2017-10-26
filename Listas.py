# encoding UTF-8
# AUTOR: Luis Enrique Neri Pérez
# DESCRIPCIÓN: Programa que muestra varios ejemplos donde se refleje que cada función funciona adecuadamente

#PRIMER EJERCICIO ---------------------------------------------------------------------------------------------------

def ejercicio1(original):
    nueva = []
    acumulador = 0
    comprobador = sum(original)
    while not acumulador == comprobador:
        for dato in original:
            acumulador = acumulador + dato
            nueva.append(acumulador)
    print("  -La lista",original,"devuelve",nueva)


def funcion1():
    print("EJERCICIO #1: Regresa la suma acumulada de los datos")
    print("--------------------------------------------------------------")
    prueba1 = [1, 2, 3]
    ejercicio1(prueba1)
    prueba2 = [1, 2, 3, 4]
    ejercicio1(prueba2)
    prueba3 = []
    ejercicio1(prueba3)
    prueba4 = [5]
    ejercicio1(prueba4)
    print("\n")

#SEGUNDO EJERCICIO ---------------------------------------------------------------------------------------------------
def ejercicio2(original):
    nueva = []
    nueva = nueva + original
    nueva.remove(nueva[0])
    nueva.remove(nueva[-1])
    print("  -La lista", original, "devuelve", nueva)


def funcion2():
    print("EJERCICIO #2: Regresa la lista sin el primer ni el último elemento ")
    print("--------------------------------------------------------------")
    prueba1 = [1, 2, 3]
    ejercicio2(prueba1)
    prueba2 = [1, 2, 3, 4]
    ejercicio2(prueba2)
    prueba3 = ["Primer", "Hola", "Mundo", "Último"]
    ejercicio2(prueba3)
    prueba4 = [0,4,4,4,0]
    ejercicio2(prueba4)
    print("\n")

#TERCER EJERCICIO ---------------------------------------------------------------------------------------------------

def ejercicio3(original):
    nueva = sorted(original)
    if original == nueva:
        print("  -¿La lista", original, "está ordenada?:", True)
    else:
        print("  -¿La lista", original, "está ordenada?:", False)

def funcion3():
    print("EJERCICIO #3: Regresa True si la lista está ordenenada o False si no lo está ")
    print("--------------------------------------------------------------------------------")
    prueba1 = [1, 2, 3, 4]
    ejercicio3(prueba1)
    prueba2 = ["A", "B", "C", "D"]
    ejercicio3(prueba2)
    prueba3 = [2, 3, 1 ,5]
    ejercicio3(prueba3)
    prueba4 = ["X", "B", "Y", "D"]
    ejercicio3(prueba4)
    print("\n")

#CUARTO EJERCICIO ---------------------------------------------------------------------------------------------------

def ejercicio4(prueba1, prueba2):
    original = list(prueba1.upper())
    nueva= list(prueba2.upper())
    nueva.reverse()
    if original == nueva:
        print("  -¿La cadena", prueba1, "y", prueba2, "son anagramas?:", True)
    else:
        print("  -¿La cadena" , prueba1, "y", prueba2 , "son anagramas?:", False)

def funcion4():
    print("EJERCICIO #4: Regresa True si las dos palabras son anagramas o False si no lo son ")
    print("--------------------------------------------------------------------------------")
    prueba1 = "Roma"
    prueba2 = "Amor"
    ejercicio4(prueba1,prueba2)
    prueba1 = "Hola"
    prueba2 = "Hello"
    ejercicio4(prueba1, prueba2)
    prueba1 = "Reto"
    prueba2 = "Oter"
    ejercicio4(prueba1, prueba2)
    prueba1 = "Pedro"
    prueba2 = "Peter"
    ejercicio4(prueba1, prueba2)
    print("\n")

#QUINTO EJERCICIO ---------------------------------------------------------------------------------------------------

def ejercicio5(original):
    for k in range(len(original)-1):
        if original.count(original[k]) >1:
            print("  -¿La lista" , original , "repite elementos?:", True)
            return True
    print("  -¿La lista", original, "repite elementos?:", False)
    return False

def funcion5():
    print("EJERCICIO #5: Regresa True si alguno de los datos están repetidos o False si no lo están ")
    print("------------------------------------------------------------------------------------------")
    prueba1 = [1,2,3,4]
    ejercicio5(prueba1)
    prueba2 = [1,2,3,2]
    ejercicio5(prueba2)
    prueba3 = ["a", "b", "c", "d"]
    ejercicio5(prueba3)
    prueba4 = []
    ejercicio5(prueba4)
    print("\n")

#SEXTO EJERCICIO ---------------------------------------------------------------------------------------------------

def ejercicio6(original):
    duplicado = []
    duplicado = duplicado + original
    for indice in range(len(original)-1):
        datoRep = original[indice]
        if original.count(datoRep) >1:
            while not original.count(datoRep) == 0:
                original.remove(datoRep)
            original.insert(indice,datoRep)
    print("Para la lista", duplicado, "se regresa", original)

def funcion6():
    print("EJERCICIO #6: Si un elemento en la lista se repite, este de quitara dejando solo uno")
    print("------------------------------------------------------------------------------------------")
    prueba1 = [10, 30, 20, 30]
    ejercicio6(prueba1)
    prueba2 = [1,8,3,4,3]
    ejercicio6(prueba2)
    prueba2 = [1,2,3,4]
    ejercicio6(prueba2)
    prueba2 = [1,1]
    ejercicio6(prueba2)


#Función Main que despliega todos los ejemplos del código
def main():
    print("TAREA 07: EJEMPLOS DE USO DE LISTAS")
    print("\n")
    funcion1()
    funcion2()
    funcion3()
    funcion4()
    funcion5()
    funcion6()


main()