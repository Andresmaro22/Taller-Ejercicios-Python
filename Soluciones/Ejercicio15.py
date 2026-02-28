import pandas as pd

df = pd.read_csv("data/personas.csv")

salario = pd.to_numeric(df["salario"], errors="coerce")

maximo = salario.max()

print(f"El salario máximo registrado después de limpiar los datos es: {maximo}.")