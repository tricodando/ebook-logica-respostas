"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Person:
  def __init__(self, firstName, lastName, birthDate):
    self.firstName = firstName
    self.lastName = lastName
    self.birthDate = birthDate
  
  def fullName(self):
    return f"{self.firstName} {self.lastName}"

person = Person("Fulano", "de Tal", "01-01-2024")
print(person.fullName())