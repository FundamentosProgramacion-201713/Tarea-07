#encoding: UTF-8
#Autor Aaron Villanueva

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

def main():

main()
