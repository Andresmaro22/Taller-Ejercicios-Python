import pandas as pd

df = pd.read_csv("data/personas.csv")

salario = pd.to_numeric(df["salario"], errors="coerce")

minimo = salario.min()

print(f"El salario mínimo encontrado tras la limpieza del dataset es: {minimo}.")