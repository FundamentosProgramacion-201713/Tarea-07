#encoding: UTF-8
#Autor Aaron Villanueva

def verificarAnagrama(original):
  lista=original[:]
  lenLista=len(lista)
  for i in range(1,lenLista):
    lista[i]=lista[i]+lista[i-1]
  return(lista)

def eliminarprimerysegundo(entrada):
  lista=entrada[:]
  if len(lista)>=2:
    lista.pop(0)
    lista.pop()
  elif len(lista)==1:
    lista.pop()
  return(lista)

def verificarlistaordenada(entrada):
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
  conteo=0
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
main()
