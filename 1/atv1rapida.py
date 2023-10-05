def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Função para inserir os dados pelo usuário
def input_data():
    data = []
    n = int(input("Quantos números deseja ordenar? "))
    
    for i in range(n):
        num = int(input("Digite o número {}: ".format(i + 1)))
        data.append(num)
    
    return data

if __name__ == "__main__":
    data = input_data()
    sorted_data = quicksort(data)
    
    print("Lista ordenada:")
    print(sorted_data)
