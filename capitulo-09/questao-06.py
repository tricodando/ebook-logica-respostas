"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def txtUpper(func):
  def wrapper():
    txt = func()
    print(txt.upper())
  return wrapper

@txtUpper
def message():
  return "transforma o texto com decorator"

message()