# 6. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# • Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# • Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# • A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
# percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
# o programa permitindo que o usuário digite o salário inicial do funcionário.


ano_admissao = int(input("Informe o ano de admissão do funcionário:"))
salario = float(input("Informe o salário do funcionário:"))
ano = ano_admissao
percentual = 0.015
contagem=1
print(f'Em seu primeiro ano de admissão({ano_admissao}) seu salário era de:{salario} R$.')
while ano <=2025:
    ano+=1
    aumento_salarial = salario + (salario* percentual)
    print(f'Você está na empresa há:{contagem} ano(s) com isso seu salário teve um aumento de:{percentual*100:.2f}% e passou a ser:{aumento_salarial:.2f} R$.')
    percentual*=2
    contagem+=1
    