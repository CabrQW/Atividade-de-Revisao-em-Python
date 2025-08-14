# 9. Neste exercício, você irá criar um programa que solicita ao usuário a sigla de uma moeda
# e exibe a cotação do Real (BRL) em relação a essa moeda. O objetivo é fazer uma
# requisição à API de cotações de moedas, tratar a resposta e apresentar o valor do Real
# em face da moeda escolhida. Você deve usar essa API: https://api.exchangerate-api.
# com/v4/latest/BRL onde BRL é a sigla da moeda alvo (Real).
# • Solicite ao usuário que insira a sigla da moeda desejada (por exemplo, “USD” para Dólar
# Americano, “EUR” para Euro, “GBP” para Libra Esterlina, etc.).
# • Faça uma requisição à API de cotações de moedas para obter a taxa de câmbio do Real
# em relação à moeda informada pelo usuário.
# • Extraia o valor da cotação do Real em relação à moeda solicitada.
# • Exiba uma mensagem clara e informativa, como “O Real vale X [nome da moeda]”, onde
# X é o valor da cotação. Ex: O Real vale 5.42 dólares americanos, traduzindo a sigla da
# moeda para o nome completo (USD para dólares americanos).

import requests # type: ignore


moedas_nomes = {
    "USD": "dólares americanos",
    "EUR": "euros",
    "GBP": "libras esterlinas",
    "JPY": "ienes japoneses",
    "ARS": "pesos argentinos",
    "CHF": "francos suíços"
}


sigla = str(input("Digite a sigla que voce quer consultar a cotação: ")).upper()

url = f'https://v6.exchangerate-api.com/v6/577a033201adabead38c273e/latest/{sigla}'

nome_moeda = moedas_nomes.get(sigla)

response = requests.get(url)
data = response.json()

id_real = data["conversion_rates"]["BRL"]


print(f"O real vale {id_real:.2f} em {nome_moeda}")