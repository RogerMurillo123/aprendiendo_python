numero= int(input("Ingrese un número: "))
if numero >0:
    print("El número es positivo")
elif numero <0:
    print("El número es negativo")
else:
    print("El número es cero")

color = input("Ingrese un color del semáforo: ")
if color.lower() == "rojo":
    print("detenerse")  
elif color.lower() == "amarillo":
    print("precaución")
elif color.lower() == "verde":
    print("avanzar")
else:
    print("Color no válido")

edad = int(input("Ingrese su edad: "))
if edad < 5:
    print("menones de 5 años:gratis")
elif edad >= 5 and edad <= 17:
    print("De 5 a 17 años: $10")
elif edad >= 18 and edad <= 65:
    print("De 18 a 65 años: $20")
else:
    print("De 65 años en adelante: $5 (Descuento adulto mayor)")

lista = ["pan", "leche", "huevos"]
lista.append("mantequilla")
print(lista[0],lista[3]) 
lista.insert(1, "queso") 
lista.pop(2) 
print(lista.pop(2)) 