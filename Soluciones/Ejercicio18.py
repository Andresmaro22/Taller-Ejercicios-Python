import pandas as pd

df = pd.read_csv("data/personas.csv")

activo = df["activo"].astype(str).str.lower().str.strip()

cantidad = activo.isin(["false","0","no"]).sum()

print(f" Luego de la normalización, {cantidad} registros presentan el campo 'activo' como falso.")