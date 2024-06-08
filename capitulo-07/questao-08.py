"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

day = int(input())

match day:
  case 0:
    print("Domingo")
  case 1:
    print("Segunda")
  case 2:
    print("Terça")
  case 3:
    print("Quarta")
  case 4:
    print("Quinta")
  case 5:
    print("Sexta")
  case 6:
    print("Sábado")
  case _:
    print("Dia não encontrado!")