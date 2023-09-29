import time

class FarmLifeSimulator:
    def __init__(self):
        self.tiempo_en_juego_minutos = 0
        self.duracion_del_dia_en_juego_minutos = 24 * 60
        self.actividades_programadas = {
            7: "Desayunar",
            8: "Cuidar a los animales",
            12: "Almorzar",
            18: "Regar las plantas",
            22: "Ir a dormir"
        }

    def avanzar_tiempo(self):
        while self.tiempo_en_juego_minutos < self.duracion_del_dia_en_juego_minutos:
            hora_actual = self.tiempo_en_juego_minutos // 60
            minutos_actuales = self.tiempo_en_juego_minutos % 60

            # Mostrar la hora actual en pantalla
            print(f'Hora en el juego: {hora_actual:02d}:{minutos_actuales:02d}')

            # Verificar si hay una actividad programada para esta hora
            if hora_actual in self.actividades_programadas:
                actividad = self.actividades_programadas[hora_actual]
                print(f"¡Es hora de {actividad}!")

            # Avanzar el tiempo en el juego
            self.tiempo_en_juego_minutos += 1
            time.sleep(1)  # Simula que un minuto del juego equivale a 1 segundo real

if __name__ == "__main__":
    juego = FarmLifeSimulator()
    juego.avanzar_tiempo()
