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

  def config(self, percent):
    for employee in self.employees:
      if employee["status"]:
        old = employee["salary"]
        new = old + (old*percent)
        employee["salary"] = new

rh = RH()
rh.hiredIn({
  "name": "Joe",
  "office": "Dev",
  "date": "01-01-2024",
  "salary": 1000,
  "status": True}
)
rh.hiredIn({
  "name": "Janet",
  "office": "Tester",
  "date": "01-01-2024",
  "salary": 1000,
  "status": False}
)
print(rh.employees)
rh.config(0.1)
print(rh.employees)