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

def extrair_tratar_selic():
    url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoSelic?%24top=1000&%24format=json"
    resposta = requests.get(url)
    dados = resposta.json()

    df = pd.DataFrame(dados['value'])

    print("Colunas recebidas da API:")
    print(df.columns)

    
    colunas_interesse = ['Data', 'Media', 'Minimo', 'Maximo', 'Mediana']
    df = df[colunas_interesse]

    
    df['Data'] = pd.to_datetime(df['Data'])


    
    df.to_csv('src/datasets/selic_expectativas.csv', index=False)
    print(" Dados da Selic extraídos e salvos com sucesso.")