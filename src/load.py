import sqlite3
import pandas as pd
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, dec: str):
    df.to_csv(nome_arquivo, sep=separador, decimal=dec)
    return


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    conn = sqlite3.connect(nome_banco)
    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()

def salvarMySQL(
        df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
    
    return
