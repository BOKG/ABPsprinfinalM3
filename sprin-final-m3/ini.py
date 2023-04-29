#● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
#aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
#● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
#● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
#cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
#● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
#● Por cada cuenta debe pedir un número telefónico para contactarse.
#
#● El programa no terminará de preguntar por los números hasta que todas las organizaciones
#tengan un número de contacto asignado.
#● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
#● Se debe guardar como un string.




import time
import random



#Lista de usuarios de la aplicación
usuarios = ["Awakemed", "Telovendo", "AwakeIT", "AwakeGames", "AwakeStore", "AwakeMusic", "AwakeBooks", "AwakeMovies", "AwakeFood", "AwakeTravel"]

#Diccionario de cuentas en el que se guardará el usuario, contraseña y número de contacto
cuentas = {}
#Función para generar contraseña
def generar_pass():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    longitud = 8
    contraseña = "".join(random.sample(caracteres, longitud))
    return contraseña
#Función para validar número de contacto
def validar_numero(numero):
    if len(numero) == 8 and numero.isdigit():
        return True
    else:
        return False
#Ciclo para crear cuentas y pedir números de contacto   
for usuario in usuarios:
    contraseña = generar_pass()
    cuentas[usuario] = contraseña

    while True:
        num = input(f"Ingrese el número de contacto de {usuario}: ")
        if validar_numero(num):
            break
        else:
            print("Número inválido. Debe tener 8 dígitos numéricos.")
    cuentas[usuario] = {"contraseña": contraseña,"celular": num}
#Imprimir cuentas creadas
print("\nCuentas creadas:")
for usuario, datos in cuentas.items():
    print(f"Usuario: {usuario}, Contraseña asignada: {datos['contraseña']}, Celular: {datos['celular']}")
    time.sleep(2)
