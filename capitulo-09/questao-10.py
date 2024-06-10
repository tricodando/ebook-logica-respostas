"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def cash(value):
  c100 = (value // 100)
  c50 = ((value % 100) // 50)
  c20 = (((value % 100) % 50) // 20)
  c10 = ((((value % 100) % 50) % 20) // 10)
  c5 = (((((value % 100) % 50) % 20) % 10) // 5)
  c2 = ((((((value % 100) % 50) % 20) % 10) % 5) // 2)
  c1 = (((((((value % 100) % 50) % 20) % 10) % 5) % 2) // 1)
  
  print(f"{c100:.0f} x 100")
  print(f"{c50:.0f} x 50")
  print(f"{c20:.0f} x 20")
  print(f"{c10:.0f} x 10")
  print(f"{c5:.0f} x 5")
  print(f"{c2:.0f} x 2")
  print(f"{c1:.0f} x 1")

value = float(input("Digite o valor: "))
cash(value)