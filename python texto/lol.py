import string

def revtexto(eltextodelafuncion):
    """
    Procesa el texto eliminando espacios en blanco al inicio y al final,
    convirtiendo todo el texto a minúsculas, reemplazando signos de puntuación por espacios,
    dividiendo el texto en palabras y contando la frecuencia de cada palabra.

    Args:
    eltextodelafuncion (str): El texto que se va a procesar.

    Returns:
    dict: Un diccionario con la frecuencia de cada palabra.
    """
    # Elimina espacios en blanco al inicio y al final y convierte todo a minúsculas
    koala = eltextodelafuncion.strip().lower()
    
    # Reemplaza los signos de puntuación por espacios
    for punct in string.punctuation:
        koala = koala.replace(punct, ' ')
    
    # Divide el texto en palabras
    koala_words = koala.split()
    
    # Cuenta la frecuencia de cada palabra
    word_frequency = {}
    for word in koala_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

# Ejemplo de uso
eltextodelafuncion = 'En un mundo donde la tecnología domina cada aspecto de nuestra vida, es importante recordar que la verdadera esencia de la humanidad radica en la conexión con el mundo natural que nos rodea. Explorar el mundo a través de los ojos de un niño nos permite redescubrir la magia y la maravilla que a menudo pasamos por alto en nuestro día a día. Juntos, podemos crear un mundo mejor para las generaciones futuras, donde la igualdad, la compasión y el respeto por el mundo sean los pilares de nuestra sociedad.'
word_frequency = revtexto(eltextodelafuncion)
print(word_frequency)