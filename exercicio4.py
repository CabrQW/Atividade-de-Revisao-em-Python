# 4. Desenvolver um programa para verificar a nota dos alunos em uma prova com 10
# questões. O programa deve seguir os seguintes passos:
# • Perguntar ao aluno a resposta de cada uma das 10 questões.
# • Comparar as respostas fornecidas pelo aluno com o gabarito da prova.
# • Calcular o total de acertos, atribuindo 1 ponto para cada resposta correta.
# • Após cada aluno utilizar o sistema, perguntar se outro aluno deseja fazer a prova.
# Após todos os alunos terem respondido, o programa deve informar:
# • O maior e o menor número de acertos entre os alunos.
# • O total de alunos que utilizaram o sistema.
# • A média das notas da turma.


gabarito_prova = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']


maior_nota = 0
menor_nota = 10
soma_notas = 0
total_alunos = 0

while True:
    print(f"\nAluno {total_alunos + 1}")
    acertos = 0

    for i in range(10):
        resposta = input(f"Resposta da questão {i + 1}: ").strip().upper()
        if resposta == gabarito_prova[i]:
            acertos += 1

    print(f"Você acertou {acertos} de 10 questões.")

 
    if acertos > maior_nota:
        maior_nota = acertos
    if acertos < menor_nota:
        menor_nota = acertos

    soma_notas += acertos
    total_alunos += 1

  
    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()
    if continuar != 'S':
        break


media = soma_notas / total_alunos

print("\n=== Resultados Finais ===")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Total de alunos: {total_alunos}")
print(f"Média da turma: {media:.2f}")
