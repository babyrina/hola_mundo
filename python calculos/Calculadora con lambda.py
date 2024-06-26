def opera(operador, a, b): #defino la operación con operador
        return {  #abro el diccionario
            '1': lambda: a + b,#lambda usa una función pequeña anónima, por lo que usamos el diccionario
            '2': lambda: a - b,#lambda con mini función resta
            '3': lambda: a * b,#lambda con mini función multiplicación
            '4': lambda: a / b #lambda con mini función división
              if b != 0 else 'Error: División por cero' # si b es distinto de 0, pasa. sino, tira 'error división por cero'
        }.get(operador, lambda: "Operador no válido")() #si no se cumple ninguno de los números, se manda operador no válido.

print('  Calculadora  ')
print('Elige la función:')
print('1.- Suma        ')
print('2.- Resta       ')
print('3.- Multiplicación')
print('4.- División')
print('-----------------')

opcion = input("Ingresa el número de la función que deseas usar (1/2/3/4): ")
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

resultado = opera(opcion, a, b)
print(f'Resultado: {resultado}')