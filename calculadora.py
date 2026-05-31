def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("divisão por zero não é permitida")
    return a / b

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(n):
    return n ** 0.5