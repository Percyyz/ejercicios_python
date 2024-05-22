#**Ejercicio Dieciséis**
##Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:
#
##- Debe permitir agregar nuevas tareas a la lista.
##- Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
##- Debe mostrar la lista actual de tareas pendientes.
##- Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
##El menú debe presentar las siguientes opciones:
#
##- Agregar tarea
##- Marcar tarea como completada
##- Mostrar tareas
##- Salir
tareas_pendientes = []
while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    opcion:str= input("Seleccione una opción: ")
    if opcion == "1":
        nueva_tarea:str = input("Ingrese la nueva tarea: ")
        if len(nueva_tarea) > 0:
            tareas_pendientes += [nueva_tarea]
            print("Tarea agregada correctamente.")
        else:
            print("La tarea no puede estar vacía.")
    elif opcion == "2":
        if len(tareas_pendientes) > 0:
            print("Lista de tareas pendientes:")
            for i, tarea in enumerate(tareas_pendientes):
                print(f"{i + 1}. {tarea}")
            num_tarea:int= int(input("Ingrese el número de la tarea completada: "))
            if 1 <= num_tarea <= len(tareas_pendientes):
                tarea_completada = tareas_pendientes[num_tarea - 1]
                tareas_pendientes = tareas_pendientes[:num_tarea - 1] + tareas_pendientes[num_tarea:]
                print(f"La tarea '{tarea_completada}' ha sido marcada como completada.")
            else:
                print("Número de tarea inválido.")
        else:
            print("No hay tareas pendientes para marcar como completadas.")
    elif opcion == "3":
        if len(tareas_pendientes) > 0:
            print("Lista de tareas pendientes:")
            for i, tarea in enumerate(tareas_pendientes):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas pendientes.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

#**Ejercicio Diecisiete**
##Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
#
##- Verificar el saldo de su cuenta.
##- Depositar dinero en su cuenta.
##- Retirar dinero de su cuenta.
##- Salir del programa.
##El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
#
##- Verificar saldo
##- Depositar dinero
##- Retirar dinero
##- Salir
saldo:int = 1000
while True:
    print("\nMenú:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print(f"Su saldo actual es: s/.{saldo} soles.")
    elif opcion == "2":
        cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad_deposito
        print(f"s/.{cantidad_deposito} soles depositados correctamente. Su saldo actual es: s/.{saldo} soles.")
    elif opcion == "3":
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
        if cantidad_retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= cantidad_retiro
            print(f"s/.{cantidad_retiro} soles retirados correctamente. Su saldo actual es: s/.{saldo} soles.")
    elif opcion == "4":
        print("¡Gracias por utilizar nuestro cajero automático!")
        break
    else:
        print("Opción no válida. ¡Inténtelo de nuevo!")

#**Ejercicio Dieciocho**
##Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
while True:
    contrasena1:str = input("Escriba su contraseña: ")
    contrasena2:str = input("Escriba de nuevo su contraseña: ")
    if contrasena2 == contrasena1:
        print("Contraseña confirmada. ¡Hasta la vista!")
        break
    else:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")