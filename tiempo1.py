import time

class FarmLifeSimulator:
    def __init__(self):
        self.tiempo_en_juego_minutos = 0
        self.duracion_del_dia_en_juego_minutos = 24 * 60  # Un día equivale a 24 horas * 60 minutos

    def avanzar_tiempo(self, minutos_avance=1):
        while self.tiempo_en_juego_minutos < self.duracion_del_dia_en_juego_minutos:
            hora_actual = self.tiempo_en_juego_minutos // 60
            minutos_actuales = self.tiempo_en_juego_minutos % 60

            # Mostrar la hora actual en pantalla
            print(f'Hora en el juego: {hora_actual:02d}:{minutos_actuales:02d}')

            # Puedes agregar aquí la lógica para que los jugadores interactúen con el mundo del juego

            # Avanzar el tiempo en el juego
            self.tiempo_en_juego_minutos += minutos_avance
            time.sleep(1)  # Simula que un minuto del juego equivale a 1 segundo real

if __name__ == "__main__":
    juego = FarmLifeSimulator()
    juego.avanzar_tiempo()
