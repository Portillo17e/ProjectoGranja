import random

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
        self.producto = "litros de leche"
        self.__tiempo_espera = 0 

    def recolectar(self):
        return random.randint(1,5)
    
class Gallina(Animal):
    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre, "gallina")
        self.producto = "huevo(s)"

    def recolectar(self):
        return random.randint(1,3)

class Oveja(Animal):
    def __init__(self, id, nombre) -> None:
        super().__init__(id, nombre, "oveja")
        self.producto = "rollos de lana"

    def recolectar(self):
        return random.randint(2, 6)
    
class Alimento():
    def __init__(self, valor) -> None:
        self.valor = valor
class Medicina():
    def __init__(self, valor) -> None:
        self.valor = valor

#animales:list[Animal] = []
# Inicialización de la variable dinero
dinero = 500

class Establo:
    def __init__(self):
        # Inicialización de las variables de la granja
        self.animales = []
        self.gallinas = []
        self.ovejas = []
        self.vacas = []
        self.comida_gallina = 1
        self.comida_vaca = 1
        self.comida_oveja = 1
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
                print(f"Cuenta con {self.huevos} huevos")
                cantidad = int(input("Ingrese la cantidad que desea vender de Huevos: "))
                if cantidad > 0 and cantidad <= self.huevos:
                    ganancia = cantidad * 4
                    self.dinero += ganancia
                    self.huevos -= cantidad
                    print("Ha obtenido: ", ganancia)
                    print("Felicidades, venta exitosa")
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 2:
                print(f"Cuenta con {self.leche_litro} litros de leche")
                cantidad = int(input("Ingrese la cantidad de litros de leche que desea vender: "))
                if cantidad > 0 and cantidad <= self.leche_litro:
                    ganancia = cantidad * 14
                    self.dinero += ganancia
                    self.leche_litro -= cantidad
                    print("Ha obtenido: ", ganancia)
                    print("Felicidades, venta exitosa")
                else:
                    print("Suministros incompletos o cantidad no válida")

            elif opcion == 3:
                print(f"Cuenta con {self.lana} rollos de lana")
                cantidad = int(input("Ingrese la cantidad de rollos de lana que desea vender: "))
                if cantidad > 0 and cantidad <= self.lana:
                    ganancia = cantidad * 8
                    self.dinero += ganancia
                    self.lana -= cantidad
                    print("Ha obtenido: ", ganancia)
                    print("Felicidades, venta exitosa")
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
            while True:
                print("¿Qué desea mejorar? (Tranquilo, el espacio viene incluido en el precio)\n1-. Aumentar gallinas (65 Monedas c/u)\n2-. Aumentar ovejas (85 Monedas c/u\n3-. Aumentar vacas (100 c/u)\n0-. Regresar")
                eleccion = int(input("Ingrese el número correspondiente a lo que desea mejorar: "))
                if eleccion == 1:
                    cantidad = int(input("Ingrese la cantidad de gallinas que desea: "))
                    costo = cantidad * 65
                    if costo <= self.dinero:
                        self.dinero -= costo
                        
                        gallinas = []
                        for x in range(cantidad):
                            gallina = self.crear_gallina()
                            gallinas.append(gallina)
                            self.animales.append(gallina)

                        print("Lo gastado fue:", costo)
                        print("Felicidades, mejora exitosa\nDinero:", self.dinero, "\nCantidad dr Gallinas y espacios actuales:", len(self.ver_gallinas()))
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 2:
                    cantidad = int(input("Ingrese la cantidad ovejas que desea: "))
                    costo = cantidad * 85
                    if costo <= self.dinero:
                        self.dinero -= costo

                        ovejas = []
                        for x in range(cantidad):
                            oveja = self.crear_oveja()
                            ovejas.append(oveja)
                            self.animales.append(oveja)
                        
                        print("Lo gastado fue: ", costo)
                        print("Felicidades, mejora exitosa\nDinero:", self.dinero, "\nCantidad de Ovejas y espacios actuales:", len(self.ver_ovejas()))
                    else:
                        print("No cuenta con la moneda suficiente para hacer mejoras")
                elif eleccion == 3:
                    cantidad = int(input("Ingrese la cantidad de vacas que desea: "))
                    costo = cantidad * 100
                    if costo <= self.dinero:
                        self.dinero -= costo

                        vacas = []
                        for x in range(cantidad):
                            vaca = self.crear_vaca()
                            vacas.append(vaca)
                            self.animales.append(vaca)

                        print("Lo gastado fue: ", costo)
                        print("Felicidades, mejora exitosa\nDinero:", self.dinero, "\nVacas y espacios actuales:", len(self.ver_vacas()))
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


# Funciones para facilitar la modificacion de atributos en los animales

    def actualizar(self):
        for animal in self.animales:
            animal.tener_hambre()
            animal.entristecer()
            animal.enfermar()

    def alimentar(self, animal, alimento = 20):
        animal.comer(alimento)

    def dar_medicina(self, animal, medicina = 15):
        animal.sanar(medicina)

    def recolectar(self, animal:Animal):
        #If la salud del animal es buena recolectar
        # sino una advertencia
        if animal.ver_salud() > 8:
            return animal.recolectar() 
        else:
            return

# Funciones para mostrar a los animales

    def ver_vacas(self):
        return [x for x in self.animales if type(x) == Vaca]
    def ver_gallinas(self):
        return [x for x in self.animales if type(x) == Gallina]
    def ver_ovejas(self):
        return [x for x in self.animales if type(x) == Oveja]

# Funcion para crear un animal, tipo variable entera para identificar el tipo de animal a crear
    def nuevo_animal(self, tipo):
        print(f"Creando: {TIPOS[tipo-1]}")
        id = len(self.animales)+1
        nombre = input("Nombre: ")
        animal = None
        match tipo:
            case 1:
                animal = Vaca(id, nombre)
            case 2:
                animal = Gallina(id, nombre)
            case 3:
                animal = Oveja(id, nombre)
        #animales.append(animal)
        return animal

# Funciones para crear un animal de tipo especifico        
    def crear_vaca(self):
        return self.nuevo_animal(1)
    def crear_gallina(self):
        return self.nuevo_animal(2)
    def crear_oveja(self):
        return self.nuevo_animal(3)

    # Menus para interactuar
    # Menu para cuidar de los animales
    def cuidar(self, animal:Animal):
        while True:
            print(animal.ver_estado())
            print(
            # Opciones
            "1. Acariciar\n",
            "2. Alimentar\n",
            "3. Dar Medicina\n",
            "4. Limpiar\n",
            "5. Recolectar productos\n",
            "0. Terminar"
            )
            opcion = input(f"Como desea cuidar a {animal.get_nombre()}: ")
            match opcion:
                # Opciones
                case "1":
                    animal.acariciar()
                case "2":
                    tipo =  type(animal)
                    if tipo == Vaca:
                        print(f"Comida disponible: {self.comida_vaca}")
                        print("Recuerda cada alimento le quita 20 puntos de hambre")
                        cantidad = input("Cantidad a alimentar: ")
                        while not cantidad.isnumeric():
                            cantidad = input("Por favor ingrese valores enteros:")
                        cantidad = int(cantidad)
                        if cantidad <= self.comida_vaca and cantidad>=0:
                            self.comida_vaca -= cantidad
                            self.alimentar(animal, 20*cantidad)
                        else:
                            print("No hay suficiente comidad")
                    elif tipo == Gallina:
                        print(f"Comida disponible: {self.comida_gallina}")
                        print("Recuerda cada alimento le quita 5 puntos de hambre")
                        cantidad = input("Cantidad a alimentar: ")
                        while not cantidad.isnumeric():
                            cantidad = input("Por favor ingrese valores enteros:")
                        cantidad = int(cantidad)
                        if cantidad <= self.comida_gallina and cantidad>=0:
                            self.comida_gallina -= cantidad
                            self.alimentar(animal,20*cantidad)
                        else:
                            print("No hay suficiente comidad")
                    elif tipo ==  Oveja:
                        print(f"Comida disponible: {self.comida_oveja}")
                        print("Recuerda cada alimento le quita 20 puntos de hambre")
                        cantidad = input("Cantidad a alimentar: ")
                        while not cantidad.isnumeric():
                            cantidad = input("Por favor ingrese valores enteros:")
                        cantidad = int(cantidad)
                        if cantidad <= self.comida_oveja and cantidad>=0:
                            self.comida_oveja -= cantidad
                            self.alimentar(animal, 20*cantidad)
                        else:
                                print("No hay suficiente comidad")
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
                    self.dar_medicina(animal)
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
                    tipo = type(animal)
                    recolectado = self.recolectar(animal)
                    if tipo == Vaca:
                        if recolectado:
                            self.leche_litro += recolectado
                            #print(f"+{recolectado} litros de leche")
                        #else:
                           #print(f"{animal.get_nombre()} esta mal de salud, cuidala antes de recolectar")
                    elif tipo == Gallina:
                        if recolectado:
                            self.huevos += recolectado
                            #print(f"+{recolectado} huevos")
                        #else:
                            #print(f"{animal.get_nombre()} esta mal de salud, cuidala antes de recolectar")
                    elif tipo == Oveja:
                        if recolectado:
                            self.lana += recolectado
                            #print(f"+{recolectado} rollos de lana")                            
                        #else:
                            #print(f"{animal.get_nombre()} esta mal de salud, cuidala antes de recolectar")
                    if recolectado:
                        print(f"+{recolectado} {animal.producto}")
                    else:
                        print(f"{animal.get_nombre()} esta mal de salud, cuidala antes de recolectar")
                case "0":
                    return
                case _:
                    print("Opcion no reconocida")
            input()

    # Menu para seleccionar un animal en especifico para interactuar
    def seleccionar_animal(self):
        while True:
            codigo = input("Ingrese el numero del animal: ")
            codigo = int(codigo) if codigo.isnumeric() else -1
            if codigo <= len(self.animales) and codigo>0 :
                return self.animales[codigo-1]
            else:
                print("Codigo no reconocido, verifique utilizar numeros")

    # Menu para crear los diversos animales
    def crear_animal(self):
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
                    return self.crear_vaca()
                case "2":
                    return self.crear_gallina()
                case "3":
                    return self.crear_oveja()
                case _:
                    print("Opcion no reconocida")

    # Menu para visualizar
    # Este es el metodo a ejecutar para poder interactuar con los animales
    def entrar(self):
        while True:
            print(
            # Opciones
            "1. Ver todos los animales\n" +
            "2. Ver todos los animales con salud\n" +
            "3. Seleccionar animales\n" +
            "0. Regresar\n"
            )
            opcion = input("Ingrese la opcion a realizar: ")
            match opcion:
                # Opciones
                case "1":
                    for animal in self.animales:
                        print(animal)
                case "2":
                    for animal in self.animales:
                        print(animal.ver_estado())
                case "3":
                    if len(self.animales) > 0:
                        animal = self.seleccionar_animal()
                        self.cuidar(animal)
                        print(animal.ver_estado())
                    else:
                        print("Aun no tiene animales para seleccionar")
                # case "4":
                #     # crear_animal()
                case "0":
                    return
                case _:
                    print("Opcion no reconocida, vuelva a intentarlo")
            input()

establo = Establo()
establo.mejorar()
establo.entrar()
establo.vender_suministros()