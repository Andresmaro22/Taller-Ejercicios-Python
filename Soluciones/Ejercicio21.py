import pandas as pd

df = pd.read_csv("data/personas.csv")

fecha = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")

cantidad = df[fecha.dt.year < 1960].shape[0]

print(f"La cantidad de personas nacidas antes del año 1960 es: {cantidad}.")