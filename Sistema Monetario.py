huerto = 1
hue = 500
abono = 0
insect = 0
class Moneda:
    def __init__(self):
        self.moneda = 250

    def moneda(self):
        print("Moneda:", self.moneda)

    def vender_comida(self):
        print("Moneda:", self.moneda)
        print("¿Que producto desea vender?\n1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoría\n 0-.Salir")
        store = int(input("Ingrese el número correspondiente al producto que desea vender: "))
        while True:
            if store == 1:
                number = int(input("Ingrese la cantidad que desea de fresas: "))
                buy_f = number * 7
                self.moneda = self.moneda + buy_f
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 2:
                number = int(input("Ingrese la cantidad que desea de pepinos: "))
                buy_p = number * 10
                self.moneda = self.moneda + buy_p
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 3:
                number = int(input("Ingrese la cantidad que desea de naranjas: "))
                buy_n = number * 10
                self.moneda = self.moneda + buy_n
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 4:
                number = int(input("Ingrese la cantidad que desea de tomate: "))
                buy_t = number * 7
                self.moneda = self.moneda + buy_t
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 5:
                number = int(input("Ingrese la cantidad que desea de zanahorias: "))
                buy_z = number * 8
                self.moneda = self.moneda + buy_z
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 0:
                print("Proceso realizado")
                break
            else:
                print("Opcion no existente, ingrese una opcion que si exista")

            print("Moneda:", self.moneda)
            print(
                "¿Que producto desea vender?\n1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoría\n 0-.Salir")
            store = int(input("Ingrese el número correspondiente al producto que desea vender: "))

    def comprar_producto(self):
        print("Moneda:", self.moneda)
        print("¿Que producto desea comprar?\n1-. Abono\n2-. Insecticida\n 0-.Salir")
        store = int(input("Ingrese el número correspondiente al producto que desea comprar: "))
        while True:
            if store == 1:
                number = int(input("Ingrese la cantidad que desea de abono: "))
                buy_a = number * 40
                if buy_a <= self.moneda:
                    self.moneda = self.moneda - buy_a
                    abono + number
                    return print("Felicidades, compra exitosa\nMoneda", self.moneda)
                else:
                    print("Moneda insuficiente, siga produciendo para hacer la compra")

            elif store == 2:
                number = int(input("Ingrese la cantidad que desea de insecticida: "))
                buy_i = number * 30
                if buy_i <= self.moneda:
                    self.moneda = self.moneda - buy_i
                    insect + number
                    return print("Felicidades, compra exitosa\nMoneda", self.moneda)

            elif store == 0:
                print("Proceso realizo")
                break

            else:
                print("Opcion no existente, ingrese una opcion que si exista")

            print("¿Que producto desea comprar?\n1-. Abono\n2-. Insecticida\n 0-.Salir")
            store = int(input("Ingrese el número correspondiente al producto que desea comprar: "))

    def mejorar(self):
        challenge = int(input("¿Desea mejorar el huerto?\n1-. Si\n2-. No\n"))
        while True:
            if challenge == 1:
                huerto = huerto + 1
                hue = hue + 50
            elif challenge == 2:
                print("Vuelve pronto")
                break
            else:
                print("Opción no disponible")




