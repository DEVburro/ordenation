def busca_sequencial(lista, elemento):
    for i, item in enumerate(lista):
        if item == elemento:
            return i  # Retorna a posição do elemento encontrado
    return -1  # Retorna -1 se o elemento não for encontrado

# Solicita ao usuário que insira os dados separados por espaços
entrada = input("Insira os dados separados por espaços: ")
elemento_busca = input("Digite o elemento que deseja buscar: ")

# Converte a entrada do usuário em uma lista de inteiros (ou outro tipo, dependendo dos dados)
dados = [int(item) for item in entrada.split()]

# Chama a função de busca sequencial
resultado = busca_sequencial(dados, int(elemento_busca))

# Verifica o resultado da busca
if resultado != -1:
    print(f"Elemento encontrado na posição {resultado}")
else:
    print("Elemento não encontrado na lista.")
