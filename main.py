import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySQL

dadosBcb = requestApiBcb("20191")


salvarCsv(dadosBcb, "src/datasets/meiospagamentosTri.csv", ";", ".")

salvarSQLite(dadosBcb, "src/datasets/dadosbcb.db", "meiospagamentosTri")

salvarMySQL(dadosBcb,"root","localhost","etlbcb","meiosdepagamentostri" )