def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


estudiantes = [
{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
{'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
{'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
{'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
{'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

print('Estudiantes mayores de edad con promedio mayor a 85:')
for estudiante in estudiantes:
    if estudiante['edad'] >= 18 and suma(estudiante['calificaciones'])/3 > 85:
        print(estudiante['nombre'])
        
print('Promedio de calificaciones de estudiantes con edad mayor a 18 y número primo')
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        print(estudiante['nombre'], suma(estudiante['calificaciones'])/3)