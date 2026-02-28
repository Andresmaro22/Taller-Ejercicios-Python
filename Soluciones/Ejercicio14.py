import pandas as pd

df = pd.read_csv("data/personas.csv")

salario = pd.to_numeric(df["salario"], errors="coerce")

promedio = salario.mean()

print(f" El salario promedio después del proceso de limpieza es: {promedio:.2f}.")