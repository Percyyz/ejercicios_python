#**Ejercicio Trece**
##Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos `SAL` no se apaga.
#
##Esta calculadora funciona de la siguiente manera:
#
##- Recogemos los datos A y B
##- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
##- Si operación es 2 calcula A / B. Vigilamos que B no sea 0 ...
##- Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
print("Calculadora encendida.")
while True:
    valor_a:int =int(input("Introduce el valor de A: "))
    valor_b:int =int(input("Introduce el valor de B: "))
    operacion:str= input("Selecciona la operación (1: Raíz cuadrada de la suma, 2: División, 3: Fórmula): ")
    if operacion == "1":
        resultado = (valor_a + valor_b) ** 2
        print(f"Resultado: {resultado}")
    elif operacion == "2":
        if valor_b != 0:
            resultado = valor_a / valor_b
            print(f"Resultado: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    elif operacion == "3":
        resultado = (valor_a * valor_b) / 2.5
        print(f"Resultado: {resultado}")
    elif operacion == "SAL":
        print("Calculadora apagada.")
        break
    else:
        print("Operación no válida. Inténtalo de nuevo.")

#**Ejercicio Catorce**
##Tenemos la pantalla del móvil bloqueada. Partiendo de un `PIN_SECRETO`, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario `login correcto`. Sino, `llamando ala policía`.
PIN_SECRETO :int= "1234"
max_intentos = 3
intentos = 0
while intentos < max_intentos:
    pin_ingresado :str= input("Introduce el PIN: ")
    if pin_ingresado == PIN_SECRETO:
        print("login correcto")
        break
    else:
        intentos += 1
        print("PIN incorrecto")
if intentos == max_intentos:
    print("llamando a la policía")

#**Ejercicio Quince**
##Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
#
##`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89`
#
##Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.
numero:int = 12  
numero_a, numero_b = 0, 1
count = 0
while count < numero:
    print(numero_a, end=", ")
    numero_a, numero_b = numero_b, numero_a + numero_b
    count += 1