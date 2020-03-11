# Módulo de números de Fibonacci

def fib(n): # escreve a sequência de Fibonacci até n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n): # retorna a sequência de Fibonacci até n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
