def heapify(arr, n, i):
    maior = i  # Inicializa o maior como raiz
    left = 2 * i + 1
    right = 2 * i + 2

    # Verifica se o filho da esquerda existe e é maior que a raiz
    if left < n and arr[left] > arr[maior]:
        maior = left

    # Verifica se o filho da direita existe e é maior que a raiz ou o filho da esquerda
    if right < n and arr[right] > arr[maior]:
        maior = right

    # Se o maior não for a raiz, troque os elementos
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]

        # Recursivamente faz a heapify no subárvore afetada
        heapify(arr, n, maior)

def heapSort(arr):
    n = len(arr)

    # Constrói um heap máximo.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca o máximo (raiz) com o último elemento
        heapify(arr, i, 0)

# Entrada de dados do usuário
try:
    n = int(input("Digite o número de elementos: "))
    arr = []

    for i in range(n):
        elemento = int(input(f"Digite o elemento {i + 1}: "))
        arr.append(elemento)

    print("Array desordenado:", arr)
    heapSort(arr)
    print("Array ordenado:", arr)

except ValueError:
    print("Digite um número válido.")
