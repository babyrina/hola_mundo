#Diccionario
auto = {
    'marca':'toyoya',
    'cantidad de ruedas':4,
    'color':'rojo'
}
estudiante = {
    'nombre':'antonio',
    'apellido': 'bello',
    'edad':35
}
 
#si fuera un array:
nombres = ['antonio','loreto']

print(nombres[0]) #imprime lista valor0
print(estudiante['nombre']) #imprime 

print('----------------')

n=0
for sum in range(1,100):
  print(sum+n)

print('----------------')

contador=1
suma=0
while contador<=350:
  suma+= contador
  contador +=1
  print(f'La suma de los números del 1 al 350 es:',suma)

print('--------')

#desafio random
import random
NumeroAleatorio = random.randint (1,10)
intento = 0                                 #Inicializamos la variable de intento fuera del bucle
 
while intento != NumeroAleatorio:
    intento = int(input('Escoge un numero: ')) #intento = int(input('Escoge un número: ')
    if intento == NumeroAleatorio:
        print ('Es el numero correcto')
        break
    else:
        print ('Intenta de nuevo')

