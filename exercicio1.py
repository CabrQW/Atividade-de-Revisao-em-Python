# 1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# • até 20 litros: desconto de 3% por litro
# • acima de 20 litros: desconto de 5% por litro

# Gasolina:
# • até 20 litros: desconto de 4% por litro
# • acima de 20 litros: desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
# da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


preco_da_gasolina = 2.50
preco_do_alcool = 1.90

litro_vendido = float(input('informe quandos litros serão vendidos:'))
tipo_combustivel = str(input('informe o tipo de combustível pelo seguinte código: A-álcool, G-gasolina: '))

if tipo_combustivel == "A":
    valor_final = litro_vendido * preco_do_alcool
    if litro_vendido <= 20:
        valor_final_desconto = valor_final - (valor_final * 0.03)
        print(f'O valor sem desconto era:{valor_final}R$, e com desconto aplicado, o valor final ficou:{valor_final_desconto}R$. ')
    
    else:
        valor_final_desconto = valor_final - (valor_final * 0.05)
        print(f'O valor sem desconto era:{valor_final}R$, e com desconto aplicado, o valor final ficou:{valor_final_desconto}R$. ')

elif tipo_combustivel == "G":
    valor_final = litro_vendido * preco_da_gasolina
    if litro_vendido <= 20:
        valor_final_desconto = valor_final - (valor_final * 0.04)
        print(f'O valor sem desconto era:{valor_final}R$, e com desconto aplicado, o valor final ficou:{valor_final_desconto}R$. ')
    
    else:
        valor_final_desconto = valor_final - (valor_final * 0.06)
        print(f'O valor sem desconto era:{valor_final}R$, e com desconto aplicado, o valor final ficou:{valor_final_desconto}R$. ')

else:
    print('Resposta invalida. tente denovo')