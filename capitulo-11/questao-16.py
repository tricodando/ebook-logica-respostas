"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Sum:
  def execute(self, a, b):
    return a + b
  
class Subtractor:
  def execute(self, a, b):
    return a - b
  
class Multiplication:
  def execute(self, a, b):
    return a * b
  
class Division:
  def execute(self, a, b):
    return a / b

class Calculator:
  def __init__(self):
    self.sum = Sum()
    self.subtractor = Subtractor()
    self.multiplication = Multiplication()
    self.division = Division()

c = Calculator()
sum = c.sum.execute(1,2)
sub = c.subtractor.execute(7,3)
mult = c.multiplication.execute(3,3)
div = c.division.execute(10,2)
print(sum)
print(sub)
print(mult)
print(div)