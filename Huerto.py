import random

#Cultivo y cosechas
cultivos_disponibles = ['Fresa','Pepino','Naranja','Tomate','Zanahorias']

class Cultivo:
  def __init__(self,nombre):
    self.nombre = nombre
    self.cosechados = False
    self.riegos = 0
    self.etapa = 0

  def crecimiento(self):
    if self.etapa < 3 and self.riegos==3:
      self.etapa += 1
      self.riegos = 0
      print('Felicidades hay un cultivo que ha aumentado una etapa!')
    elif self.riegos < 3:
      self.riegos += 1
      if self.etapa == 1 or self.etapa == 0:
        print(f'Nombre del cultivo: {self.nombre}\nEtapa: Brote\n')
      elif self.etapa == 2: 
        print(f'Nombre del cultivo: {self.nombre}\nEtapa: Crecimiento\n')
      else:
        print(f'Nombre del cultivo: {self.nombre}\nEtapa: Cosecha\n')

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

  def plaga(self):
    if self.etapa > 0:
      self.etapa = self.etapa - 1

  def mostrar(self):
    print(f'Nombre: {self.nombre} - Etapa: {self.etapa}')

class Huerto:
  def __init__(self) -> None:
#variable que almacena los cultivos que hay sembrados
    self.cultivos_sembrados = [[],[],[],[],[]]
#variable que almacena los cultivos que hay cultivados
    self.cultivos_cosechados = [[],[],[],[],[]]
#variable que se encarga de ver el espacio de siembra
    self.campos = 6
#fertilizantes disponibles
    self.fertilizante_disponibles = 2
#insectisidas
    self.insecticidas = 1
#semillas disponibles 
    self.semillas = 6

#funcion que nos ayuda a cosechar recibe el arreglo de todos los cultivos sembrados y el nombre del cultivo que se desea cosechar
  def cosechar(self,cultivos_d,nombre):
    #ciclo que se encarga de buscar en los cultivos todos los que tengan un etapa 3(cosecha) para poder ser cosechados
    for fila in range(len(cultivos_d)):
      for columna in range(len(cultivos_d[fila])):
        if cultivos_d[fila][columna].nombre == nombre and cultivos_d[fila][columna].etapa == 3:
          cultivos_d[fila][columna].cosechados = True
          cosechado = cultivos_d[fila][columna]
          self.cultivos_cosechados[fila].append(cosechado)
        #este ciclo se encarga de eliminar de los cultivos que estan sembrados los que cosechamos para que no se repitan
        for a in reversed(cultivos_d):
          for b in reversed(a):
            if b.cosechados == True:
              cultivos_d[cultivos_d.index(a)].pop(cultivos_d[cultivos_d.index(a)].index(b))
    print(f'{nombre}s fueron cosechadas correctamente!\n')
    return cultivos_d

  #funcion que ejecuta las opciones que tiene el usuario en el modo sembrar.Recibe dos parametros fertilizantes y semillas 
  def granjaCosechar(self,fertilizantes, semillas,cultivos,insecticidas):
    while True:
      action = input('Que deseas hacer en la granja?\n1.Sembrar\n2.Regar\n3.Fertilizar el suelo\n4.Cosechar\n5.Ver mis cultivos\n6.Ver mis cosechas\n7.Salir\n')
      match(action):
        case '1':
          while True:
            if semillas > 0:
              b = 0
              print('\n')
              print('0.Cancelar')
              for a in cultivos_disponibles:
                b = b + 1
                print(f'{b}.{a}')

              #cantidad de cultivos que hay sembrados
              contador = 0
              for fila in self.cultivos_sembrados:
                  for valor in fila:
                      contador += 1

              cultivoSelect = input('Seleccione que cultivo desea sembrar: \n')
              #verifica si se ingresaron bien los datos
              if int(cultivoSelect) > len(cultivos_disponibles):
                print('Selecciono un cultivo fuera del rango de la lista!')
              elif int(cultivoSelect) <= len(cultivos_disponibles) and  int(cultivoSelect) > 0 :
                if contador <= self.campos:
                  newCultivo = cultivos_disponibles[int(cultivoSelect)-1]
                  newSembrado = Cultivo(newCultivo)
                  match(cultivoSelect):
                    case '1':
                      self.cultivos_sembrados[0].append(newSembrado)
                    case '2':
                      self.cultivos_sembrados[1].append(newSembrado)
                    case '3':
                      self.cultivos_sembrados[2].append(newSembrado)
                    case '4':
                      self.cultivos_sembrados[3].append(newSembrado)
                    case '5':
                      self.cultivos_sembrados[4].append(newSembrado)
                  semillas = semillas -1
                  print('El cultivo fue sembrado correctamente!')
                  salir = input('Desea sembrar otro cultivo ? \n1.Si\n2.No\n')
                  if salir =='2':
                    break
                else:
                  print('Ya no tiene espacios dentro del campo para sembrar!\nTienes que mejorar el campo en la tienda!')
                  break
              elif int(cultivoSelect) == 0:
                break
              else: 
                print('Selecciono un cultivo fuera del rango de la lista!')
            else:
              print('Ya no cuenta con semillas disponibles para seguir sembrando!')
              break
        case '2':
          numero_aleatorio = random.randint(1, 8)
          while True:
            cultivosSembrados = len(self.cultivos_sembrados[0]) + len(self.cultivos_sembrados[1])+len(self.cultivos_sembrados[2]) + len(self.cultivos_sembrados[3])+len(self.cultivos_sembrados[4])
            if cultivosSembrados == 0:
              print('No hay cultivos sembrados aun!')
              break
            else:
              if numero_aleatorio == 3 and insecticidas > 0:
                insecticidas = insecticidas - 1
                print(f'Una plaga ha afectado a tus cultivos!\nUsaste un insecticida para prevenir la plaga en tus cultivos\nTe restan {insecticidas}')
              elif numero_aleatorio == 3 and insecticidas == 0:
                for siembra in self.cultivos_sembrados:
                  for fruta in siembra:
                    fruta.plaga()
                print('Oh no!\nTus cultivos tienen plaga\nEL nivel de tus plantas fue consumido!')
              else:
                for siembra in self.cultivos_sembrados:
                  for fruta in siembra:
                    fruta.crecimiento()
                print('Los cultivos fueron regados correctamente!')
              break
        case '3':
          if len(self.cultivos_sembrados) > 0:
            if fertilizantes > 0 :
              for i in self.cultivos_sembrados:
                for a in i:
                  a.cultivo_fertilizado()
              fertilizantes = fertilizantes - 1
              print('Felicidades tus cultivos han aumentado una etapa!')
            else:
              print('Ya no cuentas con fertilizantes!\nDirigete a la tienda para poder adquirir mas!')
          else:
            print('No hay cultivos sembrados para poder fertilizar el campo!')

        case '4':
          #vector que se encarga de verificar de almacenar el nombre de la siembra y la cantidad de estos sembrados
          cultivos_Cosechables = [['Fresa',0],['Pepino',0],['Naranja',0],['Tomate',0],['Zanahorias',0]]
          #ciclo que se encarga de buscar todos los cultivos que ya tengan una etapa de crecimiento 3
          for cultivo in self.cultivos_sembrados:
            for cosecha in cultivo:
              if cosecha.etapa == 3:
                match(cosecha.nombre):
                  case 'Fresa':
                    cultivos_Cosechables[0][1] +=1
                  case 'Pepino':
                    cultivos_Cosechables[1][1] +=1
                  case 'Naranja':
                    cultivos_Cosechables[2][1] +=1
                  case 'Tomate':
                    cultivos_Cosechables[3][1] +=1
                  case 'Zanahorias':
                    cultivos_Cosechables[4][1] +=1

          #variable encargada de verificar si hay cultivos que se puedan cosechar
          cantidad_cosechables = cultivos_Cosechables[0][1] +cultivos_Cosechables[1][1] + cultivos_Cosechables[2][1] + cultivos_Cosechables[3][1] + cultivos_Cosechables[4][1] 

          if cantidad_cosechables == 0:
            print('No hay cultivos que se puedan cultivar aun!')
          #ciclo que se encarga de cosechar los cultivos
          else:
            print('Estos son los productos que pueden ser cosechados:')
            contador = 0 
            #ciclo que solo se encarga de imprimir datos
            for tipo in cultivos_Cosechables:
              contador += 1
              print(f'{contador}.Nombre: {tipo[0]} cantidad: {tipo[1]}') 
            seleccion = input('Escoja un cultivo: ')
            match(seleccion):
              case '1':
                #verifica que hayan cultivos cosechados
                if cultivos_Cosechables[0][1] == 0:
                  print('No hay ninguna siembra que pueda ser cosechada aun!')
                else:
                  for fila in range(len(cultivos)):
                    for columna in range(len(cultivos[fila])):
                      if cultivos[fila][columna].nombre == 'Fresa' and cultivos[fila][columna].etapa == 3:
                        cultivos[fila][columna].cosechados = True
                        cosechado = cultivos[fila][columna]
                        self.cultivos_cosechados[fila].append(cosechado)

                  #este ciclo se encarga de eliminar de los cultivos que estan sembrados los que cosechamos para que no se repitan
                  for a in reversed(cultivos):
                    for b in reversed(a):
                      if b.cosechados == True:
                        cultivos[cultivos.index(a)].pop(cultivos[cultivos.index(a)].index(b))
                  print('Fresas fueron cosechadas correctamente!')
              case '2':
                #verifica que hayan cultivos cosechados
                if cultivos_Cosechables[1][1] == 0:
                  print('No hay ninguna siembra que pueda ser cosechada aun!')
                else:
                  cultivos = self.cosechar(cultivos,'Pepino')
                  cultivos
              case '3':
                #verifica que hayan cultivos cosechados
                if cultivos_Cosechables[2][1] == 0:
                  print('No hay ninguna siembra que pueda ser cosechada aun!')
                else:
                  cultivos = self.cosechar(cultivos,'Naranja')
                  cultivos
              case '4':
                #verifica que hayan cultivos cosechados
                if cultivos_Cosechables[3][1] == 0:
                  print('No hay ninguna siembra que pueda ser cosechada aun!')
                else:
                  cultivos = self.cosechar(cultivos,'Tomate')
                  cultivos
              case '5':
                #verifica que hayan cultivos cosechados
                if cultivos_Cosechables[4][1] == 0:
                  print('No hay ninguna siembra que pueda ser cosechada aun!')
                else: 
                  cultivos = self.cosechar(cultivos,'Zanahorias')
                  cultivos
              
        case '5':
          cultivosSembrados = len(self.cultivos_sembrados[0]) + len(self.cultivos_sembrados[1])+len(self.cultivos_sembrados[2]) + len(self.cultivos_sembrados[3])+len(self.cultivos_sembrados[4])
          if cultivosSembrados == 0:
            print('Aun no hay cultivos sembrados!')
          else:
            for siembra in cultivos:
              for cosecha in siembra:
                cosecha.mostrar()
        case '6':
          cultivosCosechados = len(self.cultivos_cosechados[0]) + len(self.cultivos_cosechados[1])+len(self.cultivos_cosechados[2]) + len(self.cultivos_cosechados[3])+len(self.cultivos_cosechados[4])
          if cultivosCosechados == 0:
            print('No hay cultivos cosechados!')
          else:
            for tipo in self.cultivos_cosechados:
              if len(tipo)>0:
                print(f'Cosecha:{tipo[0].nombre} - cantidad:{len(tipo)}')
        case '7':
          break
        case _:
          print('Selecciono una opcion fuera del rango de la lista!')

    #de volvemos las mismas variables pero con un valor actualizado o el mismo con el que ingresaron si no fueron usadas
    return fertilizantes,semillas,cultivos,insecticidas

  def enfermar(self):
    for cultivo in self.cultivos_sembrados:
      cultivo.plaga()

  def ver(self):
    return self.granjaCosechar(self.fertilizante_disponibles, self.semillas, self.cultivos_sembrados, self.insecticidas)
    
#asignamos a las variables globales el valor que retorna la funcion que es el estado actual si fueron usadas
#fertilizante_disponibles,semillas, self.cultivos_sembrados,insecticidas = granjaCosechar(fertilizante_disponibles,semillas, self.cultivos_sembrados, insecticidas)

#ejecutamos la funcion
#fertilizante_disponibles,semillas,cultivos_sembrados

