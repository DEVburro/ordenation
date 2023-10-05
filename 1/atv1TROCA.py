def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

def main():
    # Solicita ao usuário que insira números separados por espaços
    input_str = input("Insira números separados por espaços: ")
    
    # Converte a entrada do usuário em uma lista de inteiros
    unsorted_list = [int(x) for x in input_str.split()]
    
    # Chama o algoritmo de ordenação por troca para ordenar a lista
    bubble_sort(unsorted_list)
    
    # Imprime a lista ordenada
    print("Lista ordenada:")
    print(unsorted_list)

if __name__ == "__main__":
    main()
