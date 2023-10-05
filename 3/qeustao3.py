# Função para cadastrar 10 números
def cadastrar_numeros():
    numeros = []
    for i in range(10):
        numero = float(input(f"Digite o número {i + 1}: "))
        numeros.append(numero)
    return numeros

# Função para encontrar o menor número crescente
def encontrar_menor_crescente(numeros):
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados[0]

# Função para encontrar o maior número e contar quantas vezes ele aparece
def encontrar_maior_e_contar(numeros):
    maior_numero = max(numeros)
    quantidade = numeros.count(maior_numero)
    return maior_numero, quantidade

# Função principal
def main():
    numeros = cadastrar_numeros()

    menor_crescente = encontrar_menor_crescente(numeros)
    print(f"O menor número crescente é: {menor_crescente}")

    maior_numero, quantidade = encontrar_maior_e_contar(numeros)
    print(f"O maior número é: {maior_numero}")
    print(f"Ele aparece {quantidade} vez(es) no vetor.")

if __name__ == "__main__":
    main()
