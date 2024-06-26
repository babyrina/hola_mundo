for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0: #si número es múltiplo de 3 y mayor que 0 ADEMÁS de ser múltiplo de 5 y mayor que 0
    print('fizzbuzz') #imprimir fizzbuzz
  elif i == 24 or i == 55: #condicional, si es igual a 24 número entero O 55 número entero
    print(i)
  elif i % 3 == 0: #condicional, si es múltiplo de 3
    print('buzz') #se imprime buzz
  elif i % 5 == 0: #condicional, si es múltiplo de 5
    print('fizz') #se imprime fizz
  else: #y cualquiera que no cumpla las condiciones anteriores
    print(i) #se imprime el entero del 1 al 100, el último número 101 no se incluye

#optimizado
for number in range(1,101):
  if number % 15 == 0:
    print("Fizzbuzz")
  elif number % 3 == 0 and number != 24: #signo de exclamación con el igual es 'diferente de 24'
    print("fizz") 
  elif number % 5 == 0 and number != 55:
    print("buzz")
  else:
    print(number)