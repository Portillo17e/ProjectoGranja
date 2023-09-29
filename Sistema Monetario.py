dinero = 500
cultivos_cosechados = [[],[],[],[],[]]
print("BIENVENIDO A LA TIENDA\n1-.Vender prducto\n2-. Comprar producto\n3-. Mejorar\n0-. Salir")
store_buy = int(input("Ingrese la opción que desea de la tienda: "))
while True:
    if store_buy == 1:
        print("1-. Vender producto de los cultivos\n 2-. Vender producto de la granja\n0-. Salir")
        options = int(input("Ingrese la opción del lado que desea vender: "))
        while True:
            if options == 1:
                print("1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoria\n0-. Salir")
                storess = int(input("Ingrese la opcón del producto que desea vender:"))
                while True:
                    if storess == 1:
                        cant_a = int(input("Ingrese la cantidad de fresas que desea vender: "))
                        cantida_a = len(cultivos_cosechados[0])
                        if cant_a > 0 and cant_a <= cantida_a:
                            ganancias = cant_a * 6
                            dinero += ganancias
                            for i in range(cant_a):
                                cultivos_cosechados[0].pop(0)
                        else:
                            print("Cantidad de fresas no disponible")

                    elif storess == 2:
                        cant_p = int(input("Ingrese la cantidad de pepinos que desea vender: "))
                        cantida_p = len(cultivos_cosechados[1])
                        if cant_p > 0 and cant_p <= cantida_p:
                            ganancias = cant_p * 8
                            dinero += ganancias
                            for i in range(cant_p):
                                cultivos_cosechados[1].pop(0)
                        else:
                            print("Cantidad de pepinos no disponible")

                    elif storess == 3:
                        cant_n = int(input("Ingrese la cantidad de Naranjas que desea vender: "))
                        cantida_n = len(cultivos_cosechados[2])
                        if cant_n > 0 and cant_n <= cantida_n:
                            ganancias = cant_n * 8
                            dinero += ganancias
                            for i in range(cant_n):
                                cultivos_cosechados[2].pop(0)
                        else:
                            print("Cantidad de Naranjas no disponible")

                    elif storess == 4:
                        cant_t = int(input("Ingrese la cantidad de tomate que desea vender: "))
                        cantida_t = len(cultivos_cosechados[3])
                        if cant_t > 0 and cant_t <= cantida_t:
                            ganancias = cant_t * 8
                            dinero += ganancias
                            for i in range(cant_t):
                                cultivos_cosechados[3].pop(0)
                        else:
                            print("Cantidad de tomate no disponible")

                    elif storess == 5:
                        cant_z = int(input("Ingrese la cantidad de zanahorias que desea vender: "))
                        cantida_z = len(cultivos_cosechados[4])
                        if cant_z > 0 and cant_p <= cantida_z:
                            ganancias = cant_z * 8
                            dinero += ganancias
                            for i in range(cant_z):
                                cultivos_cosechados[4].pop(0)
                        else:
                            print("Cantidad de zanahorias no disponible")

                    elif storess == 0:
                        print("Vuelva pronto")
                        break

                    else:
                        print("Suministros incompletos o cantidad no válida")

                    print("1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoria\n0-. Salir")
                    storess = int(input("Ingrese la opcón del producto que desea vender:"))

            elif options == 2:
                print("Parte alvisurez")

            elif options == 0:
                print("Vuelva pronto")
                break

            print("1-. Vender producto de los cultivos\n 2-. Vender producto de la granja\n0-. Salir")
            options = int(input("Ingrese la opción del lado que desea vender: "))

    elif store_buy == 2:


    print("BIENVENIDO A LA TIENDA\n1-.Vender prducto\n2-. Comprar producto\n3-. Mejorar\n0-. Salir")
    store_buy = int(input("Ingrese la opción que desea de la tienda: "))
