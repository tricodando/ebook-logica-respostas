"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

total = float(input("Informe o valor: "))
print(f"À vista: R${total-(total*0.15)}")
print(f"Parcelado em 1x de R${(total+(total*0.02))/1:.2f}")
print(f"Parcelado em 2x de R${(total+(total*0.04))/2:.2f}")
print(f"Parcelado em 3x de R${(total+(total*0.06))/3:.2f}")
print(f"Parcelado em 4x de R${(total+(total*0.08))/4:.2f}")
print(f"Parcelado em 5x de R${(total+(total*0.10))/5:.2f}")
print(f"Parcelado em 6x de R${(total+(total*0.12))/6:.2f}")
