# encoding UTF-8
# Jaime Orlando López Ramos




def eliminarElementos(lista):
    listaElim=lista
    if len(lista) == 2:
        listaElim=[]
    else:
        num = len(lista)
        primero = lista[0]
        final = lista[num-1]
        listaElim.remove(final)
        listaElim.remove(primero)
    return listaElim

    pass




def main():
    lista =[]
    x = int(input("Ingrese un valor para la lista (-1 si no desea agregar nada): "))
    while x != -1:
        if x >= 0:
            lista.append(x)
            x = int(input("ingrese un valor para la lista (-1 para salir): "))
        else:
            print("La lista no trabaja con números negativos, vuelva a intentar con otro número")
            x= int(input("Ingrese un valor a la lista (-1 para salir: "))
    print("Lista Original:", lista)
    print("Lista con elementos eliminados:", (eliminarElementos(lista)))

main()



