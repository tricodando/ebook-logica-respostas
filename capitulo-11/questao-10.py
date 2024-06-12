"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width
  
  def area(self):
    return self.height * self.width

  def perimetro(self):
    return self.height*2 + self.width*2

r = Rectangle(5,10)
print(r.perimetro())