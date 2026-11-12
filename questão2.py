print("=== EXCURSÃO DA ESCOLA ===")

while True:
    try:
        turmas = int(input("Quantas turmas vão participar? "))

        if turmas > 0:
            break
        else:
            print("Digite um número maior que zero.")

    except ValueError:
        print("Digite um número inteiro.")

nomes = []
inscritos = []

for i in range(turmas):
    nome = input(f"\nNome da turma {i + 1}: ")

    while True:
        try:
            quantidade = int(input(f"Inscritos na turma {nome}: "))

            if quantidade >= 0:
                break
            else:
                print("Digite um número inteiro (0 ou mais).")

        except ValueError:
            print("Digite um número inteiro (0 ou mais).")

    nomes.append(nome)
    inscritos.append(quantidade)

alunos = sum(inscritos)

professores = (alunos + 14) // 15

total_pessoas = alunos + professores

onibus = (total_pessoas + 43) // 44

lugares = onibus * 44 - total_pessoas

custo = onibus * 1800

print("\n=== RESUMO ===")
print(f"Alunos: {alunos}")
print(f"Professores acompanhantes: {professores}")
print(f"Total de pessoas: {total_pessoas}")
print(f"Ônibus necessários: {onibus}")
print(f"Lugares que sobram: {lugares}")
print(f"Custo total: R$ {custo:.2f}")

if alunos > 0:
    valor_aluno = custo / alunos
    print(f"Valor por aluno: R$ {valor_aluno:.2f}")
else:
    print("Valor por aluno: não há alunos inscritos.")

if alunos > 0:
    maior = inscritos.index(max(inscritos))
    print(f"Turma com mais inscritos: {nomes[maior]} ({inscritos[maior]} alunos)")
else:
    print("Nenhuma turma possui inscritos.")