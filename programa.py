nombre = input("Ingresa tu nombre: ")
while True:
    edad = input("Ingresa tu edad: ")
    if edad.isdigit():
        break
    print("Error: Por favor, ingresa un número válido para la edad.")
print(f"Hola {nombre}, tienes {edad} años.")
