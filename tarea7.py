#encoding:UTF-8
#José Antonio Gómez Mora
#Tarea 7. Ejercicios listas

def calcularAcumulacion(acumulacion):
    lista=[]
    lista.append(acumulacion[0])
    i=0
    desfase=0
    while i<len(acumulacion)-1:
        valor=acumulacion[i]+acumulacion[i+1]+desfase
        lista.append(valor)
        i+=1
        desfase+=i
    return lista


def calcularEjercicio2(lista):
    nuevaLista=lista[:]
    nuevaLista.remove(lista[0])
    nuevaLista.remove(lista[-1])
    return nuevaLista

def calcularEjercicio3(lista):
    listaNueva=lista[:]
    listaNueva.sort()
    if lista==listaNueva:
        return True
    return False
def esAnagrama(palabra1,palabra2):
    lista1=list(palabra1.lower())
    lista2=list(palabra2.lower())

    lista1.sort()
    lista2.sort()

    if lista1==lista2:
        return True
    return False

def calcularValorDuplicado(lista):
    nuevaLista=lista[:]
    for i in nuevaLista:
        if  nuevaLista.count(i)>1:
            return True

        else: return False

def calcularRepetidos(lista):
    for n in lista:
        valorLista=lista.count(n)
        if valorLista>1:
            return True

        else:
            return False
def main():

    print("Ejercicio 1.")
    ejercicio1=[1,2,3]
    print("Prueba la lista",ejercicio1,"obtiene",calcularAcumulacion(ejercicio1))

    print("Ejercicio 2.")
    ejercicio2=[1,2,3,4]
    print("Prueba la lista",ejercicio2,"obtiene",calcularEjercicio2(ejercicio2))

    print("Ejercicio 3.")
    ejercicio3=[1,2,3,4]
    print("Prueba la lista", ejercicio3 ,"obtiene",calcularEjercicio3(ejercicio3))

    print("Ejercicio 4.")
    palabra1="roma"
    palabra2="mora"
    print("Prueba las palabras",palabra1,"y", palabra2,"obtiene",esAnagrama(palabra1,palabra2))

    print("Ejercicio 5.")
    lista=[1,2,3,1]
    print("Prueba la lista",lista,"obtiene",calcularValorDuplicado(lista))

    print("Ejercicio 6.")
    lista6=[1,2,3,4,1,2]
    print("Prueba la lista",lista6,"obtiene",calcularRepetidos(lista6))


main()