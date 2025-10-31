# EJERCICIO 1
for x in range(101):
    print(x)

# EJERCICIO 2
numero = int(input("Ingrese un número entero: "))
if numero == 0:
    digitos = 1
else:
    digitos = 0
    while numero != 0:
        numero //= 10
        digitos += 1
print(f"El número contiene {digitos} dígitos.")

# EJERCICIO 3
a = int(input("Ingrese el primer número entero (a): "))
b = int(input("Ingrese el segundo número entero (b): "))
if a > b:
    a, b = b, a
    print(f"Los números se han intercambiado. Ahora a = {a} y b = {b}.")
if b - a <= 1:
    print("No hay números enteros entre a y b.")
    print("La suma es: 0 ")
else:
    suma = 0
    for num in range(a + 1, b):
        suma += num
        print(f"Los números sumados son: {num}")
    print(f"La suma es: {suma}")

# EJERCICIO 4
print("Ingrese número enteros. El programa termina cuando se ingrese 0. ")
total = 0
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    total += numero

    print("La suma total acumulada es: ", total)

# EJERCICIO 5
import random
print("Adivine el número entre 0 y 9. El que lo adivina en menos intentos gana.")
numeros_secretos = random.randint(0,9)
intentos = 0
while True:
    intento = int(input("Ingrese un número: "))
    intentos += 1
    if intento == numeros_secretos:
        print(f"¡Felicidades! Adivinaste el número {numeros_secretos} en {intentos} intentos.")
        break    
    else:
        print(f"Lo siento, intenta nuevamente.")

# EJERCICIO 6
for numero in range(100, -1, -2):
    print (numero)

# EJERCICIO 7
n = int(input("Ingrese un número entero positivo: "))
if n < 0:
    print("Por favor, ingrese un número positivo.")
else:
    suma = 0
    for i in range(n +1):
        suma += i
        print (f"La suma de los números desde 0 hasta {n} es: {suma}")

# EJERCICIO 8
print("Ingrese 100 números enteros.")
cantidad = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
contador = 0

for i in range(cantidad):
    entrada = input(f"Ingrese el número {i + 1}: ")

    if not entrada.isdigit() and not (entrada.startswith('-') and entrada[1:].isdigit()):
        print("Salida anticipada del programa.")
        break
    numero = int(entrada)
    contador += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos
    elif numero < 0:
        negativos += 1
print(f"Números ingresados: {contador}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

# EJERCICIO 9
print("Ingrese 100 números enteros. ")
cantidad = 100
suma = 0
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero 
    media = suma / cantidad
    print(f"la media de los {cantidad} números ingresados es: {media}")

# EJERCICIO 10
numero = input("Ingrese un número entero: ")
if numero.startswith('-'):
    numero_invertido = '-' + numero[:0:-1]
else:
    numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")

#FIN DEL PROGRAMA

