"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
 pregunte al usuario por la contraseña hasta que este introduzca la contraseña correcta."""

print("BIENVENIDO \n")
contador = 1
while contador <=3:
    usuario =input("Cual es tu nombre de usuario: \n")
    print("Hola ",usuario)      
    contraseña=input("Ingresa la contraseña: \n")
    if  usuario == usuario and contraseña == "maxpanzon":
        print("Contraseña correcta :)")
        contador = 4
    else: 
        print("La contaseña es incorrecta")
        if contador == 3:
            print("La contraseña sigue siendo incorrecta. ")
        contador = contador +1