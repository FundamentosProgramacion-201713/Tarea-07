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


def main():

main()
