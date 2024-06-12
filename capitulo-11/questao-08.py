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

  def status(self):
    avg = self.average()
    if avg < 5:
      print("Reprovado")
    elif avg >= 5 and avg < 7:
      print("Recuperação")
    elif avg >= 7:
      print("Aprovado")

d = Class('mat', [7,7,7])
print(d.average())
d.status()

d = Class('mat', [4,5,6])
print(d.average())
d.status()

d = Class('mat', [3,2,0])
print(d.average())
d.status()