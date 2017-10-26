# encoding: UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Tarea sobre listas.

def sumarElementos(lista):
    listaAcumulada = []
    numero = len(lista)
    suma = 0
    for i in range(numero):
        suma = suma + lista[i]
        listaAcumulada.append(suma)
    return listaAcumulada


def quitarPrimeroUltimo(lista):
    listaSin = lista
    listaSin.remove(lista[0])
    listaSin.remove(lista[-1])
    return listaSin


def verificarOrdenNumeros(lista):
    i = 0
    continuar = True
    while continuar == True:
        numero1 = lista[i]
        numero2 = lista[i+1]
        if (numero1 + 1) == numero2:
            continuar == True
            while i != len(lista):
                i = i+1
        else:
            continuar == False
            veredicto = "False"
            return veredicto
    veredicto = "True"
    return veredicto

def verificarOrdenLetras(lista):
        abecedario = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
        print(set(lista).issubset(abecedario))


def main():
    lista =[]
    numero = 0
    numero = int(input("Teclea el número que deseas añadir a la lista [-1 para salir]: "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Teclea el número que deseas añadir a la lista [-1 para salir]: "))

    print("Ejercicio 1.")
    listaAcumulada = sumarElementos(lista)
    print("la lista", lista, "regresa la lista acumulada", listaAcumulada)

    print("Ejercicio 2.")
    listaSin = quitarPrimeroUltimo(lista)
    print("Lista nueva:", listaSin)

    print("Ejercicio 3.")
    eleccion = int(input("Teclea 1 si deseas trabajar con números y 2 si deseas trabajar con letras: "))
    if eleccion == 1:
        elemento = 0
        while elemento != -1:
            elemento = int(input("Teclea el elemento que deseas añadir a la lista [-1 para salir]: "))
            lista.append(elemento)
        veredicto = verificarOrdenNumeros(lista)
        print("¿La lista está en orden?", veredicto)

    elif eleccion == 2:
        elemento = 0
        while elemento != "z":
            elemento = input("Teclea la letra minúscula que deseas añadir a la lista [z para salir]: ")
            lista.append(elemento)
        veredicto = verificarOrdenLetras(lista)
        print("¿La lista está en orden?", veredicto)


main()
