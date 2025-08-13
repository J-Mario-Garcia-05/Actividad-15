def verificar_edad():
    while True:
        print("\nVERIFICAR EDAD: ")
        try:
            edad = int(input("\tIngrese una edad: "))
            if edad < 0 or edad > 85:
                print("\tEdad no válida, la edad debe estar en un rango de 0 - 85")
                continue
            if edad < 18:
                print("\t¡ES MENOR DE EDAD!")
            else:
                print("\t¡ES MAYOR DE EDAD!")
            try:
                opcion = int(input("\n¿Desea volver a ingresar otra edad?: \n1.Si\t\t 2.No\nR:"))
            except ValueError:
                print("Opción no válida, regresando al menú principal")
                break
            if opcion == 2:
                print("Regresando al menú")
                break
            elif opcion != 1:
                print("Opción no válida, regresando al menú principal")
        except ValueError:
            print("Dato ingresado no válido")

def promedio():
    while True:
        print("\nCALCULAR PROMEDIO: ")
        try:
            a = int(input("\n\tIngrese No.1: "))
            b = int(input("\tIngrese No.2: "))
            c = int(input("\tIngrese No.3: "))
            if a < 0 or b < 0 or c < 0:
                print("\tError: Todos los números tienen que ser mayor a 0")
                continue
            print(f"EL PROMEDIO ES: {(a + b + c) / 3}")
            try:
                opcion = int(input("¿Desea regresar al menú principal?: \n1.Si\t\t 2.No\nR:"))
            except ValueError:
                print("Opción no válida, regresando al menú principal")
                break
            if opcion == 1:
                print("Regresando al menú")
                break
            elif opcion == 2:
                print("Opción no válida, regresando al menú principal")
                break
        except ValueError:
            print("Dato ingresado no válido")

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def ordenar(numero):
    if len(numero) <= 1:
        return numero
    pivote = numero[0]
    menores = [x for x in numero[1:] if x < pivote]
    mayores = [x for x in numero[1:] if x > pivote]
    return ordenar(menores) + pivote + ordenar(mayores)

opcion = 0
while opcion != 5:
    print("\t--MENÚ--")
    print("1.Verificar edad (mayor/menor)")
    print("2.Calcular promedio")
    print("3.Calcular factorial")
    print("4.Ordenar n números")
    print("5.Salir")
    try:
        opcion = int(input("\nSeleccione una opción: "))
        if opcion != 5:
            print(f"\nSe esta dirigiondo a la opción {opcion}")
        match opcion:
            case 1:
                verificar_edad()
            case 2:
                promedio()
            case 3:
                while True:
                    print("\nCALCULAR FACTORIAL:")
                    numero = int(input("\tIngrese un número para calcular su factorial: "))
                    if numero < 0:
                        print("ERROR: El número debe ser mayor a 0")
                        continue
                    numero_fatorial = factorial(numero)
                    print(f"EL FACTORIAL DE {numero} ES: {numero_fatorial}")
                    try:
                        opcion = int(input("¿Desea ingresar otro número?: \n1.Si\t\t 2.No\nR:"))
                    except ValueError:
                        print("Opción no válida, regresando al menú principal")
                        break
                    if opcion == 2:
                        print("Regresando al menú...")
                        break
                    elif opcion != 1:
                        print("Opción no válida, regresando al menú principal")
            case 4:
                numeros = []
                while True:
                    print("\nORDENAR n NÚMEROS")
                    cantidad = int(input("¿Cuántos números desea ingresar? (max 10): "))
                    if cantidad < 0 or cantidad > 10:
                        print("ERROR: El número debe estar en el rango entre 0-10")
                        continue
                    for n in range(cantidad):
                        numeros.append(int(input(f"Ingrese el número {n + 1}")))
                    print("\nNúmeros ingresados:")
                    for i in numeros:
                        print(i, end=", ")
                    print("\nNúmeros ordenados:")
                    for i in ordenar(numeros):
                        print(i, end=", ")
                    try:
                        opcion = int(input("¿Desea ordenar otros números?: \n1.Si\t\t 2.No\nR:"))
                    except ValueError:
                        print("Opción no válida, regresando al menú principal")
                        break
                    if opcion == 2:
                        print("Regresando al menú")
                        break
                    elif opcion != 1:
                        print("Opción no válida, regresando al menú principal")
                        break
                    numeros.clear()
            case 5:
                while True:
                    print("¿Está seguro que desea salir del programa? ")
                    print("1.Si \t\t 2.No")
                    try:
                        opcion = int(input("R: "))
                        if opcion != 1 and opcion != 2:
                            print("Confirmación no válida")
                            continue
                    except ValueError:
                        print("Confirmación no válida")
                    break
                if opcion == 1:
                    print("\nSaliendo, gracias por usar el programa")
                    opcion = 5
                elif opcion == 2:
                    print("Regresando al menú...")

    except ValueError:
        print("Dato ingresado no válido\n")