import pandas as pd
df = pd.read_csv('amostragem.csv', sep=';')
print(df.head(5))
print(df.columns)
print(df.info())    