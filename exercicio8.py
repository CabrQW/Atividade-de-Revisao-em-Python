# 8. Faça chamada à API restcountries, que retorna informações sobre países, extraia essas
# informações para as manipular conforme orientações abaixo. Por exemplo, ao acessar

# https://restcountries.com/v3.1/name/brazil, onde brazil é o país escolhido, é retor-
# nado em JSON vários dados sobre o Brasil, em posse disso você deve exibir no programa

# que criará:
# • Nome do país (Brasil), linguagem(s) (“Portuguese”...), região (“Americas”), subregião
# (“South America”) com a capital (“Brasilia”)
# • Sigla da moeda (BRL), nome (“Brazilian real”) e símbolo da moeda (“R$”)
# • Países que fazem fronteira com o Brasil: “ARG”, “BOL”, “COL”, “GUF”, “GUY” ...
# Permita que o usuário insira o nome do país (ex: italy, zambia, japan, canada, germany) e
# são retornados esses dados.

import requests # type: ignore

pais = str(input("Digite o pais que voce quer consultar: "))

url = f'https://restcountries.com/v3.1/name/{pais}'


response = requests.get(url)
data = response.json()

pais_data = data[0]

nome_comum = pais_data["name"]["common"]
linguagem = list(pais_data["languages"].values())[0]
regiao = pais_data["region"]
subregiao = pais_data["subregion"]
capital = pais_data["capital"][0]
moedas = list(pais_data["currencies"].values())[0]
nome_moeda = moedas["name"]
simbolo_moeda = moedas["symbol"]
siglamoeda = list(pais_data["currencies"].keys())[0]
fronteira = "," .join(pais_data.get("borders", []))


print(f"Nome do pais: {nome_comum}")
print(f"Linguagem do pais: {linguagem}")
print(f"Regiao do pais: {regiao}")
print(f"Subregiao do pais: {subregiao}")
print(f"Capital do pais: {capital}")
print(f"Moeda do pais: {nome_moeda}")
print(f"Simbolo da moeda: {simbolo_moeda}")
print(f"Sigla da moeda: {siglamoeda}")
print(f"Paises que fazem fronteiras: {fronteira}")