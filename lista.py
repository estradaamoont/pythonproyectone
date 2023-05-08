
"""Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y
 muestre por pantalla su media y desviación típica.
"""
print("BIENVENIDO")
lista=[]
lista =input("Para comenzar, escribe numeros separados por comas: ")
lista = lista.split(',')
print("Tu lista es: ",lista)
elementos =len(lista)
#para calcular la media tenemos que sumas todos los numeros dados en lista por el usuario y luego dividirlo entre el total de elementos.
for i in range(elementos):
    lista[i]=int(lista[i])
lista = tuple(lista)
suma=0
suma2=0
for i in lista:
    suma += i
    suma2 += i**2
resultado = suma/elementos
resultado2=(suma2/elementos-resultado**2)**(1/2)
print("La media de la lista es: ",resultado, "y la desviacion tipica es: ",resultado2)
