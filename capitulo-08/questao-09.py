"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

while True:
  n1 = int(input("Digite um número: "))
  if n1 == 0:
    break  
  n2 = int(input("Digite um número: "))
  if n1 > n2:
    print(f"{n1}>")
  elif n2 > n1:
    print(f"{n2}>")
  elif n1 == n2:
    print("Os números são iguais!")