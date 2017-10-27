#encoding: utf-8
#coded by Jordan González Bustamante

def exercise6(case):
    return set(case)

def exercise5(case):
    if len(case) != len(set(case)):
        return True
    return False

def exercise4(case, case0):
    case = case.upper()
    case0 = case0.upper()
    case = list(case)
    case0 = list(case0)
    case.sort()
    case0.sort()
    if case == case0:
        return True
    return False

def exercise3(case):
    for i in range(len(case)-1):
        if case[i] > case[i+1]:
            return False
    return True

def exercise2(case):
    return case[1:len(case) - 1]

def exercise1(case):
    n = 0
    result= []
    for i in range(len(case)):
        n = case[i] + n
        result.append(n)
    return result

def main():
    print("""Ejercicio 1:
-------------------------""")
    print("La lista [1,2,3,4,5] regresa la lista acumulada " + str(exercise1([1,2,3,4,5])))
    print("La lista [] regresa la lista acumulada " + str(exercise1([])))
    print("La lista [5] regresa la lista acumulada " + str(exercise1([5])))

    print("""Ejercicio 2:
-------------------------""")
    print("Lista original [1,2,3,4,5], regresa " + str(exercise2([1,2,3,4,5])))
    print("Lista original [1,2,3], regresa " + str(exercise2([1, 2, 3])))
    print("Lista original [a,b,c,d,e,f,g], regresa" + str(exercise2(["a","b","c","d","e","f","g"])))
    print("""Ejercicio 3: ordenado = True, desordenado = False
-------------------------""")
    print("La lista [1,2,3,4,5] regresa " + str(exercise3([1,2,3,4,5])))
    print("La lista [a,b,c,d,e] regresa " + str(exercise3(['a','b','c','d','e'])))
    print("La lista [A, X, B] regresa " + str(exercise3(['A', 'X', 'B'])))
    print("""Ejercicio 4: anagrama = True, diferente = False
-------------------------""")
    print("""La cadena 'Roma' y 'amor' regresan """ + str(exercise4("Roma", "amor")))
    print("""La cadena 'Anita lava la tina' y 'Tina Anita la lava' regresan """ + str(exercise4("Anita lava la tina", "Tina Anita la lava")))
    print("""La cadena 'Estenopo' y 'Paprika' regresan """ + str(exercise4("Estenopo", "paprika")))
    print("""Ejercicio 5: duplicados = True, únicos = False
-------------------------""")
    print("La lista [1,2,3,1,4,5] regresa " + str(exercise5([1,2,3,1,4,5])))
    print("La lista [5,4,3,2,1] regresa " + str(exercise5([5,4,3,2,1])))
    print("La lista [a,d,e,f,c,d] regresa " + str(exercise5(['a', 'd', 'e', 'f', 'c', 'd'])))
    print("""Ejercicio 6:
-------------------------""")
    print("La lista [1,8,3,4,3,1,8,2,7] queda en " + str(exercise6([1,8,3,4,3,1,8,2,7])))
    print("La lista [a,c,e,f,e,e,c,a,d] queda en " + str(exercise6(['a','c','e','f','e','e','c','a','d'])))
    print("La lista [1] queda en " + str(exercise6([1])))
    print

main()