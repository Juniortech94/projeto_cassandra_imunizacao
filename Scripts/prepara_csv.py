import pandas as pd

input_path = "imu_COVID_RJ.csv"
output_path = "imu_COVID_RJ_prepared.csv"

print("🔍 Lendo arquivo CSV...")
df = pd.read_csv("imu_COVID_RJ.csv", sep=",", quotechar='"')


print("\n📌 Colunas originais:", df.columns.tolist())
print(df.head(3))

print("\n📌 Total de linhas carregadas:", len(df))

# Renomear colunas
df = df.rename(columns={
    "paciente_endereco_coIbgeMunicipio": "municipio",
    "estabelecimento_municipio_codigo": "estabelecimento_municipio_codigo",
    "vacina_dataAplicacao": "vacina_dataAplicacao",
    "vacina_fabricante_nome": "vacina_fabricante_nome",
    "vacina_descricao_dose": "vacina_descricao_dose"
})

print("\n🔄 Convertendo datas (modo rápido)...")

df['vacina_dataAplicacao'] = pd.to_datetime(
    df['vacina_dataAplicacao'],
    format="%Y-%m-%d",     
    errors="coerce"
)

print("✔ Datas convertidas!")

invalid = df["vacina_dataAplicacao"].isna().sum()
print(f"⚠️ Linhas com data inválida removidas: {invalid}")

df = df.dropna(subset=["municipio", "vacina_dataAplicacao"])

print("🔧 Preenchendo valores nulos...")
df = df.fillna("")

print("\n💾 Salvando CSV final...")
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"\n✅ Arquivo salvo com sucesso: {output_path}")
print(df.head(5))
print(f"\n📌 Total final de linhas: {len(df)}")
