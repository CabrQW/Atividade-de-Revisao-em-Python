# 10. Faça um programa para motoristas do Uber que, ao inserir o CEP do endereço do
# destino do passageiro ele retorne qual região de São Paulo aquele CEP é. Utilize a
# documentação: https://viacep.com.br/
# Exemplo: ao inserir o CEP 02122-050 o resultado deve ser a mensagem: Bairro: Vila Maria
# Alta, Zona Norte de São Paulo.
# As zonas de São Paulo são: Norte, Sul, Leste, Oeste e Centro (indique também quando o
# destino da corrida é pra fora da grande são paulo, em cidades vizinhas). Esse programa
# Atividade de Revisão em Python - IMPACTA
# será muito útil em relação à segurança dos motoristas, e com ele eles irão poder escolher
# pra qual destino querem ou não aceitar corridas.

import requests 

zonas_sp = {
    "Centro": range(1000, 2000),
    "Norte": range(2000, 3000),
    "Leste": range(3000, 4000),
    "Oeste": range(5000, 6000),
    "Sul": range(4000, 5000)
}

def identificar_zona(cep_num):
    for zona, n in zonas_sp.items():
        if cep_num in n:
            return zona
    return None

cep = input("Digite o CEP (somente números): ")
url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)
data = resposta.json()

bairro = data.get("bairro")
cidade = data.get("localidade")
uf = data.get("uf")

if cidade == "São Paulo":
    cep_num = int(cep[:5])
    zona = identificar_zona(cep_num)
    if zona:
        mensagem = f"Bairro: {bairro}, Zona {zona} de São Paulo."
    else:
        mensagem = f"Bairro: {bairro}, Zona desconhecida de São Paulo."
else:
    mensagem = f"Bairro: {bairro}, {cidade}. Destino fora da Grande São Paulo."

print(mensagem)
