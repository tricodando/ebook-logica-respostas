"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Character:
  def __init__(self, id, x, y):
    self.__id = id
    self.__x = x
    self.__y = y
  
  @property
  def id(self):
    return self.__id
  
  @property
  def x(self):
    return self.__x
  
  @property
  def y(self):
    return self.__y

c = Character(1,2,3)
print(c.id)
print(c.x)
print(c.y)