"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

FILE_NAME = "data.db"

try:
  with open(FILE_NAME, "r") as file:
    content = file.read()
    file.close()
except:
  with open(FILE_NAME, "w") as file:
    file.close()