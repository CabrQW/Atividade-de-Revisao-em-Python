# 7. Faça um programa que leia um número indeterminado de valores numéricos, encerrando
# a entrada de dados quando for informado um valor igual a −1 (que não deve ser
# armazenado). Após esta entrada de dados, faça:
# • Mostre a quantidade de valores que foram lidos;
# • Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# • Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro;
# • Calcule e mostre a soma dos valores;
# • Calcule e mostre a média dos valores;
# • Calcule e mostre a quantidade de valores acima da média calculada;


valores = []
while True:
    valor = int(input("Digite um valor númerico: "))
    if valor <= -1:
        print('PROGRAMA FINALIZADO')
        break
    valores.append(valor)
#------------------------------------------------------------------------------------------------------------------------------    
qtd_valores = len(valores)        
soma_valores = sum(valores)
media_valores = soma_valores/qtd_valores
acima_media = [valor for valor in valores if valor > media_valores]
#------------------------------------------------------------------------------------------------------------------------------
print(f"A quantidade de valores digitados foi de: {qtd_valores}.")
print(f"A soma dos valores digitados é de: {soma_valores}.")
print(f"A média dos valores digitados foi de: {media_valores}")
print(f"Os valores acima da média são: {acima_media}.")