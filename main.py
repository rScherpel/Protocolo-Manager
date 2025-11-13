import requests
from api import Rotas
rotas = Rotas()

api_url = rotas.api_teste1

response = requests.get(api_url)
dados = response.json()

numero_protocolo = dados.get("codigo")
data = dados.get("cadastro")
situacao = dados.get("etapa")

print(f"Nº de Protocolo: {numero_protocolo}")
print(f"Data: {data}")
print(f"Situação: {situacao}")
if situacao == "Entregue" or situacao == "Cancelado":
    data_final = dados.get("encerramento")
    print(f"Encerramento: {data_final}")
