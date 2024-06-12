"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Engine:
  def __init__(self):
    self.engine = False

  def start(self):
    self.engine = True
    print("Motor ligado")

  def stop(self):
    self.engine = False
    print("Motor desligado")

class Car:
  def __init__(self, model, color, ports, fuel):
    self.model = model
    self.color = color
    self.ports = ports
    self.fuel = fuel
    self.km_l = 5
    self.engine = Engine()
  
  def calculate(self, distanceInKm):
    l = distanceInKm / self.km_l
    if l < self.fuel:
      return True
    else:
      return False

car = Car("Bugatti-Veyron", "black", 2, 100)
print(car.calculate(400))