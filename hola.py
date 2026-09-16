
poema = """
este es un poema
que se encuentra en un archivo de python
y que se puede imprimir en la consola"""
print(poema.replace("poema", "parabola "))

nombre = "roger"
ciudad = "managua"
mensaje = f"hola {nombre}, bienvenido a {ciudad}"
print(mensaje)

producto = (" computadora laptop    ")
print(producto.strip().upper())

otros = "Aprender Python es divertido"
print(len(otros))

palabra = "Programacion"
print(palabra[0])
print(palabra[-1])

frase = "Python es un lenguaje de programacion"
print(frase[0:6])
print(frase[25:37])
print(palabra[::-1])
print("Python" in frase)
print("python" in frase)
print(frase.endswith("programacion"))
print(palabra.isalpha())
print(palabra.isdigit())

texto="El café de la mañana es malo"
print(texto.replace("malo", "excelente"))
print(texto.split(" "))
texto1 = ["Phyton", "es", "un", "lenguaje", "de", "programacion"]
print(" ".join(texto1))
print(texto.title())

precio = float(15.870)
cantidad = int(4)
total = precio * cantidad
print(f"El total a pagar es: {total:.2f}")
galletas = 10
personas = 3
division = galletas // personas
residuo = galletas % personas
print(f"Cada persona recibe {division} galletas y sobran {residuo} galletas")
edad = str("30")
edad_entera = int(edad)
suma = edad_entera + 5
print(f"Si sumamos 5 a la edad, obtenemos: {suma}")