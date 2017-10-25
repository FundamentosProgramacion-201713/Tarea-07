#encoding: UTF-8
#Autor Aaron Villanueva
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

def sumaAcumulada(original):
  lista=original[:]
  lenLista=len(lista)
  for i in range(1,lenLista):
    lista[i]=lista[i]+lista[i-1]
  return(lista)

def eliminarPrimerySegundo(entrada):
  lista=entrada[:]
  if len(lista)>=2:
    lista.pop(0)
    lista.pop()
  elif len(lista)==1:
    lista.pop()
  return(lista)

def verificarListaOrdenada(entrada):
  lista=entrada[:]
  list.sort(lista)
  if lista==entrada:
    conclusion=True
  else:
    conclusion=False
  return(conclusion)

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

def verificarRepetidos(lista):
  for i in lista:
    numero=lista.count(i)
    if numero>1:
      conclusion=True
    else:
      conclusion=False
  return(conclusion)

def eliminarRepetidos(lista):
  for i in lista:
    numero=lista.count(i)
    print(numero)
    if numero>1:
      for j in range(numero-1):
        lista.remove(i)
  return(lista)

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
    
main()
