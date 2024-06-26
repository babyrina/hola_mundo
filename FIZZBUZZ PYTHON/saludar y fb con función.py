# Escribir una función que salude
def saludar(x):
  print(f"¡Hola {x}!")

saludar('Pedro')
saludar('Juan Carlos')
saludar('Mariana')
print('-------')

#traspasa el código de fizzbuzz a una función
x=int(input('Ingrese su número para saber si es FizzBuzz:'))
def fb(x):
  if (x%3== 0 and x%5==0):
    print(x)
    return (f'El número es FizzBuzz')
  elif (x%5==0):
    print(x)
    return (f'El número es Fizz')
  elif (x%3==0):
    print (x)
    return (f'El número es Buzz')
  else:
    print(x)
    return (f'No es ni Buzz ni Fizz, no es ná')
print(fb(x))
print('----------------')

#números primos