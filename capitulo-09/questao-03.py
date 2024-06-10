"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def arrayParImpar():
  numbers = [1,2,3,5,9,12,15,22,30,35,38,40,42]
  pair = []
  odd = []
  for number in numbers:
    if (number % 2) == 0:
      pair.append(number)
    else:
      odd.append(number)
  return pair, odd

print(arrayParImpar())