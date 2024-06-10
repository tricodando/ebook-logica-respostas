"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def fibonnacci(n):
  if n <= 1:
    return n
  return fibonnacci(n-1) + fibonnacci(n-2)

for i in range(21):
  print(fibonnacci(i))