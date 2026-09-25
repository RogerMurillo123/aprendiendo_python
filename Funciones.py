def bienvenido(nombre_uruario):
    print(f"Bienvenido a nuestro programa, {nombre_uruario}!")
bienvenido("Juan")
bienvenido("María")

def calcular_area(base, altura):
    area = base * altura
    return area
print("El área del rectángulo es:", calcular_area(10, 5))

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print("El número es par:", es_par(8))
print("El número es par:", es_par(11))