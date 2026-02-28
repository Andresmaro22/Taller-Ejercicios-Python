import pandas as pd

df = pd.read_csv("data/personas.csv")

df["ciudad"] = (
    df["ciudad"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace("í","i")
)

cantidad = (df["ciudad"] == "medellin").sum()

print(f"Después del proceso de limpieza, la ciudad de Medellín tiene {cantidad} registros asociados.")