import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import numpy as np

# Conectar ao banco de dados
conn = sqlite3.connect("src/datasets/dadosbcb.db")
df = pd.read_sql("SELECT * FROM meiosdepagamentostri", conn)
conn.close()

# Converter a coluna de data
df['data'] = pd.to_datetime(df['data'])

# Corrigir valores monetários (milhões)
monetary_cols = [
    'valorPix', 'valorCartaoCredito', 'valorCartaoDebito', 'valorCartaoPrePago'
]
for col in monetary_cols:
    if col in df.columns:
        df[col] = df[col] * 1_000_000

# Corrigir valores quantitativos (milhares)
quant_cols = [
    'quantidadePix', 'quantidadeCartaoCredito', 'quantidadeCartaoDebito', 'quantidadeCartaoPrePago'
]
for col in quant_cols:
    if col in df.columns:
        df[col] = df[col] * 1_000

# ================================
# 1. Média ponderada (exemplo com valorPix e quantidadePix)
# ================================
if 'valorPix' in df.columns and 'quantidadePix' in df.columns:
    media_ponderada = np.average(df['valorPix'], weights=df['quantidadePix'])
    print(f"Média ponderada valorPix (pesada por quantidadePix): {media_ponderada:,.2f}")

# ================================
# 2. Quartis e IQR
# ================================
for col in monetary_cols:
    if col in df.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        print(f"\n{col} - Q1: {q1:,.2f}, Q3: {q3:,.2f}, IQR: {iqr:,.2f}")

# ================================
# 3. Outliers (usando IQR)
# ================================
def identificar_outliers(col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]
    return outliers

# Exibir outliers em valorCartaoCredito (exemplo)
if 'valorCartaoCredito' in df.columns:
    outliers_credito = identificar_outliers('valorCartaoCredito')
    print(f"\nOutliers em valorCartaoCredito: {len(outliers_credito)} registros")
    print(outliers_credito[['data', 'valorCartaoCredito']])

# ================================
# 4. Estatísticas gerais com describe()
# ================================
print("\nResumo estatístico com describe():")
print(df.describe())
