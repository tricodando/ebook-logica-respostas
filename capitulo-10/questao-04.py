"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

import pickle

with open("data.db", "rb") as file:
  content = file.read()
  print(pickle.loads(content))
  file.close()