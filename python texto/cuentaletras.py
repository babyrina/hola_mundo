#ejercicio 1, variable 1
contador = 1 #
suma = 0 #marca desde la caja 0 hasta el 1

while contador<=10:
  suma+= contador
  contador +=1
  print(f'La suma de los números del 1 al 10 es:',suma)

print(f'--------')

#ejercicio 1, variable 2 Bianca GOD
sum=0
cuent=1
while cuent<=10:
  sum+=cuent
  print(f'Al sumar {sum-cuent} + {cuent}, da como resultado: {sum}')
  cuent+=1
print(f'La suma de los primeros 10 números naturales es: {sum}')

print(f'--------')

#crea un código que cuente las letras de tu primer nombre

while True:
  nombre=input('Escribe tu nombre:')
  nombre_borrar= len(nombre)-nombre.count(' ') #PARA QUE NO CUENTE LOS ESPACIOS
  print(f'Tu nombre tiene {nombre_borrar} letras')
  break
#tire error o que se devuelva numeros

