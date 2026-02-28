import pandas as pd

df = pd.read_csv("data/personas.csv")

df["ciudad"] = df["ciudad"].astype(str).str.strip().str.lower()

cantidad = df["ciudad"].nunique()

print(f"Luego de normalizar los nombres de ciudad, existen {cantidad} ciudades únicas en el dataset.")