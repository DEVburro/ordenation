def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento atual a ser inserido na parte ordenada
        j = i - 1  # Índice do último elemento na parte ordenada

        # Mova os elementos maiores que key para a direita
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Inserir key na posição correta na parte ordenada
        arr[j + 1] = key

# Solicitar ao usuário que insira os dados separados por espaços
user_input = input("Digite os elementos separados por espaços: ")
user_elements = [int(x) for x in user_input.split()]

# Chamar a função de ordenação por inserção
insertion_sort(user_elements)

# Imprimir a lista ordenada
print("Lista ordenada:", user_elements)