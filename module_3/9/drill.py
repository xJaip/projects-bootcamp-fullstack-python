def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return 'No se puede dividir por 0'
    return a / b

def operaciones(a, b):
    suma = sumar(a, b)
    resta = restar(a, b)
    multiplicacion = multiplicar(a, b)
    division = dividir(a, b)
    resultados = {
        'Suma': suma,
        'Resta': resta,
        'Multiplicación': multiplicacion,
        'División': division
    }
    return resultados

print(operaciones(5, 0))
