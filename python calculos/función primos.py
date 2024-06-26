def es_primo(y):
    if y < 2:
        return f'{y} no es primo'
    for i in range(2, int(y**0.5) + 1):
        if y % i == 0:
            return f'{y} no es primo'
    return f'{y} es primo'

y = int(input('Ingrese su número para saber si es primo: '))
print(es_primo(y))