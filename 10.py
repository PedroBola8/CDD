def remover_repetidos_logica(lista):
    i = 0  # Índice inicial
    while i < len(lista):
        j = i + 1  # Índice para comparar com o próximo elemento
        while j < len(lista):
            # Se encontrar um elemento repetido, remove
            if lista[i] == lista[j]:
                lista.pop(j)
            else:
                j += 1  # Só avança o índice se não remover
        i += 1  # Avança o índice principal

    return lista


# Recebe os números digitados pelo usuário e cria uma lista
def receber_numeros():
    lista = []
    print("Digite os números (digite 'fim' para terminar):")

    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fim':  # Condição para encerrar a entrada
            break
        try:
            numero = int(entrada)  # Converte a entrada para inteiro
            lista.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

    return lista


# Parte principal do código
lista_usuario = receber_numeros()  # Recebe os números do usuário
print("Lista antes de remover repetidos:", lista_usuario)

lista_sem_repetidos = remover_repetidos_logica(lista_usuario)  # Remove repetidos
print("Lista sem repetidos:", lista_sem_repetidos)
