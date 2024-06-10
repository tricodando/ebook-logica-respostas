"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

from math import pi

def circleRadius(radius):
  return pi * (radius * radius)

radius = float(input("Informe o raio: "))

print(circleRadius(radius))