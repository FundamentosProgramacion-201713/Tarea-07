#encoding UTF-8
# Jaime Orlando López Ramos





def verificarOrden(lista):
    counter = 0
    leng = len(lista)
    for i in range (leng-1):
        if lista[i] > lista[i +1]:
            counter += 1
        else:
            counter += 0
    if counter != 0:
        return False
    else:
        return True
    pass


def main():
    lista = []
    elemento = input("Teclee el valor a ingresar deseado, (Teclee salir si no desea ingresar nada): ")
    while elemento != "salir":
        lista.append(elemento)
        elemento = input("Teclee el valor a ingresar deseado (salir para ya no agregar nada): ")
    x = verificarOrden(lista)
    print(x)



main()

