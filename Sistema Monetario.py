dinero = 500
fertilizante_disponibles = 2
insecticidas = 1
campos = 6
cultivos_cosechados = [["o", "o", "o", "o", "o"], ["o", "o", "o", "o"], ["o", "o", "o"], ["o", "o"], ["o"]]

while True:
    print("BIENVENIDO A LA TIENDA")
    print("1-. Vender producto")
    print("2-. Comprar producto")
    print("3-. Mejorar")
    print("0-. Salir")
    store_buy = int(input("Ingrese la opción que desea de la tienda: "))

    if store_buy == 1:
        print("1-. Vender producto de los cultivos")
        print("2-. Vender producto de la granja")
        print("0-. Salir")
        options = int(input("Ingrese la opción del lado que desea vender: "))

        if options == 1:
            print("1-. Fresa")
            print("2-. Pepino")
            print("3-. Naranja")
            print("4-. Tomate")
            print("5-. Zanahoria")
            print("0-. Salir")
            storess = int(input("Ingrese la opción del producto que desea vender:"))

            if storess == 1:
                print("Dinero:", dinero)
                cant_a = int(input("Ingrese la cantidad de fresas que desea vender: "))
                cantida_a = len(cultivos_cosechados[0])
                if cant_a > 0 and cant_a <= cantida_a:
                    ganancias = cant_a * 6
                    dinero += ganancias
                    print("Lo gastado fue:", ganancias)
                    for i in range(cant_a):
                        cultivos_cosechados[0].pop(0)
                else:
                    print("Cantidad de fresas no disponible")

            # Implementa las otras opciones de venta de cultivos de manera similar...

        elif options == 2:
            print("Parte de la granja")

        elif options == 0:
            print("Vuelva pronto")

        else:
            print("Opción no válida")

    elif store_buy == 2:
        print("1-. Comprar producto para los cultivos")
        print("2-. Comprar producto para la granja")
        print("0-. Salir")
        options = int(input("Ingrese la opción del lado que desea comprar: "))

        if options == 1:
            print("1-. Fertilizante")
            print("2-. Insecticida")
            print("0-. Salir")
            storess = int(input("Ingrese la opción del producto que desea comprar: "))

            if storess == 1:
                print("Dinero:", dinero)
                cantidad = int(input("Ingrese la cantidad de fertilizantes que desea: "))
                if cantidad > 0:
                    costo = cantidad * 80
                    if costo <= dinero:
                        dinero -= costo
                        fertilizante_disponibles += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, compra exitosa\nDinero:", dinero, "\ncantidad de fertilizantes que tiene:",
                              fertilizante_disponibles)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")

            elif storess == 2:
                print("Dinero:", dinero)
                cantidad = int(input("Ingrese la cantidad de insecticidas que desea: "))
                if cantidad > 0:
                    costo = cantidad * 50
                    if costo <= dinero:
                        dinero -= costo
                        insecticidas += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, compra exitosa\nDinero:", dinero, "\nCantidad de Insecticidas que hay: ",
                              insecticidas)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")

            elif storess == 0:
                print("Vuelva pronto")

            else:
                print("Opción no valida")

        elif options == 2:
            print("Parte de la granja")

        elif options == 0:
            print("Vuelva pronto")

        else:
            print("Opción no valida")

    elif store_buy == 3:
        print("1-. Comprar mejora para los cultivos")
        print("2-. Comprar mejora para la granja")
        print("0-. Salir")
        options = int(input("Ingrese la opción del lado que desea mejorar: "))

        if options == 1:
            cantidad = int(input("Ingrese la cantidad de la mejora que desea hacer de campos: "))
            costo = cantidad * 85
            if costo <= dinero:
                dinero -= costo
                campos += cantidad
                print("Lo gastado fue: ", costo)
                print("Felicidades, mejora exitosa\nDinero:", dinero, "\nCampos actuales", campos)

            else:
                print("Dinero insuficiente, regrese cuando el dinero haya aumentado")

        elif options == 2:
            print("Parte de la granja")

        elif options == 0:
            print("Vuelva pronto")

        else:
            print("Opción no valida")

    elif store_buy == 0:
        print("Gracias por visitar la tienda. ¡Vuelva pronto!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
