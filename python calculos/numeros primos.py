#números primos

y=int(input('Ingrese su número para saber si es primo:'))
def prim(y):
  if ((y%2==0) or (y%3==0) or (y%5==0) or (y%7==0)):
    if ((y>0) and (y!=1) and (y!=2) and (y!=3) and (y!=5) and (y!=7)):
      print(y)
      return (f'No es primo')
  elif (y==1):
    print(y)
    return (f'Es primo, es el uno we')
  elif (y<0):
    print(y)
    return (f'No es entero, no es nada')
  else:
    print(y)
    return (f'Es primo')
  
print(prim(y))

