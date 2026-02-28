import pandas as pd

df = pd.read_csv("data/personas.csv")

activo = df["activo"].astype(str).str.lower().str.strip()

cantidad = activo.isin(["true","1","si"]).sum()

print(f"Después de normalizar el campo 'activo', {cantidad} registros tienen un valor considerado verdadero.")