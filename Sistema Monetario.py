class Moneda:
    def __init__(self):
        self.moneda = 0
        self.abono = 1000000000000000
        self.insecticida = 10000000000000
    def moneda(self):
        print("Moneda:", self.moneda)

    def vender_comida(self):
        print("Moneda:", self.moneda)
        print("¿Que producto desea vender?\n1-. Fresa\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoría\n 0-.Salir")
        store = int(input("Ingrese el número correspondiente al producto que desea vender: "))
        while True:
            if store == 1:
                number = int(input("Ingrese la cantidad que desea de fresas: "))
                buy_f = number * 5
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
                buy_t = number * 5
                self.moneda = self.moneda + buy_t
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 5:
                number = int(input("Ingrese la cantidad que desea de zanahorias: "))
                buy_z = number * 5
                self.moneda = self.moneda + buy_z
                return print("Felicidades, venta exitosa\nMoneda", self.moneda)
            elif store == 0:
                break
            else:
                print("Opcion no existente, ingrese una opcion que si exista")

    def comprar_producto(self):
        print("Moneda:", self.moneda)
        print("¿Que producto desea comprar?\n1-. Abono\n2-. Pepino\n3-. Naranja\n4-. Tomate\n5-. Zanahoría\n 0-.Salir")
        store = int(input("Ingrese el número correspondiente al producto que desea comprar: "))
        while True:
            if store == 1:
                number = int(input("Ingrese la cantidad que desea de abono: "))
                buy_a = number * 40
                self.moneda = self.moneda - buy_a
                return print("Felicidades, compra exitosa\nMoneda", self.moneda)

            if store == 2:
                number = int(input("Ingrese la cantidad que desea de insecticida: "))
                buy_i = number * 60
                self.moneda = self.moneda - buy_i
                return print("Felicidades, compra exitosa\nMoneda", self.moneda)









