import pandas as pd
import codecs 
datos = pd.read_csv('data/personas.csv')

texto_original = "Juan"

texto_cifrado = codecs.encode(texto_original, 'rot_13')
print(f'Texto cifrado: {texto_cifrado}')
print(f'Texto original: {texto_original}')

condicion = datos['nombre_cifrado'] == "Whna"
datos_nuevos = datos[condicion]
print("El numero de repeticiones de Juan es:", datos_nuevos.shape[0]) 