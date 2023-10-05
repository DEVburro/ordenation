# Função para cadastrar produtos
def cadastrar_produtos():
    produtos = []
    for i in range(12):
        codigo = int(input(f"Digite o código do produto {i + 1}: "))
        descricao = input(f"Digite a descrição do produto {i + 1}: ")
        preco = float(input(f"Digite o preço do produto {i + 1}: "))
        produtos.append((codigo, descricao, preco))
    return produtos

# Função para realizar busca sequencial
def busca_sequencial(produtos, codigo_alvo):
    comparacoes = 0
    for codigo, _, _ in produtos:
        comparacoes += 1
        if codigo == codigo_alvo:
            return comparacoes
    return comparacoes  # Retorna o número total de comparações se o código não for encontrado

# Função para realizar busca binária
def busca_binaria(produtos, codigo_alvo):
    comparacoes = 0
    produtos_ordenados = sorted(produtos, key=lambda x: x[0])
    esquerda, direita = 0, len(produtos_ordenados) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if produtos_ordenados[meio][0] == codigo_alvo:
            return comparacoes
        elif produtos_ordenados[meio][0] < codigo_alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return comparacoes  # Retorna o número total de comparações se o código não for encontrado

# Função principal
def main():
    produtos = cadastrar_produtos()
    
    codigo_alvo = int(input("Digite o código do produto que deseja encontrar: "))

    comparacoes_sequencial = busca_sequencial(produtos, codigo_alvo)
    print(f"Busca sequencial: {comparacoes_sequencial} comparações")

    comparacoes_binaria = busca_binaria(produtos, codigo_alvo)
    print(f"Busca binária: {comparacoes_binaria} comparações")

if __name__ == "__main__":
    main()
