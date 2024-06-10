"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def IMC(peso, altura):
  imc = peso/(altura * altura)
  return imc

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

print(IMC(peso, altura))