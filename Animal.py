# salud
# hambre
# felicidad
# produccion
TIPOS = ["Vaca", "Gallina", "Oveja"]



class Animal:
    def __init__(self, id, nombre, especie) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__especie = especie
        self.__felicidad = 25
        self.__hambre = 50
        self.__salud = 100
        self.__estado = "Bien"

    def get_nombre(self):
        return self.__nombre

    def limpiar(self):
        self.__felicidad += 5
        self.__salud += 5

    def acariciar(self):
        self.__felicidad += 5

    def comer(self, cantidad):
        self.__felicidad += 3
        self.__hambre += cantidad

    def entristecer(self):
        self.__felicidad -= 5

    def tener_hambre(self):
        self.__hambre -= 10

    def enfermar(self):
        self.__salud -= 15

    def sanar(self, medicina):
        self.__salud += medicina

    def recolectar(self):
        pass

    def ver_salud(self):
        return self.__salud
   
    def ver_estado(self):
        return self.__str__() + f"\nSalud: {self.__salud}\nFelicidad: {self.__felicidad}\nHambre: {self.__hambre}"

    def __str__(self) -> str:
       return f"{self.__id}. {self.__especie.title()}\nNombre: {self.__nombre}"

class Vaca(Animal):
    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre, "vaca")
        self.producto = " lt(s) de leche"
        self.__tiempo_espera = 0 

    def recolectar(self):
        return 1
    
class Gallina(Animal):
    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre, "gallina")
        self.producto = "huevo(s)"

    def recolectar(self):
        return 2

class Oveja(Animal):
    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre, "oveja")
        self.producto = "rollo(s) de lana"

    def recolectar(self):
        return 3 
    
class Alimento():
    def __init__(self, valor) -> None:
        self.valor = valor
class Medicina():
    def __init__(self, valor) -> None:
        self.valor = valor

class Establo():
    def __init__(self, size) -> None:
        self._size = size
        self.animales = []

    def aumentar_espacio(self, espacio):
        self._size += espacio
    
    def espacio_disponible(self):
        return self._size - len(self.animales)

animales:list[Animal] = []

def actualizar():
    for animal in animales:
        animal.tener_hambre()
        animal.entristecer()
        animal.enfermar()

def alimentar(animal, alimento = 20):
    animal.comer(alimento)

def dar_medicina(animal, medicina = 15):
    animal.sanar(medicina)

def recolectar(animal:Animal):
    #If la salud del animal es buena recolectar
    # sino una advertencia
    if animal.ver_salud() > 8:
        return f"{animal.recolectar()} {animal.producto}" 
    else:
        return f"{animal.get_nombre()} no está bien de salud"
    
alimentos = [4, 5, 6]
medicinas = []

def ver_vacas():
    return [x for x in animales if type(x) == Vaca]
def ver_gallinas():
    return [x for x in animales if type(x) == Gallina]
def ver_ovejas():
    return [x for x in animales if type(x) == Oveja]

def nuevo_animal(tipo):
    print(f"Creando: {TIPOS[tipo-1]}")
    id = len(animales)+1
    nombre = input("Nombre: ")
    animal = None
    match tipo:
        case 1:
            animal = Vaca(id, nombre)
        case 2:
            animal = Gallina(id, nombre)
        case 3:
            animal = Oveja(id, nombre)
    animales.append(animal)
    return animal
    
def crear_vaca():
    return nuevo_animal(1)
def crear_gallina():
    return nuevo_animal(2)
def crear_oveja():
    return nuevo_animal(3)

# Menus para interactuar
# Menu para cuidar de los animales
def cuidar(animal:Animal):
    while True:
        print(
        # Opciones
        "1. Acariciar\n",
        "2. Alimentar\n",
        "3. Dar Medicina\n",
        "4. Limpiar\n",
        "5. Terminar\n",
        )
        opcion = input(f"Como desea cuidar a {animal.get_nombre()}: ")
        match opcion:
            # Opciones
            case "1":
                animal.acariciar()
            case "2":
                alimentar(animal)
                # for alimento in alimentos:
                #     print(f"{alimentos.index(alimento)+1}, {alimento}")
                # opcion = input("Seleccione la canidad a alimentar: ")
                # if opcion.isdigit():
                #     opcion = int(opcion)
                # else:
                #     print("Por favor vuelva a intentarlo")
                # if opcion < len(alimentos) and opcion>0:
                #     alimentar(animal, alimentos[opcion+1].valor)
                # else:
                #     print("Por favor vuelva a intentarlo")
            case "3":
                dar_medicina(animal)
                # for medicina in medicinas:
                #     print(f"{medicinas.index(medicina)+1}, {medicina.valor}")
                # opcion = input("Seleccione la canidad a medicar: ")
                # if opcion.isdigit():
                #     opcion = int(opcion)
                # else:
                #     print("Por favor vuelva a intentarlo")
                # if opcion < len(medicinas) and opcion>0:
                #     dar_medicina(animal,medicinas[opcion+1])
                # else:
                #     print("Por favor vuelva a intentarlo")
            case "4":
                animal.limpiar()
            case "5":
                return
            case _:
                print("Opcion no reconocida")
        input()

def seleccionar_animal():
    while True:
        codigo = input("Ingrese el numero del animal: ")
        codigo = int(codigo) if codigo.isnumeric() else -1
        if codigo <= len(animales) and codigo>0 :
            return animales[codigo-1]
        else:
            print("Codigo no reconocido, verifique utilizar numeros")

def crear_animal():
    while True:
        print(
        # Opciones
        "1. Vaca\n" +
        "2. Gallina\n" +
        "3. Oveja\n" +
        ""
        )
        opcion = input("Seleccione el animal a crear: ")
        match opcion:
            # Opciones
            case "1":
                return crear_vaca()
            case "2":
                return crear_gallina()
            case "3":
                return crear_oveja()
            case _:
                print("Opcion no reconocida")

# Menu para visualizar
# Este es el metodo a ejecutar para poder interactuar con los animales
def entrar():
    while True:
        print(
        # Opciones
        "1. Ver todos los animales\n" +
        "2. Ver todos los animales con salud\n" +
        "3. Seleccionar animales\n" +
        "4. Agregar animales\n" +
        "0. Regresar\n"
        )
        opcion = input("Ingrese la opcion a realizar: ")
        match opcion:
            # Opciones
            case "1":
                for animal in animales:
                    print(animal)
            case "2":
                for animal in animales:
                    print(animal.ver_estado())
            case "3":
                if len(animales) > 0:
                    animal = seleccionar_animal()
                    cuidar(animal)
                    print(animal.ver_estado())
                else:
                    print("Aun no tiene animales para seleccionar")
            case "4":
                crear_animal()
            case "0":
                return
            case _:
                print("Opcion no reconocida, vuelva a intentarlo")
        input()

# Inicialización de la variable dinero
dinero = 500

class Granja:
    def __init__(self):
        # Inicialización de las variables de la granja
        self.gallinas = []
        self.ovejas = []
        self.vacas = []
        self.comida_gallina = 1
        self.comida_vaca = 1
        self.comida_ovejas = 1
        self.huevos = 1
        self.lana = 1
        self.leche_litro = 1
        # Almacena la variable global dinero en una variable de instancia
        self.dinero = dinero

    # Función para mostrar la cantidad de dinero
    def mostrar_dinero(self):
        print("Dinero:", self.dinero)

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
                    self.dinero += ganancia
                    self.huevos -= cantidad
                    print("Lo gastado fue: ", ganancia)
                    print("Felicidades, venta exitosa\nDinero:", self.dinero)
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 2:
                cantidad = int(input("Ingrese la cantidad de litros que desea de leche: "))
                if cantidad > 0 and cantidad <= self.leche_litro:
                    ganancia = cantidad * 14
                    self.dinero += ganancia
                    self.leche_litro -= cantidad
                    print("Lo gastado fue: ", ganancia)
                    print("Felicidades, venta exitosa\nDinero:", self.dinero)
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 3:
                cantidad = int(input("Ingrese la cantidad de rollos de lana que desea: "))
                if cantidad > 0 and cantidad <= self.lana:
                    ganancia = cantidad * 8
                    self.dinero += ganancia
                    self.lana -= cantidad
                    print("Lo gastado fue: ", ganancia)
                    print("Felicidades, venta exitosa\nDinero:", self.dinero)
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
                    if costo <= self.dinero:
                        self.dinero -= costo
                        self.comida_ovejas += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, compra exitosa\nDinero:", self.dinero)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")
            elif opcion == 2:
                cantidad = int(input("Ingrese la cantidad de bolsas de comida para vaca que desea: "))
                if cantidad > 0:
                    costo = cantidad * 50
                    if costo <= self.dinero:
                        self.dinero -= costo
                        self.comida_vaca += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, compra exitosa\nDinero:", self.dinero)
                    else:
                        print("Moneda insuficiente, siga produciendo para hacer la compra")
                else:
                    print("La cantidad debe ser mayor que 0")
            elif opcion == 3:
                cantidad = int(input("Ingrese la cantidad de bolsas de comida para gallinas que desea: "))
                if cantidad > 0:
                    costo = cantidad * 50
                    if costo <= self.dinero:
                        self.dinero -= costo
                        self.comida_gallina += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, compra exitosa\nDinero:", self.dinero)
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
                    if costo <= self.dinero:
                        self.dinero -= costo
                        self.gallinas += cantidad
                        print("Lo gastado fue:", costo)
                        print("Felicidades, mejora exitosa\nDinero:", self.dinero, "\nGallinas y espacios actuales:", self.gallinas)
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 2:
                    cantidad = int(input("Ingrese la cantidad de espacios de ovejas que desea: "))
                    costo = cantidad * 85
                    if costo <= self.dinero:
                        self.dinero -= costo
                        self.ovejas += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, mejora exitosa\nDinero:", self.dinero, "\nOvejas y espacios actuales:", self.ovejas)
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 3:
                    cantidad = int(input("Ingrese la cantidad de espacios de vacas que desea: "))
                    costo = cantidad * 100
                    if costo <= self.dinero:
                        self.dinero -= costo
                        self.vacas += cantidad
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, mejora exitosa\nDinero:", self.dinero, "\nVacas y espacios actuales:", self.vacas)
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


entrar()