"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

listNumbers = []

for n in range(1,51):
  if n%2 == 0:
    listNumbers.append(f"{n} - par")
  else:
    listNumbers.append(f"{n} - impar")

with open("numbers.txt", "w") as file:
  for number in listNumbers:
    file.write(number + '\n')
  file.close()