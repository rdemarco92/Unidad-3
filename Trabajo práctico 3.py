#EJERCICIO 1
edad = int(input("Ingrese su edad:"))
if edad > 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
    
#EJERCICIO 2
nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")   
#EJERCICIO 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#EJERCICIO 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print ("Niño/a")
elif edad >= 12 and edad < 18:
    print ("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a Jóven")
else:
    print("Adulto/a")
#EJERCICIO 5
contraseña = input("Ingrese la contraseña: ")
if 8<=(len(contraseña)) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres:")
#EJERCICIO 6
import statistics as stats
numeros_aleatorios = [2, 4, 5, 6, 8, 9, 10, 15, 23, 50]

media = stats.mean(numeros_aleatorios)
mediana = stats.median(numeros_aleatorios)
moda = stats.mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("La distribución tiene sesgo positivo.")
elif moda > mediana > media:
    print("La distribución tiene sesgo negativo.")
else:
    print("No hay sesgo en la distribución.")
#EJERCICIO 7
texto = input("Ingrese una frase o palabra")

if texto[-1].lower() in "aeiou":
    texto = texto + "!"
print(texto)
#EJERCICIO 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para la primer letra en mayúsculas: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida. Debe elegir entre 1, 2 o 3. ")
#EJERCICIO 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve.")
elif 3 <= magnitud < 4:
    print("Leve.")
elif 4 <= magnitud < 5:
    print("Moderado.")
elif 5 <= magnitud < 6:
    print("Fuerte.")
elif 6 <= magnitud < 7:
    print("Muy fuerte.")
elif 7 <= magnitud:
    print("Extremo.")
#EJERCICIO 10
hemisferio = input("Ingrese en que hemisferio se encuentra: ").upper()
año = 2025
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

fecha = año, mes, dia

inicio_invierno = año, 6, 21
inicio_primavera = año, 9, 21
inicio_verano = año, 12, 21
inicio_otoño = año, 3, 21

if hemisferio == "SUR":
    if fecha >= inicio_invierno and fecha < inicio_primavera:
        estacion = "Invierno"
    elif fecha >= inicio_primavera and fecha < inicio_verano:
        estacion = "Primavera"
    elif fecha >= inicio_verano and fecha < inicio_otoño:
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "NORTE":
    if fecha >= inicio_verano and fecha < inicio_otoño:
        estacion = "Verano"
    elif fecha >= inicio_otoño and fecha < inicio_invierno:
        estacion = "Otoño"
    elif fecha >= inicio_invierno and fecha < inicio_primavera:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
print("La estación es:", estacion)