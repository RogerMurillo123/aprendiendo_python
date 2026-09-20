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

nombres = ["Ana", "Carlos", "Sofia"]
for nombre in nombres:
    print("hola", nombre)

for i in range(1, 11):
    print(5, "x", i, "=", 5 * i)

valores = [2, 7, 4, 9, 10, 3]
suma=0
for num in valores:
    if num %2 == 0:
        suma += num
print("La suma de los números pares es:", suma)

num=5
while num >=1:
    print(num)
    num -= 1

suma = 0
num_ingresados = -1
while num_ingresados != 0:
    num_ingresados = int(input("Ingrese un número (0 para salir): "))
    suma += num_ingresados
print("La suma de los números ingresados es:", suma)

clave = "python"
while True:
    ingreso = input("Ingrese la clave: ")
    ingreso = ingreso.lower()
    if ingreso == clave:
        print("Clave correcta")
        break
    else:
        print("Clave incorrecta, intente nuevamente")
