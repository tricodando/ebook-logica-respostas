"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def footer(func):
  def wrapper():
    print(func())
    print("Obrigado pela preferência!")
  return wrapper

@footer
def message():
  return "Você adquiriu um ótimo livro de lógica de programação."

message()