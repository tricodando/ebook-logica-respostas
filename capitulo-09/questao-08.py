"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def counter(n):
  if n > 10:
    return
  print(n)
  counter(n+1)

counter(0)