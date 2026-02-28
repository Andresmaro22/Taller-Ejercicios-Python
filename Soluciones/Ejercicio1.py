import pandas as pd
df = pd.read_csv("data/personas.csv")
cantidad = (~df["id"].astype(str).str.isnumeric()).sum()
print("Filas con id no numérico:", cantidad)