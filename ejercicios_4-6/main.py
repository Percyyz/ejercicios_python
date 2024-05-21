#**Ejercicio Cuatro**
##Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1,11):
    print(f"la tabla de {i}")
    for n in range(1,13):
        print(f"{i}x{n}={i*n}")       

#**Ejercicio Cinco**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra_usuario:str=input("ingrese una palabra :")
for i in reversed(palabra_usuario):
    print(i)

#**Ejercicio Seis**
##Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.
numero:int = int(input("Introduce un número entero: "))
for i in range(1, numero + 1):
    if (i % 2) != 0:
        linea = ""
        for j in range(i, 0, -2):
            linea += str(j) + " "
        print(linea)