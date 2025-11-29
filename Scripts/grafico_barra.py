import pandas as pd
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("amostragem.csv")

# Agrupar por fabricante
fabricantes = df["vacina_fabricante_nome"].value_counts()

# Plot
plt.figure(figsize=(10, 6))
fabricantes.plot(kind="bar")

plt.xlabel("Fabricante da Vacina")
plt.ylabel("Quantidade de Aplicações")
plt.title("Total de Aplicações por Fabricante")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
