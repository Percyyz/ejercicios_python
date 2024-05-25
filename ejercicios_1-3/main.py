#**Ejercicio Uno**
##Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor de 18 deberá pagar 10 soles.
edad:int=int(input("ingrse su edad :"))
if edad <4:
    print("puede entrar gratis")
elif  4<= edad <= 18:
    print("usted debe pagar 5 soles")
else:
    print("10 soles")

#**Ejercicio Dos**
##Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
palabra:str=input("ingrese una palabra :")
for n in range(10):
    print(palabra)

#**Ejercicio Tres**
##Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero:int=int(input("ingrese un numero entero positivo :"))
for i in range(1,numero+1):
    if i % 2 != 0:
        if i ==1 :
            print(i, end="")
        else:
            print(f",{i}",end="")
print()