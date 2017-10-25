# encondig:UTF-8
#Autor Angel Ramírez Martínez  A01273759
#Descripción: Programa que realiza diferentes operaciones con listas
#Determinación de variables globales con listas y cadenas
lista1 = [1,2,3,4,5]
lista2 = []
lista3 = [5]
lista4=[1,2,3,2,4,5]
lista5=[1,1,1,2,3,4,5,6,6,6,7]
lista6=[1,2,3]
lista7=[1,3,2,4,8,6,7]
plbra1 = 'Roma'
plbra2 = 'Mora'
plbra3 = 'Hola'
plbra4 = 'Hello'
plbra5 = 'Opio'
plbra6 = 'Pipo'
#Función que regresa una nueva lista la cual esa conformada por la suma de los primeros i+1 valores de la lista original que recibe como parámetro
def sumarLista(lista):
    nuevalista = []
    listasum = []
    for index in range(len(lista)):
        listasum.append(lista[index])
        nuevalista.append(sum(listasum))
    return nuevalista
#Función que regresa una nueva lista que ya no contiene el primer y el ultimo elemento de la lista original que recibe como parámetro
def eliminardatos(lista):
    if len(lista)==0:
        return lista
    else:
        nuevalista = lista[:]
        nuevalista.remove(nuevalista[0])
        nuevalista.remove(nuevalista[-1])
        return nuevalista

#Función que que regresa si dos cadenas que reciben como parámetros son anagramas
def esAnagrama(p1,p2):
    p1=p1.upper()
    p2=p2.upper()
    lista1=[]
    lista2=[]
    for letter in p1:
        lista1.append(letter)
    for letter2 in p2:
        lista2.append(letter2)
    if len(lista1)==len(lista2):
        for dato in lista1:
            if dato in lista2:
                return True
    return False

#Función que regresa si una lista que recibe como parámetro tiene elementos duplicados
def esDuplicado(lista):
    lista_nueva = []
    for i in lista:
        if i not in lista_nueva:
            lista_nueva.append(i)
    if len(lista_nueva)!= len(lista):
        return True
    else:
        return False

#Función que regresa si una lista que recibe como parámetro está ordenada
def esOrdenado(lista):
    listao = lista[:]
    listao.sort()
    if lista == listao:
        return True
    else:
        return False

#Función que borra elementos repetidos de una lista que recibe como perámetro
def borrarrepetidos(lista):
    for dato in lista:
        while lista.count(dato) >1:
            lista.remove(dato)
    return lista

#Función main que imprime las pruebas de diferentes listas por las diferentes funciones anteriores
def main():
    print('''• La lista %s, regresa la lista acumulada %s 
• La lista %s, regresa la lista acumulada %s
• La lista %s, regresa la lista acumulada %s
''' %(lista1,sumarLista(lista1),lista2,sumarLista(lista2),lista3,sumarLista(lista3)))
    print('''• Lista original %s, regresa %s 
• Lista original %s, regresa %s
• Lista original %s, regresa %s
''' % (lista1, eliminardatos(lista1), lista2, eliminardatos(lista2), lista6, eliminardatos(lista6)))
    print('''• Para la lista %s, regresa %s
• Para la lista %s, regresa %s
• Para la lista %s, regresa %s    
''' %(lista1, esOrdenado(lista1), lista2, esOrdenado(lista2), lista7, esOrdenado(lista7)))
    print('''• Para la cadena %s y %s, regresa %s
• Para la cadena %s y %s, regresa %s
• Para la cadena %s y %s, regresa %s   
''' % (plbra1,plbra2, esAnagrama(plbra1,plbra2), plbra3,plbra4, esAnagrama(plbra3,plbra4), plbra5,plbra6, esAnagrama(plbra5,plbra6)))
    print('''• Para la lista %s, regresa %s
• Para la lista %s, regresa %s
• Para la lista %s, regresa %s    
''' % (lista1, esDuplicado(lista1), lista4, esDuplicado(lista4), lista5, esDuplicado(lista5)))
    print('''• Para la lista %s, regresa %s
• Para la lista %s, regresa %s
• Para la lista %s, regresa %s    
''' % (lista1, borrarrepetidos(lista1), lista4, borrarrepetidos(lista4), lista5, borrarrepetidos(lista5)))
main()