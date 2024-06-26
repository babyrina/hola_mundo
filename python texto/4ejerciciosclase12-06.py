import re
from collections import Counter

#Reemplazar subcadenas
#Dada la cadena "Hola mundo, hola universo", reemplaza todas las ocurrencias de "hola" por "Hola".

hello = 'Hola mundo, hola universo'
nuevo_hello = hello.replace('hola', 'Hola')

print(nuevo_hello)
print('---------')

#Dividir cadenas
#Dada la cadena "manzana,pera,plátano,uva", divídela en una lista de frutas
awa = 'manzana,pera,plátano,uva'
newawa=awa.split(',')
print(len(newawa))
print(newawa)
print('---------')

#Eliminar espacios en blanco
# Dada la cadena " Hola mundo ", elimina los espacios en blanco al inicio y al final.
hello2= ' Hola mundo '
print(hello2)
texto_limpio = hello2.strip()
print(texto_limpio)

print('---------')

#eliminar espacios en blanco al inicio y al final
#convertir la cadena en minúscula
#reemplazar todas las ocurrencias de 'mundo' por 'universo'
#dividir la cadena en palabras
#contar cuantas veces aparece la palabra universo en la lista resultante
texto1=' En un mundo donde la tecnología domina cada aspecto de nuestra vida, es importante recordar que la verdadera esencia de la humanidad radica en la conexión con el mundo natural que nos rodea. Explorar el mundo a través de los ojos de un niño nos permite redescubrir la magia y la maravilla que a menudo pasamos por alto en nuestro día a día. Juntos, podemos crear un mundo mejor para las generaciones futuras, donde la igualdad, la compasión y el respeto por el mundo sean los pilares de nuestra sociedad. '
texto2=texto1.strip().lower().replace('mundo','universo').split(' ')
conteo=texto2.count('universo')

print(texto2)
print('---------')
print(conteo)
print('---------')

#crea una función que tome un párrafo y realice las operaciones:
#elimina espacio en blanco al inicio y final
#convertir todo el texto a minusculas
#reemplazar . , ;:!? por espacios(función de libreria)
#dividir el texto en palabras
#contar la frecuencia de cada palabra y revolver un diccionario tips usar import string
eltextodelafuncion= 'En un mundo donde la tecnología domina cada aspecto de nuestra vida, es importante recordar que la verdadera esencia de la humanidad radica en la conexión con el mundo natural que nos rodea. Explorar el mundo a través de los ojos de un niño nos permite redescubrir la magia y la maravilla que a menudo pasamos por alto en nuestro día a día. Juntos, podemos crear un mundo mejor para las generaciones futuras, donde la igualdad, la compasión y el respeto por el mundo sean los pilares de nuestra sociedad.'

def revtexto(eltextodelafuncion):
    koala = eltextodelafuncion.strip().lower()
    koala = re.sub(r'[.,;:!?]', ' ',koala)
    koala = koala.split()
    return koala

koalaimpreso = revtexto(eltextodelafuncion)
contador = Counter(koalaimpreso)
print(contador)
print(koalaimpreso)

print('---------')
