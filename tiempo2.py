import time

class FarmTime:
    def __init__(self):
        self.tiempo_en_juego_minutos = 0
        self.duracion_del_dia_en_juego_minutos = 24 * 60  
        self.actividades_programadas = {}

    def avanzar_tiempo(self, minutos_a_avanzar=1):
        self.tiempo_en_juego_minutos += minutos_a_avanzar
        self.tiempo_en_juego_minutos %= self.duracion_del_dia_en_juego_minutos

    def mostrar_tiempo(self):
        horas = self.tiempo_en_juego_minutos // 60
        minutos = self.tiempo_en_juego_minutos % 60
        return f"{horas:02d}:{minutos:02d}"

    def programar_actividad(self, hora, actividad):
        self.actividades_programadas[hora] = actividad

    def obtener_actividad_programada(self):
        hora_actual = self.tiempo_en_juego_minutos // 60
        return self.actividades_programadas.get(hora_actual, "Nada programado")

if __name__ == "__main__":
    juego = FarmTime()

    # Programar actividades
    juego.programar_actividad(7, "Desayunar")
    juego.programar_actividad(8, "Cuidar a los animales")
    juego.programar_actividad(12, "Almorzar")
    juego.programar_actividad(18, "Regar las plantas")
    juego.programar_actividad(22, "Ir a dormir")

    while True:
        print(f'Tiempo en el juego: {juego.mostrar_tiempo()}')
        actividad_programada = juego.obtener_actividad_programada()
        print(f"Actividad programada: {actividad_programada}")
        juego.avanzar_tiempo()
        time.sleep(60)  # Avanza el tiempo en el juego 1 minuto cada minuto real
