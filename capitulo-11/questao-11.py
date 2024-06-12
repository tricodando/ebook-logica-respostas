"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class RH:
  def __init__(self):
    self.employees = []
  
  def hiredIn(self, data):
    self.employees.append(data)

rh = RH()
rh.hiredIn({
      "name": "Joe",
      "office": "Dev",
      "date": "01-01-2024",
      "salary": 3500,
      "status": True
    })
print(rh.employees)