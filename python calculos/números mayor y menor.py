print('--------------------')

#Desafío de orden de números cree un código que permita: Ingresar números y me indique cuál es el mayor

mi_lista = []# Crear una lista vacía
num_elementos = int(input("¿Cuántos elementos deseas agregar a la lista? "))#número de la lista

for datos in range(num_elementos):#en rango desde el 0 hasta los elementos q pediste antes
    elemento = input("Ingresa un elemento: ")# Pedir al usuario que ingrese cada elemento
    mi_lista.append(elemento)#los elementos

print("Lista después de agregar los elementos:", mi_lista)# Mostrar la lista después de agregar los elementos

print(f'Número mayor de la lista es:',max(mi_lista)) # Mostrar el número mayor de la lista con max
print(f'Número menor de la lista es:',min(mi_lista)) # Mostrar el número menor de la lista con max
print('--------------------')

print('')
#Busque un texto largo. Cree un código que cuente todas las palabras del string.


