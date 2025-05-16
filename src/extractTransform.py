import requests
import pandas as pd


def requestApiBcb(data: str) -> pd.DataFrame:
    """Funcao para extrair os dados dos meios de pagamentos trimestrais do Banco Central
    Parametros: Data - string - aaaat (Ex:20191)
    Saida: DataFrame - Estrutura de dados do Pandas"""

    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    dados = req.json()

    df = pd.json_normalize(dados["value"])
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])
    return df


dadosBcb = requestApiBcb("20191")
print(dadosBcb.info())
