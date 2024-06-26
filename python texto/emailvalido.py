''''crea una función que tome una lista de correos electrónicos y realice las siguientes operaciones:
  elimina espacios en blanco al inicio y al final 
  convertir todo a minuscula
  verificar si tiene un formato válido(@.com)
  devolver una lista de correos válidos'''

import re
email_list=[
   ' Oriana@gmail.com',' ana@gmAil.cl',' gabriEl@gmail.cl ','marcianeKe@gmail.cl ','ytumamA@gmail.cl','yquetecreivo@gmail.cl.com','aslkdjñlhsdflajsdf','shalameavOla@gmail.com ','eeeeeeeeeeeeeeeeeeeeeeeeeeeeee@', 'MIMAMAMELOTEJETOTO','catabella@outlook.com','bornthisway@lgbt.com','potaxianajiafei@avocado.com.com.com.com'
            ]


def hotmail(email_list):
  patron=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  email_validos=[]
  for gmail in (email_list):
    outlook=gmail.strip().lower()
    yahoo=re.findall(patron,outlook)
    if yahoo:
        email_validos.append(yahoo)
  return email_validos


email_validos=hotmail(email_list)
emailgatito=len(email_validos)
print(email_validos)
print(f'Hay {emailgatito} emails en la lista.')
print('----------')
