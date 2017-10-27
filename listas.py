# Encoding: UTF-8
# Autor: Viviana Osorio Nieto
# una lista que regrese una nueva lista son el primer y ultimo valor

def eliminarNumeros(lista):
    lista2 = lista
    lista2.remove(lista[0])
    lista2.remove(lista[len(lista)-1])
    print("la lista sin el primer y ultimo digito es:", lista2)
    main()


def sumarNumeros(lista):
    lista2 = lista
    suma= 0
    for x in range(len(lista2)):
        suma = suma + lista2[x]
        lista2[x] = suma
        print("el resultado es:", lista2)
    main()


def calificarNumerosOrgenados(lista):
    lista2 = lista.sort()
    if lista2 == lista:
        print  ("True")
    else:
        print ("False")
    main ()


def calcularAnagramas():
    r = print(input("teclee la primera palabra: "))
    p = print(input("teclee la segunda palabra: "))
    lista1= []
    lista1.append(r)
    if lista1.__contains__(p):
        print ("es un angrama \(^.^)/ ")
    else:
        print ("no es un anagrama :( ")


    main()


def calcularDuplicados():
    list1 =[1,1,4,6,5]
    list2=[1,3,5,6,7,8]
    unico1= []
    repetido1 = []
    unico2 =[]
    repetido2=[]
    for x in list1:
        if x not in unico1:
            unico1.append(x)
        elif x not in repetido1:
            repetido1.append(x)
        elif len(repetido1)> 0 :
            print ("Caso 1 cuando los valores son: 1,1,4,6,5 es True")
        else:
            print("Casoo 2 cuando los valores son: 1,3,5,6,7,8 es False")
    for x in list2:
        if x not in unico2:
            unico2.append(x)
        elif x not in repetido2:
            repetido2.append(x)
        elif len(repetido2)> 0 :
            print ("Caso 1 cuando los valores son: 1,1,4,6,5 es True")
        else:
            print("Casoo 2 cuando los valores son: 1,3,5,6,7,8 es False")

    main()


def eliminarDuplicados():
    elementos = (1,1,3,4,5)
    lista = []
    while elementos not in lista:
        lista.append(elementos)
    print(lista)
    main()
def main ():
    lista = [1,2,3,4]
    n = int(input(print("1-sumarNumeros\n"  
          "2-eliminarPrimer-Ultimo\n"
          "3-calificarNumerosOrdenados\n"
          "4-calcularAnagramas\n"
          "5-calcularDuplicados\n"
          "6-eliminarDuplicados\n"
          "7- Salir\n"
          "teclea una opcion: ")))
    while n != 7:
        if n == 1:
            sumarNumeros (lista)
        elif n == 2:
            eliminarNumeros (lista)
        elif n == 3:
            calificarNumerosOrgenados (lista)
        elif n == 4:
            calcularAnagramas ()
        elif n == 5:
            calcularDuplicados ()
        elif n == 6:
            eliminarDuplicados ()


main()