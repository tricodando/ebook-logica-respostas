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

person = Person("Joe", "Doe", "01-02-2020")