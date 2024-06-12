"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Bank:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.value = 0
  
  def deposit(self, value):
    if value > 0:
      self.value += value
  
  def withdraw(self, value):
    if self.value - value > 0:
      self.value -= value
    else:
      print("Saldo insuficiente!")

b = Bank('1', 'Joe')
b.deposit(150)
b.withdraw(170)