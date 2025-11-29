import pandas as pd
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("amostragem.csv")

# Converter data
df["vacina_dataAplicacao"] = pd.to_datetime(df["vacina_dataAplicacao"])

# Criar o scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df["vacina_dataAplicacao"], df["municipio"], s=5)

plt.xlabel("Data da Aplicação")
plt.ylabel("Código do Município")
plt.title("Distribuição das Aplicações ao Longo do Tempo por Município")
plt.tight_layout()

plt.show()
