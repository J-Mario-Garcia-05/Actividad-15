opcion = 0
while opcion != 5:
    print("\t--MENÚ--")
    print("1.Verificar edad (mayor/menor)")
    print("2.Calcular promedio")
    print("3.")
    print("4.")
    print("5.Salir")
    try:
        opcion = int(input("\nSeleccione una opción: "))
        if opcion != 5:
            print(f"\nSe esta dirigiondo a la opción {opcion}", end=" ")
        match opcion:
            case 1:
                print("Verificar edad")
            case 5:
                while True:
                    print("¿Está seguro que desea salir del programa? ")
                    print("1.Si")
                    print("2.No")
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