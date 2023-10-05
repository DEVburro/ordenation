# Função para cadastrar funcionários
def cadastrar_funcionarios():
    funcionarios = []
    for i in range(5):
        nome = input(f"Digite o nome do funcionário {i + 1}: ")
        salario = float(input(f"Digite o salário do funcionário {i + 1}: "))
        funcionarios.append((nome, salario))
    return funcionarios

# Função para listar funcionários em ordem crescente de salário
def listar_por_salario_crescente(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda x: x[1])
    return funcionarios_ordenados

# Função para listar funcionários em ordem decrescente de salário
def listar_por_salario_decrescente(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda x: x[1], reverse=True)
    return funcionarios_ordenados

# Função para listar funcionários em ordem alfabética
def listar_por_ordem_alfabetica(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda x: x[0])
    return funcionarios_ordenados

# Função para exibir a lista de funcionários
def mostrar_lista(funcionarios):
    for nome, salario in funcionarios:
        print(f"Nome: {nome}, Salário: {salario}")

# Função principal
def main():
    funcionarios = cadastrar_funcionarios()
    
    print("\nFuncionários em ordem crescente de salário:")
    funcionarios_crescente = listar_por_salario_crescente(funcionarios)
    mostrar_lista(funcionarios_crescente)

    print("\nFuncionários em ordem decrescente de salário:")
    funcionarios_decrescente = listar_por_salario_decrescente(funcionarios)
    mostrar_lista(funcionarios_decrescente)

    print("\nFuncionários em ordem alfabética:")
    funcionarios_alfabetica = listar_por_ordem_alfabetica(funcionarios)
    mostrar_lista(funcionarios_alfabetica)

if __name__ == "__main__":
    main()
