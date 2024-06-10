"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

def carLocator(typeof, days):
  options = {
    'basic': 20,
    'medium': 40,
    'premium': 80
  }
  value = f"Valor Total: R$ {options[typeof] * days:.2f}"
  return value

print("== Boas vindas a locadora de carros! ==")
typeof = input("Digite um tipo [basic, medium, premium]: ")
days = int(input("Digite a quantidade de dias para a locação: "))
print(carLocator(typeof, days))