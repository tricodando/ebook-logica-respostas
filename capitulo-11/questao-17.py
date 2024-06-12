"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Car:
  def __init__(self, model, color, ports, fuel, engine):
    self.model = model
    self.color = color
    self.ports = ports
    self.fuel = fuel
    self.engine = engine
  
  def start(self):
    self.engine = True
    print("Motor ligado")

  def stop(self):
    self.engine = False
    print("Motor desligado")

car = Car("Bugatti-Veyron", "black", 2, 100, False)
car.start()