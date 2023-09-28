# Variable global para el dinero
dinero = 500

# Clase Granja
class Granja:
    def __init__(self):
        # Inicialización de las variables de la granja
        self.gallinas = 1
        self.ovejas = 1
        self.vacas = 1
        self.comida_gallina = 1
        self.comida_vaca = 1
        self.comida_ovejas = 1
        self.huevos = 1
        self.lana = 1
        self.leche_litro = 1

    # Función para mostrar la cantidad de dinero
    def mostrar_dinero(self):
        print("Dinero:", dinero)

    # Función para vender suministros
    def vender_suministros(self):
        while True:
            self.mostrar_dinero()
            print("¿Qué producto desea vender?\n1-. Huevos\n2-. Leche\n3-. Lana\n\n0-. Salir")
            opcion = int(input("Ingrese el número correspondiente al producto que desea vender: "))

            if opcion == 1:
                cantidad = int(input("Ingrese la cantidad que desea de Huevos: "))
                if cantidad > 0 and cantidad <= self.huevos:
                    ganancia = cantidad * 4
                    global dinero
                    dinero += ganancia
                    self.huevos -= cantidad
                    print("Felicidades, venta exitosa\nDinero:", dinero)
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 2:
                cantidad = int(input("Ingrese la cantidad de litros que desea de leche: "))
                if cantidad > 0 and cantidad <= self.leche_litro:
                    ganancia = cantidad * 14
                    global dinero
                    dinero += ganancia
                    self.leche_litro -= cantidad
                    print("Felicidades, venta exitosa\nDinero:", dinero)
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 3:
                cantidad = int(input("Ingrese la cantidad de rollos de lana que desea: "))
                if cantidad > 0 and cantidad <= self.lana:
                    ganancia = cantidad * 8
                    global dinero
                    dinero += ganancia
                    self.lana -= cantidad
                    print("Felicidades, venta exitosa\nDinero:", dinero)
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 0:
                print("Proceso realizado")
                break

            else:
                print("Opción no válida, ingrese una opción válida.")

    # Función para comprar productos
    def comprar_producto(self):
        while True:
            self.mostrar_dinero()
            print("¿Qué producto desea comprar?\n1-. Comida para oveja\n2-. Comida para vaca\n3-. Comida para gallinas\n0-. Salir")
            opcion = int(input("Ingrese el número correspondiente al producto que desea comprar: "))
            if opcion == 1:
                cantidad = int(input("Ingrese la cantidad de bolsas de comida para oveja que desea: "))
                if cantidad > 0:
                    costo = cantidad * 50
                    if costo <= dinero:
                        global dinero
                        dinero -= costo
                        self.comida_ovejas += cantidad
                        print("Felicidades, compra exitosa\nDinero:", dinero)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")
            elif opcion == 2:
                cantidad = int(input("Ingrese la cantidad de bolsas de comida para vaca que desea: "))
                if cantidad > 0:
                    costo = cantidad * 50
                    if costo <= dinero:
                        global dinero
                        dinero -= costo
                        self.comida_vaca += cantidad
                        print("Felicidades, compra exitosa\nDinero:", dinero)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")
            elif opcion == 3:
                cantidad = int(input("Ingrese la cantidad de bolsas de comida para gallinas que desea: "))
                if cantidad > 0:
                    costo = cantidad * 50
                    if costo <= dinero:
                        global dinero
                        dinero -= costo
                        self.comida_gallina += cantidad
                        print("Felicidades, compra exitosa\nDinero:", dinero)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")
            elif opcion == 0:
                print("Proceso realizado")
                break
            else:
                print("Opción no válida, ingrese una opción válida.")

    # Función para mejorar la granja
    def mejorar(self):
        print("¿Desea mejorar algo de su granja?\n1-. Si\n2-. No\n")
        opcion = int(input("Ingrese su elección: "))
        if opcion == 1:
            print("¿Qué desea mejorar?\n1-. Espacio de gallinas\n2-. Espacio de ovejas\n3-. Espacio de vacas\n0-. Salir")
            while True:
                eleccion = int(input("Ingrese el número correspondiente a lo que desea mejorar: "))
                if eleccion == 1:
                    cantidad = int(input("Ingrese la cantidad de espacios de gallinas que desea: "))
                    costo = cantidad * 65
                    if costo <= dinero:
                        global dinero
                        dinero -= costo
                        self.gallinas += cantidad
                        print("Felicidades, mejora exitosa\nDinero:", dinero, "\nGallinas y espacios actuales:", self.gallinas)
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 2:
                    cantidad = int(input("Ingrese la cantidad de espacios de ovejas que desea: "))
                    costo = cantidad * 85
                    if costo <= dinero:
                        global dinero
                        dinero -= costo
                        self.ovejas += cantidad
                        print("Felicidades, mejora exitosa\nDinero:", dinero, "\nOvejas y espacios actuales:", self.ovejas)
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 3:
                    cantidad = int(input("Ingrese la cantidad de espacios de vacas que desea: "))
                    costo = cantidad * 100
                    if costo <= dinero:
                        global dinero
                        dinero -= costo
                        self.vacas += cantidad
                        print("Felicidades, mejora exitosa\nDinero:", dinero, "\nVacas y espacios actuales:", self.vacas)
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 0:
                    print("Vuelva pronto")
                    break
                else:
                    print("Opción no válida, ingrese una opción válida.")
        elif opcion == 2:
            print("Vuelva pronto")
        else:
            print("Opción no válida")

# Ejemplo de uso de la clase Granja
mi_granja = Granja()
mi_granja.vender_suministros()