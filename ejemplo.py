import random
import time

# Definición de clases

class Cultivo:
    def __init__(self, nombre, tiempo_crecimiento, valor, estado="siembra"):
        self.nombre = nombre
        self.tiempo_crecimiento = tiempo_crecimiento
        self.valor = valor
        self.estado = estado

class Animal:
    def __init__(self, nombre, salud_max, hambre_max, felicidad_max, produccion):
        self.nombre = nombre
        self.salud = salud_max
        self.hambre = hambre_max
        self.felicidad = felicidad_max
        self.produccion = produccion

# Creación de objetos

maiz = Cultivo("Maíz", 5, 10)
zanahoria = Cultivo("Zanahoria", 4, 8)

vaca = Animal("Vaca", salud_max=100, hambre_max=100, felicidad_max=100, produccion="Leche")
oveja = Animal("Oveja", salud_max=80, hambre_max=80, felicidad_max=100, produccion="Lana")

cultivos_disponibles = [maiz, zanahoria]
animales_disponibles = [vaca, oveja]

# Inicialización del juego

dinero = 100
granja = []

# Funciones

def avanzar_tiempo(dias):
    for _ in range(dias):
        for cultivo in granja:
            if cultivo.estado == "maduro":
                ganancia = cultivo.valor
                print(f"Has cosechado {cultivo.nombre} y ganaste ${ganancia}")
                dinero += ganancia
                granja.remove(cultivo)
            elif cultivo.estado == "crecimiento":
                cultivo.tiempo_crecimiento -= 1
                if cultivo.tiempo_crecimiento == 0:
                    cultivo.estado = "maduro"
                    print(f"{cultivo.nombre} ha madurado.")

def alimentar_animales(animales):
    for animal in animales:
        animal.hambre -= random.randint(5, 15)
        if animal.hambre < 30:
            print(f"{animal.nombre} tiene hambre.")

# Bucle principal del juego

while True:
    print("\n--- Menú ---")
    print("1. Ver estado de la granja")
    print("2. Plantar cultivos")
    print("3. Alimentar animales")
    print("4. Avanzar el tiempo")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n--- Granja ---")
        for cultivo in granja:
            print(f"{cultivo.nombre}: {cultivo.estado}")
        for animal in animales_disponibles:
            print(f"{animal.nombre}: Salud - {animal.salud}, Hambre - {animal.hambre}")
        print(f"Dinero disponible: ${dinero}")
    
    elif opcion == "2":
        print("\n--- Plantar cultivos ---")
        print("Cultivos disponibles:")
        for i, cultivo in enumerate(cultivos_disponibles, 1):
            print(f"{i}. {cultivo.nombre} (Valor: ${cultivo.valor})")
        
        eleccion = int(input("Selecciona un cultivo para plantar: ")) - 1
        if 0 <= eleccion < len(cultivos_disponibles):
            cultivo_elegido = cultivos_disponibles[eleccion]
            if dinero >= cultivo_elegido.valor:
                granja.append(cultivo_elegido)
                dinero -= cultivo_elegido.valor
                print(f"Has plantado {cultivo_elegido.nombre}.")
            else:
                print("No tienes suficiente dinero para plantar este cultivo.")
        else:
            print("Opción inválida.")
    
    elif opcion == "3":
        print("\n--- Alimentar animales ---")
        alimentar_animales(animales_disponibles)
    
    elif opcion == "4":
        print("\n--- Avanzar el tiempo ---")
        dias_avanzar = int(input("Cuántos días deseas avanzar: "))
        avanzar_tiempo(dias_avanzar)
    
    elif opcion == "5":
        print("Gracias por jugar. ¡Hasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

