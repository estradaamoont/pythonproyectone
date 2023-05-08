"""Escribir un programa que guarde en un diccionario los precios de los productos de la tabla, 
pregunte al usuario por un producto, un numero de kilos y muestre por pantalla el precio de ese 
numero de kilos de productos. si la fruta no esta en el diccionario debe mostrar un mensaje
 informando de ello
 fruta|precio
 platano|1.35
 manzana|0.80
 pera|0.85
 naranja|0.70"""
print('Alfpo')
print("Fruteria doña Mary\n")
#este es un inventario de frutas disponibles.
print("MENU")
print("Platano. \nManzana. \nPera. \nNaranja \n")
fruta=input("Ingresa el nombre de la fruta: \n")
kilos=int(input("Ingresa la cantidad de kilos: \n"))

def inventario(fruta):
    precio = {
        "Platano":1.35,
        "Manzana":0.80,
        "Pera":0.85,
        "Naranja":0.70
    }

    return precio[fruta]

print(inventario(fruta)*kilos)

#print("No existe en el inventario.")