"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

year = int(input("Informe um ano: "))
bissexto = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
if bissexto:
  print("É bissexto!")
else:
  print("Não é bissexto!")