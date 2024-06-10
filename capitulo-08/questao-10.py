"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

colors = {
  "blue": "azul",
  "orange": "laranja",
  "black": "preto",
  "yellow": "amarelo",
  "white": "branco"
}

while True:
  color = input("Digite um nome em inglês do dicionário: ")
  if color == "exit":
    break
  else:
    print(colors[color])