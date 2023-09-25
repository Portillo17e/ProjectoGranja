#Cultivo y cosechas
cultivos_disponibles = ['Fresa','Pepino','Naranja','Tomate','Zanahorias']

class Cultivo:
  def __init__(self,nombre):
    self.nombre = nombre
    self.riegos = 0
    self.etapa = 0

  def crecimiento(self):
    if self.etapa < 3 and self.riegos==3:
      self.etapa += 1
      self.riegos = 0
      print('Felicidades el cultivo ha aumentado una etapa!')

    elif self.riegos < 3:
      self.riegos += 1
      print('Se rego correctamente el cultivo!')
      if self.etapa == 1 or self.etapa == 0:
        print(f'\nNombre del cultivo: {self.nombre}\nEtapa: Brote\n')
      elif self.etapa == 2: 
        print(f'\nNombre del cultivo: {self.nombre}\nEtapa: Crecimiento\n')
      else:
        print(f'\nNombre del cultivo: {self.nombre}\nEtapa: Cosecha\n')

    elif self.etapa == 3:
      print('El cultivo ya llego al maximo de su crecimiento!\nYa puede ser cosechado')
      print(f'\nNombre del cultivo: {self.nombre} \n Etapa:Cosecha')
  
  def cosecha(self):
    if self.etapa == 3:
      return self.nombre
    else:
      print('El cultivo aun no puede ser cosechado!')

  def cultivo_fertilizado(self):
    if self.etapa < 3:
      self.etapa += 1
    else:
      print('Hay cultivos que ya pueden ser cosechados!!')
  
#variable que almacena los cultivos que hay sembrados
cultivos_sembrados = []
#variable que almacena los cultivos que hay cultivados
cultivos_cosechados = []
#variable que se encarga de ver el espacio de siembra
campos = 6
#fertilizantes 
fertilizantes = 1

def granjaCosechar():
  while True:
    action = input('Que deseas hacer en la granja?\n1.Sembrar\n2.Regar\n3.Fertilizar el suelo\n4.Cosechar\n6.Ver mis cultivos\n5.Salir\n')
    match(action):
      case '1':
        while True:
          b = 0
          print('\n')
          print('0.Cancelar')
          for a in cultivos_disponibles:
            b = b + 1
            print(f'{b}.{a}')

          cultivoSelect = input('Seleccione que cultivo desea sembrar: \n')
          if int(cultivoSelect) > len(cultivos_disponibles):
            print('Selecciono un cultivo fuera del rango de la lista!')
          elif int(cultivoSelect) <= len(cultivos_disponibles) and  int(cultivoSelect) > 0 :
            if len(cultivos_disponibles) <= campos:
              newCultivo = cultivos_disponibles[int(cultivoSelect)-1]
              newSembrado = Cultivo(newCultivo)
              cultivos_sembrados.append(newSembrado)
              print('El cultivo fue sembrado correctamente!')
              salir = input('Desea sembrar otro cultivo ? \n1.Si\n2.No\n')
              if salir =='2':
                break
            else:
              print('Ya no tiene espacios dentro del campo para sembra!\nTiene que mejorar el campo!')
              break
          elif int(cultivoSelect) == 0:
            break
          else: 
            print('Selecciono un cultivo fuera del rango de la lista!')
      case '2':
        while True:
          if len(cultivos_sembrados) == 0:
            print('No hay cultivos sembrados aun!')
            break
          else:
            b = 0
            print('\n')
            print('0.Cancelar')
            for a in cultivos_sembrados:
              b = b + 1
              print(f'{b}.{a.nombre}')
            cultivoSelect = input('Seleccione que cultivo desea sembrar: \n')
            if int(cultivoSelect) > len(cultivos_sembrados):
              print('Selecciono un cultivo fuera del rango de la lista!')
            elif int(cultivoSelect) <= len(cultivos_sembrados) and  int(cultivoSelect) > 0 :
              cultivos_sembrados[int(cultivoSelect)-1].crecimiento()
              salir = input('Desea regar otro cultivo ? \n1.Si\n2.No\n')
              if salir =='2':
                break
            elif int(cultivoSelect) == 0:
              break
            else: 
              print('Selecciono un cultivo fuera del rango de la lista!')

      case '5':
        break

granjaCosechar()