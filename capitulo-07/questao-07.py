"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

age = int(input())
if age < 16:
  print("Não pode votar!")
elif age == 16 or age == 17 or age >= 70:
  print("Voto facultativo!")
elif age >= 18 and age < 70:
  print("Voto obrigatório!")