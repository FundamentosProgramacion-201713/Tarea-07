# encoding UTF-8
# Jaime Orlando López Ramos, A01374696
#Suma de elementos en lista


def sumarElementos(lista):
    listaSum=[]
    num = len(lista)
    counter = 0
    for i in range (num):
        counter = counter + lista[i]
        listaSum.append(counter)
    return listaSum

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
    print("lista original:", lista)
    print("Lista con suma",(sumarElementos(lista)))

main()



