import time

class TiempoEnJuego:
    def __init__(self):
        self.tiempo_en_juego_minutos = 0
        self.duracion_del_dia_en_juego_minutos = 24 * 60  # Un día equivale a 24 horas * 60 minutos

    def avanzar_tiempo(self):
        while self.tiempo_en_juego_minutos < self.duracion_del_dia_en_juego_minutos:
            self.mostrar_tiempo_actual()
            self.tiempo_en_juego_minutos += 1
            time.sleep(1)  # Avanza el tiempo en el juego 1 minuto cada segundo real

    def mostrar_tiempo_actual(self):
        horas = self.tiempo_en_juego_minutos // 60
        minutos = self.tiempo_en_juego_minutos % 60
        print(f'Tiempo en el juego: {horas:02d}:{minutos:02d}')


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def planificar_actividades(self, tiempo_en_juego):
        while True:
            print("\n¿Qué quieres hacer ahora?")
            print("1. Trabajar en el campo")
            print("2. Cuidar a los animales")
            print("3. Descansar")
            print("4. Salir del juego")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                print(f"{self.nombre} está trabajando en el campo...")
                # Simula el trabajo en el campo (puedes agregar tu lógica aquí)
            elif opcion == '2':
                print(f"{self.nombre} está cuidando a los animales...")
                # Simula el cuidado de los animales (puedes agregar tu lógica aquí)
            elif opcion == '3':
                print(f"{self.nombre} está descansando...")
                # Simula el descanso (puedes agregar tu lógica aquí)
            elif opcion == '4':
                print(f"{self.nombre} ha salido del juego.")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    tiempo = TiempoEnJuego()
    jugador = Jugador("Juan")  # Cambia el nombre del jugador según lo necesites

    print("¡Bienvenido a Farm Life Simulator!")
    tiempo.avanzar_tiempo()  # Iniciar el tiempo en el juego
    jugador.planificar_actividades(tiempo)
