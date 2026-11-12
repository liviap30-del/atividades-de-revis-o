def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60

    if horas > 0:
        return f"{horas}h{resto:02d}min"

    return f"{resto}min"


def tempo_total(duracoes):
    total = 0

    for duracao in duracoes:
        total += duracao

    return total


def dias_para_terminar(total_minutos, minutos_por_dia=120):
    return (total_minutos + minutos_por_dia - 1) // minutos_por_dia


def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    elif total_minutos <= 900:
        return "Média"
    else:
        return "Intensa"


print("=== MARATONA DE SÉRIE ===")

serie = input("Nome da série: ")

while True:
    try:
        temporadas = int(input("Quantas temporadas? "))
        if temporadas > 0:
            break
        print("Digite um número maior que zero.")
    except ValueError:
        print("Digite um número inteiro.")

duracoes = []

for i in range(1, temporadas + 1):
    while True:
        try:
            episodios = int(input(f"Temporada {i} - número de episódios: "))
            if episodios > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite um número inteiro.")

    while True:
        try:
            duracao = int(input(f"Temporada {i} - duração média do episódio (min): "))
            if duracao > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite um número inteiro.")

    duracoes.append(episodios * duracao)

total = tempo_total(duracoes)

print(f"\n=== {serie.upper()} ===")

for i in range(len(duracoes)):
    print(f"Temporada {i + 1}: {formatar_duracao(duracoes[i])}")

print(f"Total: {formatar_duracao(total)} ({classificar_maratona(total)})")

while True:
    try:
        minutos_dia = int(input("\nQuantos minutos por dia você pode assistir? "))
        if minutos_dia > 0:
            break
        print("Digite um número maior que zero.")
    except ValueError:
        print("Digite um número inteiro.")

dias = dias_para_terminar(total, minutos_dia)
dias_padrao = dias_para_terminar(total)

print(f"Você termina {serie} em {dias} dias.")
print(f"Com 2 horas por dia (padrão), seriam {dias_padrao} dias.")