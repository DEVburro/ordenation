# Função para cadastrar números únicos
def cadastrar_numeros_unicos():
    numeros = set()
    while len(numeros) < 15:
        numero = int(input(f"Digite o número {len(numeros) + 1}: "))
        numeros.add(numero)
    return sorted(list(numeros))

# Função para realizar busca sequencial
def busca_sequencial(vetor, numero):
    for i, n in enumerate(vetor):
        if n == numero:
            return i
    return -1

# Função para realizar busca binária
def busca_binaria(vetor, numero):
    esquerda, direita = 0, len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == numero:
            return meio
        elif vetor[meio] < numero:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

# Função principal
def main():
    vetor = cadastrar_numeros_unicos()
    
    numero_procurado = int(input("Digite o número que deseja procurar: "))

    indice_sequencial = busca_sequencial(vetor, numero_procurado)
    indice_binaria = busca_binaria(vetor, numero_procurado)

    if indice_sequencial != -1:
        print(f"O número {numero_procurado} está presente no vetor.")
        if indice_sequencial % 2 == 0:
            print(f"Está em uma posição par do vetor.")
        else:
            print(f"Está em uma posição ímpar do vetor.")
    else:
        print(f"O número {numero_procurado} não está no vetor.")

if __name__ == "__main__":
    main()
