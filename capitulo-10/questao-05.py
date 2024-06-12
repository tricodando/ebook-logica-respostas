"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

listName = []

while True:
  name = input("Digite um nome: ")
  if name == "":
    break
  listName.append(name)

with open("list.txt", "w") as file:
  for name in listName:
    file.write(f"{name}\n")
  file.close()