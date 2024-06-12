"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Class:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades
  
  def average(self):
    total = 0
    for nota in self.grades:
      total += nota
    avg = total / len(self.grades)
    return avg

d = Class('mat', [7,7,7])
print(d.average())