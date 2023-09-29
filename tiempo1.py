import time

from Establo import Establo
from Huerto import Huerto
import Sistema_Monetario as Mercado




class FarmLifeSimulator:
    def __init__(self):
        self.tiempo_en_juego_minutos = 360
        self.duracion_del_dia_en_juego_minutos = 24 * 60  # Un día equivale a 24 horas * 60 minutos

        ## Variables del Huerto ##
        # region
        self.huerto = Huerto()
        # endregion

        ## Variables del establo ##
        # region
        self.establo = Establo()
        # endregion

        ## Variables del mercado ##
        #region
        self.dinero = 500
        #endregion

    def avanzar_tiempo(self, minutos_avance=60):
        while self.tiempo_en_juego_minutos < self.duracion_del_dia_en_juego_minutos:
            hora_actual = self.tiempo_en_juego_minutos // 60
            minutos_actuales = self.tiempo_en_juego_minutos % 60

            # Mostrar la hora actual en pantalla
            print(f'{hora_actual:02d}:{minutos_actuales:02d}')

            # Puedes agregar aquí la lógica para que los jugadores interactúen con el mundo del juego
            if hora_actual>6 and hora_actual<20: 

                contador_plaga = 0
                contador_plaga += 1
                if contador_plaga == 6:
                    contador_plaga = 0
                    self.huerto.enfermar()

                print(self.dinero)
                print(
                # Opciones
                "1. Ver cultivos\n" +
                "2. Entrar al establo\n" +
                "3. Ir al mercado\n" +
                "4. Inventario\n" +
                "0. Salir"
                )
                opcion = input("Ingrese la opcion a realizar: ")
                match opcion:
                    # Opciones

                    case "1":
                        self.huerto.ver()
                    case "2":
                        self.establo.entrar()
                    case "3":
                        self.dinero = Mercado.entrar_tienda(self.huerto, 
                        self.establo, self.dinero)
                    case "4":
                        # Ver dinero, semillas, productos cosechados, productos del establo, insecticidas, fertilizantes
                        inventario = ""
                        inventario += f"Dinero: {self.dinero}"
                        inventario +="\nProductos cosechados: "
                        
                        for tipo in self.huerto.  cultivos_cosechados:
                            if len(tipo)>0:
                                inventario += f'\nCosecha:{tipo[0].nombre} - cantidad:{len(tipo)}'
                        inventario += f"\n{self.establo.leche_litro} litros de leche"        
                        inventario += f"\n{self.establo.huevos} huevos"        
                        inventario += f"\n{self.establo.lana} rollos de lana"        
                        inventario +=f"\nSemillas: {self.huerto.semillas}"
                        inventario +=f"\nInsecticidas: {self.huerto.insecticidas}"
                        inventario +=f"\nFertilizante: {self.huerto.fertilizante_disponibles}"
                        print(inventario)
                        input()
                    case "0":
                        return
                    case _:
                        print("Opcion no reconocida")
            else:
                print("Descansando hasta las 7 am")
            self.establo.actualizar()
            # Avanzar el tiempo en el juego
            self.tiempo_en_juego_minutos += minutos_avance
            time.sleep(1)  # Simula que un minuto del juego equivale a 1 segundo real


if __name__ == "__main__":
    juego = FarmLifeSimulator()
    juego.avanzar_tiempo()
