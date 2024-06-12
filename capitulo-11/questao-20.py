"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

class Temperature:
  def __init__(self):
    ...

  def celsius(self, type, temp):
    if type == 'k':
      celsius = temp - 273.15
      return f"{temp:.2f}K -> {celsius:.2f}ºC"
    if type == 'f':
      celsius = (temp - 32) / 1.8
      return f"{temp:.2f}F -> {celsius:.2f}ºC"

  def fahrenheit(self, type, temp):
    if type == 'k':
      fahr = (temp-273.15) * 9/5 + 32
      return f"{temp:.2f}K -> {fahr:.2f}F"
    if type == 'c':
      fahr = (1.8*temp) + 32
      return f"{temp:.2f}C -> {fahr:.2f}F"

  def kelvin(self, type, temp):
    if type == 'c':
      kelvin = temp + 273.15
      return f"{temp:.2f}C -> {kelvin:.2f}K"
    if type == 'f':
      kelvin = (temp-32) * 5/9 + 273.15
      return f"{temp:.2f}F -> {kelvin:.2f}K"
  
t = Temperature()
print(t.kelvin('c', 37))
print(t.kelvin('f', 0))
print(t.celsius('k', 310))
print(t.celsius('f', 95))
print(t.fahrenheit('c', 35))
print(t.fahrenheit('k', 310))