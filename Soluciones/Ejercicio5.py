import pandas as pd
import codecs

df = pd.read_csv("data/personas.csv")

df["apellido"] = df["apellido_cifrado"].apply(
    lambda x: codecs.decode(str(x), "rot_13")
).str.strip()

resultado = df["apellido"].value_counts().head(1)

print("Apellido más frecuente:", resultado.index[0])
print("Veces:", resultado.iloc[0])