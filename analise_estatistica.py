import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# =============================
# 1. Conectar ao banco de dados SQLite
# =============================
conn = sqlite3.connect("src/datasets/dadosbcb.db")

# Carregar os dados (ajuste o nome da tabela se necessário)
df = pd.read_sql("SELECT * FROM meiosdepagamentostri", conn)
conn.close()

# =============================
# 2. Verificar dados nulos
# =============================
print("Valores nulos por coluna:")
print(df.isnull().sum())

# 3. Converter coluna de data
df['data'] = pd.to_datetime(df['data'])


# 4. Corrigir colunas monetárias (milhões)

monetary_cols = [
    'valorPix', 'valorTED', 'valorTEC', 'valorCheque', 'valorBoleto',
    'valorDOC', 'valorCartaoCredito', 'valorCartaoDebito', 'valorCartaoPrePago',
    'valorTransIntrabancaria', 'valorConvenios', 'valorDebitoDireto', 'valorSaques'
]

for col in monetary_cols:
    if col in df.columns:
        df[col] = df[col] * 1_000_000


# 5. Corrigir colunas de quantidade (milhares)

quant_cols = [
    'quantidadePix', 'quantidadeTED', 'quantidadeTEC', 'quantidadeCheque',
    'quantidadeBoleto', 'quantidadeDOC', 'quantidadeCartaoCredito',
    'quantidadeCartaoDebito', 'quantidadeCartaoPrePago',
    'quantidadeTransIntrabancaria', 'quantidadeConvenios',
    'quantidadeDebitoDireto', 'quantidadeSaques'
]

for col in quant_cols:
    if col in df.columns:
        df[col] = df[col] * 1_000

# =============================
# 6. Filtrar apenas colunas de Pix e Cartões
# =============================
pix_cartoes_cols = [
    'data',
    'valorPix', 'valorCartaoCredito', 'valorCartaoDebito', 'valorCartaoPrePago',
    'quantidadePix', 'quantidadeCartaoCredito', 'quantidadeCartaoDebito', 'quantidadeCartaoPrePago'
]

df = df[[col for col in pix_cartoes_cols if col in df.columns]]

# =============================
# 7. Estatísticas descritivas
# =============================
print("\nMédia:")
print(df.mean(numeric_only=True))

print("\nMediana:")
print(df.median(numeric_only=True))

print("\nModa:")
print(df.mode(numeric_only=True).iloc[0])

print("\nVariância:")
print(df.var(numeric_only=True))

print("\nDesvio Padrão:")
print(df.std(numeric_only=True))

print("\nAmplitude (max - min):")
print(df.max(numeric_only=True) - df.min(numeric_only=True))



# Histograma do valorPix
if 'valorPix' in df.columns:
    sns.histplot(df['valorPix'], kde=True, bins=30)
    plt.title("Histograma - valorPix")
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()

# Boxplot dos cartões
cartoes = ['valorCartaoCredito', 'valorCartaoDebito', 'valorCartaoPrePago']
cartoes_existentes = [col for col in cartoes if col in df.columns]

if cartoes_existentes:
    sns.boxplot(data=df[cartoes_existentes])
    plt.title("Boxplot - Cartões")
    plt.tight_layout()
    plt.show()

# Série Temporal - valorPix
if 'valorPix' in df.columns:
    df_sorted = df.sort_values('data')
    plt.plot(df_sorted['data'], df_sorted['valorPix'], marker='o')
    plt.title("Série Temporal - valorPix")
    plt.xlabel("Data")
    plt.ylabel("Valor")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
