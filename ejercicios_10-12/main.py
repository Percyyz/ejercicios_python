#**Ejercicio Diez**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase:str=input("ingresa una frase :")
letra:str=input("ingresa una letra :")
contador:int=0
for i in frase:
    if letra in i:
        contador+=1
print(f"las letra {letra} aparece {contador} veces")

#**Ejercicio Once**
##Escriba un programa que pregunte cuantos números se van a introducir, pidalos esos números (que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.
cantidad:int = int(input("¿Cuántos números vas a introducir? "))
suma:float = 0.0
for i in range(cantidad):
    numero:float= float(input(f"Introduce el número {i+1}: "))
    suma += numero
print(f"La suma de los números introducidos es: {suma}")

#**Ejercicio Doce**
##Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
cantidad:int = int(input("¿Cuántos números vas a introducir? "))
contador_negativos:int=0
if cantidad < 0:
    print("¡imposible!")
else:
    numeros = []
    numeros += [cantidad]
    for i in range(cantidad):
        numero:float = float(input(f"escriba el número {i+1}: "))
        if numero<=0:
           contador_negativos+=1
    print(f" ha escrito {contador_negativos} numero negativo")