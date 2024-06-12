"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

while True:
  try:
    a = int(input("Digite um número: "))
    print (a * a)
  except:
    print("Número inválido!")
    raise ValueError