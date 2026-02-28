import pandas as pd

df = pd.read_csv("data/personas.csv")

fecha = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")

cantidad = fecha.isna().sum()

print(f"Se encontraron {cantidad} registros con formato de fecha diferente a AAAA-MM-DD o inválido.")