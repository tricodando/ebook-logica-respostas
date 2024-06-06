"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

number1 = input()
number2 = input()
number1_replace = number1.replace(',','.')
number2_replace = number2.replace(',','.')
print(float(number1_replace) + float(number2_replace))