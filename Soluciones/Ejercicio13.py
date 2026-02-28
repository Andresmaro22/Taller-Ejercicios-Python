import pandas as pd

df = pd.read_csv("data/personas.csv")

cantidad = (~df["salario"].astype(str).str.match(r"^\d+$")).sum()

print(f"Existen {cantidad} registros donde el campo salario contiene caracteres no numéricos.")