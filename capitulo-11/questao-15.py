"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Sum:
  def execute(self, a, b):
    return a + b

class Calculator:
  def __init__(self):
    self.soma = Sum()
  
c = Calculator()
result1 = c.soma.execute(0,0)
result2 = c.soma.execute(7,3)
result3 = c.soma.execute(-5,2)
result4 = c.soma.execute(7,0.9)
print(result1)
print(result2)
print(result3)
print(result4)