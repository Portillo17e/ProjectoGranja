class Monetaria:
    def __init__(self):
        self.moneda = 500
        self.gallina = 1
        self.vacas = 1
        self.ovejas = 1
        self.comida_gallina = 1
        self.comida_vaca = 1
        self.comida_ovejas = 1
        self.huevos = 1
        self.lana = 1
        self.leche_litro = 1

    def mostrar_moneda(self):
        print("Moneda:", self.moneda)

    def vender_suministros(self):
        print("Moneda:", self.moneda)
        print("¿Que producto desea vender?\n1-. Huevos\n2-. Leche\n3-. Lana\n\n 0-.Salir")
        store = int(input("Ingrese el número correspondiente al producto que desea vender: "))
        while True:
            if store == 1:
                variable = int(self.moneda)
                number = int(input("Ingrese la cantidad que desea de Huevos: "))
                buy_f = number * 4
                new = variable + buy_f
                self.moneda = str(new)
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 2:
                variabl = int(self.moneda)
                number = int(input("Ingrese la cantidad de litros que desea de leche: "))
                buy_p = number * 14
                ne = variabl + buy_p
                self.moneda = str(ne)
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 3:
                variab = int(self.moneda)
                number = int(input("Ingrese la cantidad de rollos de lana que desea: "))
                buy_n = number * 8
                n = variab + buy_n
                self.moneda = str(n)
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 0:
                print("Proceso realizado")
                break
            else:
                print("Opcion no existente, ingrese una opcion que si exista")

            print("Moneda:", self.moneda)
            print("¿Que producto desea vender?\n1-. Huevos\n2-. Leche\n3-. Lana\n\n 0-.Salir")
            store = int(input("Ingrese el número correspondiente al producto que desea vender: "))

    def comprar_producto(self):
        print("Moneda:", self.moneda)
        print("¿Que producto desea comprar?\n1-. Comida para oveja\n2-. Comida para vaca\n3-. Comida para gallinas\n0-.Salir")
        store = int(input("Ingrese el número correspondiente al producto que desea comprar: "))
        while True:
            if store == 1:
                number = int(input("Ingrese la cantidad de bolsas de comida para oveja que desea: "))
                buy_ov = number * 35
                if buy_ov <= self.moneda:
                    variable = int(self.moneda)
                    new = variable - buy_ov
                    self.moneda = str(new)
                    ove = int(self.comida_ovejas)
                    suma = ove + number
                    self.comida_ovejas = str(suma)
                    return print("Felicidades, venta exitosa\nMoneda", self.moneda, "\nLa cantidad de bolsas de comida para oveja es: ",self.comida_ovejas)
                else:
                    print("Moneda insuficiente, siga produciendo para hacer la compra")

            elif store == 2:
                number = int(input("Ingrese la cantidad de bolsas de comida para vaca que desea: "))
                buy_va = number * 40
                if buy_va <= self.moneda:
                    variable = int(self.moneda)
                    new = variable - buy_va
                    self.moneda = str(new)
                    cab = int(self.comida_vaca)
                    suma = cab + number
                    self.comida_vaca = str(suma)
                    return print("Felicidades, venta exitosa\nMoneda", self.moneda,"\nLa cantidad de bolsas de comida para vaca es: ", self.comida_vaca)
                else:
                    print("Moneda insuficiente, siga produciendo para hacer la compra")

            elif store == 3:
                number = int(input("Ingrese la cantidad de bolsas de comida para gallinas que desea: "))
                buy_ga = number * 40
                if buy_ga <= self.moneda:
                    variable = int(self.moneda)
                    new = variable - buy_ga
                    self.moneda = str(new)
                    cab = int(self.comida_gallina)
                    suma = cab + number
                    self.comida_gallina = str(suma)
                    return print("Felicidades, venta exitosa\nMoneda", self.moneda,"\nLa cantidad de bolsas de comida para gallina es: ", self.comida_vaca)
                else:
                    print("Moneda insuficiente, siga produciendo para hacer la compra")

            elif store == 0:
                print("Proceso realizo")
                break

            else:
                print("Opcion no existente, ingrese una opcion que si exista")

            print("Moneda:", self.moneda)
            print("¿Que producto desea comprar?\n1-. Comida para oveja\n2-. Comida para vaca\n3-. Comida para gallinas\n0-.Salir")
            store = int(input("Ingrese el número correspondiente al producto que desea comprar: "))


    def mejorar(self):
        challenge = int(input("¿Desea mejorar algo de su granja?\n1-. Si\n2-. No\n"))
        while True:
            if challenge == 1:
                option = int(input("¿Que desea mejorar?\n1-. Espacio de gallinas\n2-. Espacio de ovejas\n3-. Espacio de vacas\n0-. Salir"))
                while True:
                    if option == 1:
                        cantidad = int(input("Ingrese la cantidad de espacios de gallinas que desea: "))
                        buy_g = cantidad  * 65
                        if buy_g <= self.moneda:
                            variable = int(self.moneda)
                            new = variable - buy_g
                            self.moneda = str(new)
                            galli = int(self.gallina)
                            suma = galli + cantidad
                            self.gallina = str(suma)
                            return print("Felicidades, venta exitosa\nMoneda", self.moneda, "\nGallinas y espacios actuales", self.gallina)
                        else:
                            print("No cuenta con la moneda para hacer mejoras")

                    elif option == 2:
                        cantida = int(input("Ingrese la cantidad de espacios de ovejas que desea: "))
                        buy_o = cantida * 85
                        if buy_o <= self.moneda:
                            variabl = int(self.moneda)
                            new = variabl - buy_g
                            self.moneda = str(new)
                            ove = int(self.ovejas)
                            suma = ove + cantidad
                            self.ovejas = str(suma)
                            return print("Felicidades, venta exitosa\nMoneda", self.moneda, "\nOvejas y espacios actuales", self.ovejas)
                        else:
                            print("No cuenta con la moneda para hacer mejoras")

                    elif option == 3:
                        cantidad = int(input("Ingrese la cantidad de espacios de vacas que desea: "))
                        buy_v = cantidad * 65
                        if buy_v <= self.moneda:
                            variab = int(self.moneda)
                            new = variab - buy_g
                            self.moneda = str(new)
                            vac = int(self.vacas)
                            suma = vac + cantidad
                            self.vacas = str(suma)
                            return print("Felicidades, venta exitosa\nMoneda", self.moneda, "\nVacas y espacios actuales", self.vacas)
                        else:
                            print("No cuenta con la moneda para hacer mejoras")

                    elif option == 0:
                        print("Vuelva pronto")
                        break

                    else:
                        print("Opción no valida")

                    option = int(input("¿Que desea mejorar?\n1-. Espacio de gallinas\n2-. Espacio de ovejas\n3-. Espacio de vacas\n0-. Salir"))

            elif challenge == 2:
                print("Vuelva pronto")
                break
            else:
                print("Opción no valida")
