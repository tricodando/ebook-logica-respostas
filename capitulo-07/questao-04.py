"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

score1 = float(input())
score2 = float(input())
score3 = float(input())
average = (score1 + score2 + score3) / 3
if average < 5 and average >= 0:
  print("REPROVADO!")
elif average >= 5 and average < 7:
  print("RECUPERAÇÃO!")
elif average >= 7 and average <= 10:
  print("APROVADO!")
else:
  print("Média fora do intervalo")