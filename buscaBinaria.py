def busca_binaria(array, valor_procurado):
    esquerda = 0
    direita = len(array) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        # Verifica o elemento do meio
        if array[meio] == valor_procurado:
            return meio
        elif array[meio] < valor_procurado:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1  # Retorna -1 se o valor não estiver no array

# Exemplo de uso
array_ordenado = [1, 3, 5, 7, 9, 11, 13]
valor = 7
resultado = busca_binaria(array_ordenado, valor)

print(f"O valor {valor} está no índice {resultado}.")