#Encoding: UTF-8
#Autor: Roberto Téllez Perezyera
"""
En este programa se prueban diversos conceptos sobre lista con funciones que emplean éstos para realizar sus tareas
y devolver nuevas listas.
Se muestra al usuario un conjunto de demostraciones del trabajo de las funciones por cada uno de los 6 ejercicios
"""

#Ejercicio1
def sumarDatos(lista):
    list = []
    resultado = 0
    for k in range(0,len(lista)):
        resultado += lista[k]
        list.append(resultado)

    return list


#Ejercicio2
def quitarExtremos(lista):
    list = lista[:]
    if len(list)==1:
        list.remove(list[0])
    elif len(list) == 0:
        pass
    else:
        list.remove(list[0])
        list.remove(list[-1])

    return list


#Ejercicio3
def estaOrdenada(lista):
    original = lista[:]
    sortedList = sorted(original)

    if original == sortedList:
        return True
    else:
        return False




#Ejercicio4
def esAnagrama(string1, string2):

    lista1 = list(string1)
    lista2 = list(string2)
    lista1 = sorted(lista1)
    lista2 = sorted(lista2)
    if lista1 == lista2:
        return True
    else:
        return False


#Ejercicio5
def hayDuplicado(lista):

    return


#Ejercicio6
def eliminarRepetidos(lista):
    #OJO: se hacen los cambios sobre la misma lista

    return


def main():
    #Se prueban cada una de las funciones con varias listas, demostrando que realizan correctamente su tarea designada
    a = [1,2,3,4,5]
    b = [1,2,3]
    c = []
    d = [5]
    h = ["A","X","B"]
    i = [1,8,3,4,3,1,8,2,7]
    j = [1,2,3,1,4,5]
    k = [5,4,3,2,1]
    str1 = "roma"
    str2 = "amor"
    str3 = "mora"
    str4 = "hola"
    str5 = "hello"

    print("Ejercicio 1:")
    print("La lista ",a,", regresa ",sumarDatos(a))
    print("La lista ",c,", regresa ",sumarDatos(c))
    print("La lista ",d,", regresa ",sumarDatos(d))
    print("---------------------")


    print("Ejercicio 2:")
    print("La lista ",a,", regresa ",quitarExtremos(a))
    print("La lista ",b,", regresa ",quitarExtremos(b))
    print("La lista ",c,", regresa ",quitarExtremos(c))
    print("La lista ",d,", regresa ",quitarExtremos(d))
    print("---------------------")


    print("Ejercicio 3:")

    print("La lista ",b," está en orden:",estaOrdenada(b))
    print("La lista ",j," está en orden:",estaOrdenada(j))
    print("La lista ",h," está en orden:",estaOrdenada(h))


    print("---------------------")

    print("Ejercicio 4:")
    print("Una palabra es anagrama de otra si las dos tienen las mismas letras, con el MISMO NÚMERO de apariciones, "
          "pero en orden diferente.")
    print(esAnagrama(str1,str2),", para 'roma' y 'amor'")
    print(esAnagrama(str4,str5),", para 'hola' y 'hello'")
    print(esAnagrama(str1,str3),", para 'roma' y 'mora'")
    print("---------------------")

    print("Ejercicio 5:")
    print("!!FALTA!!")
    print("---------------------")

    print("Ejercicio 6:")
    print("!!FALTA!!")
    print("---------------------")


main()






"""
def hacerAlgo(lista):

    contador = 0
        if condición:
            contador += 1
        
    return contador
    
    
poner listas en main()

en main:
    print("la lista", original1, "tiene", contarPares(a))
"""

"""
pls repasa how to circulo, linea, rectángulo...
en las listas van a estar los datos que van a usar para dibujar
los datos pueden ser radios, colores, equis y yes
"""
