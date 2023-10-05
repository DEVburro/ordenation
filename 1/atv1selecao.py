def ordenacao_por_selecao(arr):
    n = len(arr)
    
    for i in range(n):
        # Encontre o índice do menor elemento restante no array não ordenado
        indice_minimo = i
        for j in range(i+1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
                
        # Troque o elemento mínimo encontrado com o primeiro elemento não ordenado
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

# Solicita ao usuário que insira os números separados por espaço
entrada = input("Digite os números separados por espaço: ")
numeros = [int(x) for x in entrada.split()]

# Chama a função de ordenação por seleção
ordenacao_por_selecao(numeros)

# Exibe o array ordenado
print("Array ordenado:", numeros)
