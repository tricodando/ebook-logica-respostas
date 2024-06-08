"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

name = input()

match name:
  case "Steve":
    print(f"Ola, {name}!")
  case "Bob":
    print(f"Ola, {name}!")
  case "Alice":
    print(f"Ola, {name}!")
  case "Jane":
    print(f"Ola, {name}!")
  case _:
    print(f"Desculpa, você não foi convidado!")