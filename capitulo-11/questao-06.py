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

class Player(Character):
  def __init__(self, id, x, y, nick, power, life):
    super().__init__(id, x, y)
    self.nick = nick
    self.power = power
    self.life = life
  
  def jump(self):
    return "Jumping"
  
  def attack(self):
    return "Attacking"

player = Player(1, 2, 3, "Hero", 10, 100)
print(player.id)