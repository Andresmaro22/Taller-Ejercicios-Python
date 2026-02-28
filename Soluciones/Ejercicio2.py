import pandas as pd
import codecs 
datos = pd.read_csv('data/personas.csv')

texto_original = "Maria"

texto_cifrado = codecs.encode(texto_original, 'rot_13')
print(f'Texto cifrado: {texto_cifrado}')
print(f'Texto original: {texto_original}')

condicion = datos['nombre_cifrado'] == "Znevn"
datos_nuevos = datos[condicion]
print("El numero de repeticiones de Marias es:", datos_nuevos.shape[0]) 