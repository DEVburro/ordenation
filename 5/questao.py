# Função para cadastrar alunos
def cadastrar_alunos():
    alunos = []
    for i in range(8):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nota1 = float(input(f"Digite a nota 1 do aluno {i + 1}: "))
        nota2 = float(input(f"Digite a nota 2 do aluno {i + 1}: "))
        alunos.append((nome, nota1, nota2))
    return alunos

# Função para calcular a média ponderada das notas
def calcular_media_ponderada(nota1, nota2):
    return (2 * nota1 + 3 * nota2) / 5

# Função para listar os alunos ordenados pela média ponderada
def listar_por_media_ponderada(alunos):
    alunos_ordenados = sorted(alunos, key=lambda x: calcular_media_ponderada(x[1], x[2]), reverse=True)
    return alunos_ordenados

# Função para listar os alunos ordenados pela nota 1
def listar_por_nota1(alunos):
    alunos_ordenados = sorted(alunos, key=lambda x: x[1])
    return alunos_ordenados

# Função para listar os alunos reprovados (média < 7) em ordem alfabética
def listar_reprovados(alunos):
    reprovados = [aluno for aluno in alunos if calcular_media_ponderada(aluno[1], aluno[2]) < 7]
    reprovados_ordenados = sorted(reprovados, key=lambda x: x[0])
    return reprovados_ordenados

# Função principal
def main():
    alunos = cadastrar_alunos()
    
    print("\nAlunos ordenados pela média ponderada:")
    alunos_media_ponderada = listar_por_media_ponderada(alunos)
    for aluno in alunos_media_ponderada:
        nome, nota1, nota2 = aluno
        media = calcular_media_ponderada(nota1, nota2)
        print(f"Nome: {nome}, Média Ponderada: {media:.2f}")

    print("\nAlunos ordenados pela nota 1 (crescente):")
    alunos_nota1 = listar_por_nota1(alunos)
    for aluno in alunos_nota1:
        nome, nota1, nota2 = aluno
        print(f"Nome: {nome}, Nota 1: {nota1}")

    print("\nAlunos reprovados (média < 7) em ordem alfabética:")
    alunos_reprovados = listar_reprovados(alunos)
    for aluno in alunos_reprovados:
        nome, _, _ = aluno
        print(f"Nome: {nome}")

if __name__ == "__main__":
    main()
