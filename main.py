import pandas as pd
from src.extractTransform import requestApiBcb, extrair_tratar_selic
from src.load import salvarCsv, salvarSQLite  

dadosBcb = requestApiBcb("20191")

salvarCsv(dadosBcb, "src/datasets/meiospagamentosTri.csv", ";", ".")
salvarSQLite(dadosBcb, "src/datasets/dadosbcb.db", "meiospagamentosTri")


extrair_tratar_selic()
