#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que hace una serie de operaciones con listas


def sumarNumeros(lista):    #Función que acumula la suma de los números de una lista
    listaSuma= []
    suma=0

    for i in range(lista[len(lista)-1]):
        suma+=lista[i]
        listaSuma.append(suma)


    print(listaSuma)

def removerElementos(lista):    #Función que remueve el primer y el último elemento de una lista

    lista2= lista[:]
    if len(lista2)>0:
        lista2.remove(lista2[0])
        lista2.remove(lista2[len(lista2)-1])
        print(lista2)
    else:
        print(lista2)

def verOrden(lista):    #Función que dice si una lista está en orden o no

    lista2=lista[:]
    lista2.sort()
    if lista==lista2:
        print(True)
    else:
        print(False)

def esAnagrama(cadena1,cadena2):    #Función que determina si hay un anagrama o no
    cadena1= cadena1.upper()
    cadena2= cadena2.upper()
    lista1=list(cadena1)
    lista2=list(cadena2)
    anagrama= True

    for i in lista2:
        if not i in lista1 or lista1.count(i)!=lista2.count(i):
            anagrama=False
    print(anagrama)

def esDuplicado(lista):     #Función que determina si hay duplicados en una lista
    duplicado= False
    for i in (lista):
        if lista.count(i)>1:
            duplicado=True
    print (duplicado)

def quitarDuplicados(lista):    #Función que remueve los duplicados de una lista
    for i in (lista):
        if lista.count(i)>1:
            lista.remove(i)
    print(lista)

def main():
    print("La lista [1,2,3] regresa la lista acumulada: ")
    sumarNumeros([1,2,3])
    print("La lista [1,2,3,4,5,6,7] regresa la lista acumulada: ")
    sumarNumeros([1, 2, 3, 4, 5, 6, 7])
    print("")
    print("Lista original: [1,2,3,4] ")
    print("Regresa: ")
    removerElementos([1,2,3,4])
    print("Lista original: [700,600,50,300,75,4] ")
    print("Regresa: ")
    removerElementos([700,600,50,300,75,4])
    print("")
    print("Esta lista está ordenada: [1,2,3]")
    verOrden([1,2,3])
    print("Esta lista está ordenada: [4,1,5,3,9,2]")
    verOrden([4,1,5,3,9,2])
    print("")
    print("Este es un anagrama: [Roma,Mora]")
    esAnagrama("Roma","Mora")
    print("Este es un anagrama: [Perro,Gato]")
    esAnagrama("Perro", "Gato")
    print("Este es un anagrama: [Repaso,Separo]")
    esAnagrama("Repaso", "Separo")
    print("")
    print("Esta lista tiene duplicados: [1, 2, 3, 4, 5, 7, 11]")
    esDuplicado([1, 2, 3, 4, 5, 7, 11])
    print("Esta lista tiene duplicados: [1, 2, 3, 4, 5, 5, 7, 7]")
    esDuplicado([1, 2, 3, 4, 5, 5, 7, 7])
    print("A la lista anterior se le quitaron los duplicados")
    quitarDuplicados([1, 2, 3, 4, 5, 5, 7, 7])

main()






