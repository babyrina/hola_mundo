def solcito(temperatura,foc):
  if isinstance(temperatura, float) and isinstance(foc, str):
    if foc.lower() == 'f' or foc.lower() == 'f°':
      celcius_resultado=(temperatura-32)/1.8
      return f'Tenemos {celcius_resultado} C°'
    elif foc.lower() == 'c' or foc.lower() == 'c°':
      faren_resultado=(temperatura*1.8)+32
      return f'Tenemos {faren_resultado} °F'
    else:
      return('Error, vuelva a ingresar')
  else:
      return('Error, vuelva a ingresar los datos solicitados')

temperatura=float(input('Escribe tu temperatura:'))
foc=str(input('Escribe F° si es Farenheig y C° si es Celsius:')) 

print(solcito(temperatura, foc))