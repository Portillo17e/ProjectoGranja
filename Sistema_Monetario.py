from Huerto import Huerto
#from Establo import Establo
#
#dinero = 500
#establo = Establo(dinero)


def entrar_tienda(huerto : Huerto, establo, dinero):
    fertilizante_disponibles = huerto.fertilizante_disponibles
    insecticidas = huerto.insecticidas
    campos = huerto.campos
    semillas = huerto.semillas
    cultivos_cosechados = huerto.cultivos_cosechados
    print("BIENVENIDO A LA TIENDA\n1-. Vender prducto\n2-. Comprar producto\n3-. Mejorar\n0-. Salir")
    store_buy = int(input("Ingrese la opción que desea de la tienda: "))
    while True:
        if store_buy == 1:
            print("Dinero:", dinero)
            print("1-. Vender producto de los cultivos\n2-. Vender producto de la granja\n0-. Salir")
            options = int(input("Ingrese la opción del lado que desea vender: "))
            while True:
                if options == 1:
                    print("Dinero:", dinero)
                    print("1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoria\n0-. Salir")
                    storess = int(input("Ingrese la opcón del producto que desea vender: "))
                    while True:
                        if storess == 1:
                            cant_a = int(input("Ingrese la cantidad de fresas que desea vender (6.00): "))
                            cantida_a = len(cultivos_cosechados[0])
                            if cant_a > 0 and cant_a <= cantida_a:
                                ganancias = cant_a * 6
                                dinero += ganancias
                                print("La ganancia fue:", ganancias)
                                for i in range(cant_a):
                                    cultivos_cosechados[0].pop(0)
                            else:
                                print("Cantidad de fresas no disponible")

                        elif storess == 2:
                            cant_p = int(input("Ingrese la cantidad de pepinos que desea vender (8.00): "))
                            cantida_p = len(cultivos_cosechados[1])
                            if cant_p > 0 and cant_p <= cantida_p:
                                ganancias = cant_p * 8
                                dinero += ganancias
                                print("La ganancia fue:", ganancias)
                                for i in range(cant_p):
                                    cultivos_cosechados[1].pop(0)
                            else:
                                print("Cantidad de pepinos no disponible")

                        elif storess == 3:
                            cant_n = int(input("Ingrese la cantidad de Naranjas que desea vender (9.00): "))
                            cantida_n = len(cultivos_cosechados[2])
                            if cant_n > 0 and cant_n <= cantida_n:
                                ganancias = cant_n * 9
                                dinero += ganancias
                                print("Lo gastado fue:", ganancias)
                                for i in range(cant_n):
                                    cultivos_cosechados[2].pop(0)
                            else:
                                print("Cantidad de Naranjas no disponible")

                        elif storess == 4:
                            cant_t = int(input("Ingrese la cantidad de tomate que desea vender (5.00): "))
                            cantida_t = len(cultivos_cosechados[3])
                            if cant_t > 0 and cant_t <= cantida_t:
                                ganancias = cant_t * 5
                                dinero += ganancias
                                print("La ganancia fue:", ganancias)
                                for i in range(cant_t):
                                    cultivos_cosechados[3].pop(0)
                            else:
                                print("Cantidad de tomate no disponible")

                        elif storess == 5:
                            cant_z = int(input("Ingrese la cantidad de zanahorias que desea vender (8.00): "))
                            cantida_z = len(cultivos_cosechados[4])
                            if cant_z > 0 and cant_z <= cantida_z:
                                ganancias = cant_z * 8
                                dinero += ganancias
                                print("La ganancia fue:",ganancias)
                                for i in range(cant_z):
                                    cultivos_cosechados[4].pop(0)
                            else:
                                print("Cantidad de zanahorias no disponible")

                        elif storess == 0:
                            print("Vuelva pronto")
                            break

                        else:
                            print("Suministros incompletos o cantidad no válida")

                        print("Dinero:", dinero)
                        print("1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoria\n0-. Salir")
                        storess = int(input("Ingrese la opcón del producto que desea vender: "))

                elif options == 2:
                    print("Parte alvisurez")

                elif options == 0:
                    print("Vuelva pronto")
                    break

                else:
                    print("Opción no valida")

                print("Dinero:", dinero)
                print("1-. Vender producto de los cultivos\n2-. Vender producto de la granja\n0-. Salir")
                options = int(input("Ingrese la opción del lado que desea vender: "))

        elif store_buy == 2:
            print("Dinero:", dinero)
            print("1-. Comprar producto para los cultivos\n2-. Comprar producto para la granja\n0-. Salir")
            options = int(input("Ingrese la opción del lado que desea comprar: "))
            while True:
                if options == 1:
                    print("Dinero:", dinero)
                    print("1-. Fertilizante\n2-. Insecticida\n3-. Semillas\n0-. Salir")
                    storess = int(input("Ingrese la opción del producto que desea comprar: "))
                    while True:
                        if storess == 1:
                            print("Dinero:", dinero)
                            cantidad = int(input("Ingrese la cantidad de fetilizantes que desea (80.00): "))
                            if cantidad > 0:
                                costo = cantidad * 80
                                if costo <= dinero:
                                    dinero -= costo
                                    fertilizante_disponibles += cantidad
                                    print("Lo gastado fue: ", costo)
                                    print("Felicidades, compra exitosa\nDinero:", dinero, "\ncantidad de fertilizantes que tiene:", fertilizante_disponibles)
                                else:
                                    print("Moneda insuficiente, siga produciendo para hacer la compra")
                            else:
                                print("La cantidad debe ser mayor que 0")

                        elif storess == 2:
                            print("Dinero:", dinero)
                            cantidad = int(input("Ingrese la cantidad de insecticidas que desea (50.00): "))
                            if cantidad > 0:
                                costo = cantidad * 50
                                if costo <= dinero:
                                    dinero -= costo
                                    insecticidas += cantidad
                                    print("Lo gastado fue: ", costo)
                                    print("Felicidades, compra exitosa\nDinero:", dinero, "\nCantidad de Insecticidas que hay: ", insecticidas)
                                else:
                                    print("Moneda insuficiente, siga produciendo para hacer la compra")
                            else:
                                print("La cantidad debe ser mayor que 0")

                        elif storess == 3:
                            print("Dinero:", dinero)
                            cantidad = int(input("Ingrese la cantidad de semillas que desea que desea (3.00): "))
                            if cantidad > 0:
                                costo = cantidad * 3
                                if costo <= dinero:
                                    dinero -= costo
                                    semillas += cantidad
                                    print("Lo gastado fue: ", costo)
                                    print("Felicidades, compra exitosa\nDinero:", dinero, "\nCantidad de semillas que hay: ", semillas)
                                else:
                                    print("Moneda insuficiente, siga produciendo para hacer la compra")
                            else:
                                print("La cantidad debe ser mayor que 0")

                        elif storess == 0:
                            print("Vuelva pronto")
                            break

                        else:
                            print("Opción no valida")

                        print("Dinero:", dinero)
                        print("1-. Fertilizante\n2-. Insecticida\n3-. Semillas\n0-. Salir")
                        storess = int(input("Ingrese la opción del producto que desea comprar: "))

                elif options == 2:
                    establo.mejorar()

                elif options == 0:
                    print("Vueva pronto")
                    break

                else:
                    print("Opción no valida")

                print("Dinero:", dinero)
                print("1-. Comprar producto para los cultivos\n2-. Comprar producto para la granja\n0-. Salir")
                options = int(input("Ingrese la opción del lado que desea comprar: "))

        elif store_buy == 3:
            print("Dinero:", dinero)
            print("1-. Comprar mejora para los cultivos\n2-. Comprar mejora para la granja\n0-. Salir")
            options = int(input("Ingrese la opción del lado que desea mejorar: "))
            while True:
                if options == 1:
                    cantidad = int(input("Ingrese la cantidad de la mejora que desea hacer de campos (85.00): "))
                    costo = cantidad * 85
                    if costo <= dinero:
                        dinero -= costo
                        campos += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, mejora exitosa\nDinero:", dinero, "\nCampos actuales", campos)

                    else:
                        print("Dinero insuficiente, regrese cuando el dinero haya aumentado")

                elif options == 2:
                    establo.vender_suministros()

                elif options == 0:
                    print("Vueva pronto")
                    break

                else:
                    print("Opción no valida")

                print("Dinero:", dinero)
                print("1-. Comprar mejora para los cultivos\n2-. Comprar mejora para la granja\n0-. Salir")
                options = int(input("Ingrese la opción del lado que desea mejorar: "))

        elif store_buy == 0:
            print("Vueva pronto")
            return dinero

        else:
            print("Opción no valida")

        print("Dinero:", dinero)
        print("BIENVENIDO A LA TIENDA\n1-.Vender prducto\n2-. Comprar producto\n3-. Mejorar\n0-. Salir")
        store_buy = int(input("Ingrese la opción que desea de la tienda: "))
