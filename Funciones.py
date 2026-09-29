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

producto={
    "nombre": "laptop",
    "precio": 850.00,
    "stock": 15
}
print(producto)

nota = {
    "matematicas": 90,
    "historia": 90,
    "programacion": 95
}
nota["ciencia"] = 88
promedio = sum(nota.values()) / len(nota)
print("Promedio de notas:", promedio)

capitales = {
    "España": "Madrid",
    "mexico": "Ciudad de México",
    "colombia": "Bogotá"
}
for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}.")