def busca_binaria(arr, elemento):  #local onde fazemos a declaração da função.
    esquerda = 0
    direita = len(arr) - 1

    while esquerda <= direita:  #criação do loop responsavel por criar um parametro de como deve ser feito a busca
        meio = (esquerda + direita) // 2

        if arr[meio] == elemento:
            return meio
        elif arr[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

#codigo tem interação com usuario.
# Solicita ao usuário que insira os dados separados por espaços e os converte em uma lista de inteiros
entrada = input("Digite os números ordenados separados por espaços: ")
numeros = list(map(int, entrada.split()))

elemento = int(input("Digite o número que você deseja buscar: "))

resultado = busca_binaria(numeros, elemento)

if resultado != -1:
    print(f"O elemento {elemento} foi encontrado na posição {resultado}.")
else:
    print(f"O elemento {elemento} não foi encontrado na lista.")
