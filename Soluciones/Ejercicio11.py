import pandas as pd

df = pd.read_csv("data/personas.csv")

df["profesion"] = df["profesion"].astype(str).str.strip().str.lower()

cantidad = df["profesion"].nunique()

print(f"Después de normalizar los datos, existen {cantidad} profesiones únicas registradas.")