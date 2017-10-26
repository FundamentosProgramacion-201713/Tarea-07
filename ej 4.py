#encoding UTF-8
#Jaime Orlando López Ramos





def esAnagrama(p1, p2):
    if p1 == p2:
        return True
    else:
        return False

    pass


def main():
    p1 = input("Ingrese la primera palabra: ")
    p1 = list(p1)
    p1 = sorted(p1)
    print(p1)
    p2 = input("Ingrese la segunda palabra: ")
    p2 = list(p2)
    p2= sorted(p2)
    print(p2)
    x = esAnagrama(p1, p2)
    print(x)





main()