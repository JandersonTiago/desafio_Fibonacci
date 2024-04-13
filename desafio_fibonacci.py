def fibonacci(numero):
    # Inicializamos os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    # Iteramos até que o número a seja menor ou igual ao número fornecido
    while a <= numero:
        # Se o número atual for igual ao número fornecido, retornamos True
        if a == numero:
            return True
        # Atualizamos os números da sequência para o próximo valor
        a, b = b, a + b
    # Se chegarmos aqui, o número fornecido não pertence à sequência
    return False

# Solicitamos ao usuário que insira um número para verificar se pertence à sequência de Fibonacci
numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verificamos se o número fornecido pertence à sequência de Fibonacci e imprimimos a mensagem correspondente
if fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
