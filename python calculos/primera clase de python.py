nombre='Catalina' #string
edad= 26 #entero
dirección= 'Luna de mar' #string
numeración= 1290 #entero
comuna= 'conchalí' #string
hambre= True #booleano
pi = 3.17 #decimal o flotante

estudiantes=('Antonio','Loreto','Constanza') #lista
comida= ('helado','pizza','sushi','bbq','kimbap','ramen','sandwich') #lista
mascotas=('Chancha','Rocko','Manchas','Cholo','Han','Luke', 'Leelo', 'Princesa') #lista


print(estudiantes[0],estudiantes[1],comida[1],comida[5]) #con una coma se realiza un espacio y los corchetes son el index
print(estudiantes[2]+comida[5]) #con una suma no se realizan espacios
print('Antonio' in estudiantes) #in para verificar si el slag está en el array


print('-----------------------------------------')
#Usar un bucle for para imprimir la tabla de multiplicar del 3
for nun in range(1, 11):
  print(f'3 x {nun} = {3 * nun}')

#Repetir los datos desde el 1 al 100, ya que el 101 no se incluye
for uwu in range(1, 101):
  print(uwu) #el uwu es el bucle, recordar imprimir sino no funciona

#TAREAS
print('-----------------------------------------')
# 1 Programa para determinar si un número del 1 al 10 es par o impar

for num in range(1, 11):  # Recorre los números del 1 al 10
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

print('-----------------------------------------')
# 2 Programa para calcular la suma de los primeros 10 números naturales

suma = 0  # Inicializar la variable de suma en 0

for num in range(1, 11):  # Recorre los números del 1 al 10
    suma += num  # Suma cada número a la variable 'suma'

print(f"La suma de los primeros 10 números naturales es: {suma}")
print('-----------------------------------------')
# 3 Programa para imprimir la tabla de multiplicar del 5

# Número para el cual se imprimirá la tabla de multiplicar
numero = 5

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):  # Recorre los números del 1 al 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print('-----------------------------------------')
# Programa para contar cuántas letras "a" hay en una palabra dada

# Palabra de ejemplo
palabra = input("Introduce una palabra: ")

# Contador de letras 'a'
contador = 0

# Recorre cada letra en la palabra
for letra in palabra:
    if letra == 'a' or letra == 'A':  # Considera tanto 'a' minúscula como 'A' mayúscula
        contador += 1

# Imprime el resultado
print(f"La cantidad de letras 'a' en la palabra '{palabra}' es: {contador}")

print('-----------------------------------------')
# Programa para encontrar el mayor número en una lista

# Lista de ejemplo
numeros = [3, 5, 7, 2, 8, 1, 4, 10, 6, 9]

# Inicializa la variable mayor con el primer elemento de la lista
mayor = numeros[0]

# Recorre cada número en la lista
for num in numeros:
    if num > mayor:
        mayor = num

# Imprime el mayor número encontrado
print(f"El mayor número en la lista es: {mayor}")
print('-----------------------------------------')
# Programa para imprimir todos los números del 1 al 30 que son divisibles por 3

print("Números del 1 al 30 que son divisibles por 3:")

for num in range(1, 31):  # Recorre los números del 1 al 30
    if num % 3 == 0:
        print(num)

print('-----------------------------------------')
# Programa para contar números positivos y negativos en una lista

# Lista de ejemplo
numeros = [10, -1, 2, -3, 5, -8, 7, -6, 4, -9, 0]

# Inicializar contadores
positivos = 0
negativos = 0

# Recorre cada número en la lista
for num in numeros:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

# Imprime los resultados
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

print('-----------------------------------------')