#encoding: UTF-8
#Autor Aaron Villanueva

#Listas que serán evaluadas en los ejercicios
listaA=[1,2,3,4]
listaB=[4,3,2,1]
listaC=[1,1,2,2,3,3]
listaD=[]
listaE=[1]
listaF=[1,2]
anagramaA="roma"
anagramaB="amor"
anagramaC="amar"
anagramaD="RAMO"
anagramaE="ana"
listasnumericas=[listaA,listaB,listaC,listaD,listaE,listaF]
listasAnagrama=[anagramaA,anagramaB,anagramaC,anagramaD,anagramaE]

#Esta función crea una nueva lista que suma el valor de una lista con el valor anterior
def sumaAcumulada(original):
  lista=original[:]
  lenLista=len(lista)
  for i in range(1,lenLista):
    lista[i]=lista[i]+lista[i-1]
  return(lista)

#Esta función elimine el primer y el último término de una función
def eliminarPrimerySegundo(entrada):
  lista=entrada[:]
  if len(lista)>=2:
    lista.pop(0)
    lista.pop()
  elif len(lista)==1:
    lista.pop()
  return(lista)

#Esta función verifica si la lista provista esta ordenada de menor a mayor
def verificarListaOrdenada(entrada):
  lista=entrada[:]
  list.sort(lista)
  if lista==entrada:
    conclusion=True
  else:
    conclusion=False
  return(conclusion)

#Esta función verifica si un par de cadenas son anagramas. Es decir, si cada una de las letras puede ser reacomodada para crear la otra cadena.
def verificarAnagrama(primer,segundo):
  primer=str.lower(primer)
  segundo=str.lower(segundo)
  primer=list(str(primer))
  segundo=list(str(segundo))
  lenPrimer=len(primer)
  lenSegundo=len(segundo)
  contador=0
  
  if lenPrimer==lenSegundo:
    for i in primer:
      if i in segundo:
        contador+=1
    if contador==lenPrimer:
      conclusion=True
    else:
      conclusion=False
     
    contador=0
    for i in segundo:
      if i in primer:
        contador+=1
    if contador==lenPrimer:
      conclusion=True
    else:
      conclusion=False
  else:
    conclusion=False
    
  return(conclusion)

#Esta función verifica si existen valores repetidos en una lista
def verificarRepetidos(lista):
  lenLista=len(lista)
  if lenLista>=1:
    for i in lista:
      numero=lista.count(i)
      if numero>1:
        conclusion=True
      else:
        conclusion=False
  else:
    conclusion="La cadena no tiene valores"
  return(conclusion)

#Esta función elimina los valores repetidos de una lista
def eliminarRepetidos(original):
  lista=original[:]
  lenLista=len(lista)
  if lenLista>=1:
    for i in lista:
      numero=lista.count(i)
      if numero>1:
        for j in range(numero-1):
          lista.remove(i)
  return(lista)

#Esta función principal aprovecha las listas de listas para realizar una iteración de valores posibles para probar las funciones anteriores.
def main():
  print("Ejercicio 1:")
  for i in listasnumericas:
    print("La lista",i,"regresa la lista acumulada",sumaAcumulada(i))
  print("Ejercicio 2:")
  for i in listasnumericas:
    print("La lista original",i,"regresa",eliminarPrimerySegundo(i))
  print("Ejercicio 3:")
  for i in listasnumericas:
    print("La lista",i,"es ordenada:",verificarListaOrdenada(i))
  print("Ejercicio 4:")
  for i in range(0,5):
    print("La cadena",listasAnagrama[-i],"es anagrama con",listasAnagrama[i-1],verificarAnagrama(listasAnagrama[-i],listasAnagrama[i-1]))
  print("Ejercicio 5:")
  for i in listasnumericas:
    print("La cadena",i,"tiene valores repetidos:",verificarRepetidos(i))
  print("Ejercicio 6:")
  for i in listasnumericas:
    print("La cadena",i,"sin valores repetidos es:",eliminarRepetidos(i))
  
main()
