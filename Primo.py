"""EJERCICIO. Escribir un programa que pida al usuario un número 
entero y muestre por pantalla si es un número primo o no.
Para saber si un numero es primo o no este debe ser divisible unicamente entre el mismo y 1."""

print("PROGRAMA PARA SABER SI UN NUMERO ES PRIMO O NO ES PRIMO.")

num = int(input("Ingresa un numero entero: ")) 
if num <= 1:
        print("No es primo.")
        
elif num == 2:
        
    print("Es primo.")
else:

    #
    if num % 2 == 0:
        print("No es primo.")
    else: 
        print("Es primo.")
          
       
