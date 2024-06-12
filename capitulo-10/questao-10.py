"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

myList = [1,2,3,4,5]

try:
  print(myList[5])
except:
  raise IndexError("Índice inválido!")