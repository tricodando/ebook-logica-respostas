"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

import datetime

class Bank:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.value = 0
    self.history = []
  
  def deposit(self, value):
    if value > 0:
      self.value += value
      self.log(f"R$ {value} foi depositado em: {datetime.datetime.today()}")
  
  def withdraw(self, value):
    if self.value - value > 0:
      self.value -= value
      self.log(f"R$ {value} foi sacado em: {datetime.datetime.today()}")
    else:
      print("Saldo insuficiente!")

  def log(self, txt):
    self.history.append(txt)
  
  def extract(self):
    for line in self.history:
      print(line)

b = Bank('1', 'Joe')
b.deposit(50)
b.deposit(50)
b.withdraw(20)
b.withdraw(20)
b.extract()