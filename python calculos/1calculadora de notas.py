
mi_lista = []# Crear una lista vacía
num_elementos = int(input("¿Cuántos elementos deseas agregar a la lista? "))#número de la lista

for datos in range(num_elementos):#en rango desde el 0 hasta los elementos q pediste antes
    elemento = float(input("Ingresa un elemento: "))# Pedir al usuario que ingrese cada elemento
    mi_lista.append(elemento)#los elementos

print("Lista después de agregar los elementos:", mi_lista)# Mostrar la lista después de agregar los elementos
promedio = sum(mi_lista) / num_elementos
print(f'Promedio de la lista es:',promedio) # Mostrar el número mayor de la lista con max

print('')