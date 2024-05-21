#**Ejercicio Siete**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase:str=input("ingresa una frase :")
letra:str=input("ingresa una letra :")
contador:int=0
for i in frase:
    if letra in i:
        contador+=1
print(f"las letra {letra} aparece {contador} veces")

#**Ejercicio Ocho**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla la primera letra la letra que se encuentra en medio y la ultima letra separadas por comas(,).
palabra = input("Introduce una palabra: ")
primera_letra = palabra[0]
longitud = len(palabra)
letra_medio = palabra[longitud // 2]
ultima_letra = palabra[-1]
print(f"{primera_letra},{letra_medio},{ultima_letra}")

#**Ejercicio Nueve**
##Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
n = int(input("¿Cuántos números vas a introducir? :"))
if n <= 0:
    print("¡imposible!")
else:
    numeros = []
    num = int(input("Escriba un numero :"))
    numeros += [num]
    for i in range(1, n):
        num = int(input(f"Iescriba un numero mas grande que {num} :"))
        numeros += [num] 
        if num <= numeros[i - 1]:
            print(f" ¡{num} no es mayor que {numeros[i - 1]}!.")
    print("gracias por su colaboracion")