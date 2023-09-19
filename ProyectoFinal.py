#Cultivo y cosechas
cultivos_disponibles = ['Fresa','Pepino','Naranja','Tomate','Zanahorias']

class Cultivo():
  def __init__(self,nombre):
    self.nombre = nombre
    self.riegos = 0
    self.etapa = 1

  def crecimiento(self):
    if self.etapa < 3:
      self.etapa += 1
  
  def maduracion(self):
    return self.etapa == 3

  def mostrar_cultivo(self):
    print(f'Nombre del cultivo:{self.nombre} Etapa de crecimiento:',self.etapa)
  
class Granja():
  def __init__(self):
    self.cultivos_disponibles = []

  def sembrar(self):
    b = 0
    for a in cultivos_disponibles:
      b = b + 1
      print(f'{b}{a}')
    cultivoSelect = input('Seleccione que cultivo desea sembrar: ')
    newCultivo = cultivos_disponibles[int(cultivoSelect)-1]
    newSembrado = Cultivo(newCultivo)
    self.cultivos_disponibles.append(newSembrado)
  def mostrar_cultivo(self):
    for c in self.cultivos_disponibles:
      c.mostrar_cultivo()


granga1 = Granja()
granga1.sembrar()
granga1.sembrar()
granga1.sembrar()
granga1.mostrar_cultivo()
      