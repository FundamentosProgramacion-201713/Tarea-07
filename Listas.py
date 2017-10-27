#Javier Pascal Flores
#Encoding:UTF-8

def hacer_Suma(a):
    if len(a)==1:
        return a
    else:
        r=[]
        n=0
        for i in range (len(a)):
            n+=i+1
            r.append(n)
        return r
def sin_PrimeroUltimo(a):
    if len(a)==1:
        return a
    else:
        if len(a)==0:
            print ("[]")
        else:
            del a[len(a)-1]
            del a[0]

            return a
def ordenado(a):
    if a == a.sort or a == sorted(a):
        return True
    else:
        return False
def Anagrama(a,b):
    a=a.lower()
    b=b.lower()
    ListA=list(a)
    ListA=sorted(ListA)
    ListB=list(b)
    ListB = sorted(ListB)
    if ListA==ListB:
        return True
    else:
        return False
def dobles(a):
    n=True
    if a==list(set(a)):
        n=False
    return n
def elimina(a):

    return set(a)


def main():
    print("Ejercicio 1:")
    print("° La lista [1,2,3,4,5] regresa la lista acumulada",hacer_Suma([1,2,3,4,5]))
    print("La	lista	[]	regresa	la	lista	acumulada", hacer_Suma([]))
    print("La	lista	[5]	regresa	la	lista	acumulada", hacer_Suma([5]))
    print("Ejercicio 2:")
    print("° La lista [1,2,3,4,5] regresa la lista ", sin_PrimeroUltimo([1, 2, 3, 4, 5]))
    print("La	lista	[1,2,3]	regresa	la	lista	", sin_PrimeroUltimo([1,2,3]))
    print("La	lista	[5]	regresa	la	lista	", sin_PrimeroUltimo([5]))
    print("Ejercicio 3:")
    print("° La lista [1,2,3,4,5] esta ordenada? ", ordenado([1, 2, 3, 4, 5]))
    print("La	lista	[1,3,5,6,7,9,5,4,2]	esta ordenada?	", ordenado([1,3,5,6,7,9,5,4,2]))
    print("La	lista	[5]	esta ordenada?	", ordenado([5]))
    print("Ejercicio 4:")
    print("° Las palabras 'mora' y 'Amor' son anagramas? ", Anagrama("mora","Amor"))
    print("° Las palabras 'papaya' y 'coco' son anagramas?", Anagrama("papaya","coco"))
    print("° Las palabras 'energicamente' y 'generiacamente' son anagramas?", Anagrama("energicamente","generiacamente" ))
    print("Ejercicio 5:")
    print("° La lista [1,2,1,4,5,6,7] tiene dobles?  ", dobles([1,2,1,4,5,6,7]))
    print("La	lista	[1,2,3]	tiene dobles?	", dobles([1,2,3]))
    print("La	lista	[5]	tiene dobles?	", dobles([5]))
    print("Ejercicio 6:")
    print("° La lista [1,2,3,4,5] sin dobles es: ", elimina([1, 2, 3, 4, 5]))
    print("La	lista	[1,1,2,2,3,6,5,4,4,5]	sin dobles es:	", elimina([1,1,2,2,3,6,5,4,4,5]))
    print("La	lista	[5]	sin dobles es:	", elimina([5]))




main()