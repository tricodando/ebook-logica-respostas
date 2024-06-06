"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

sizes = ["P", "M", "G"]
products = ["Calca", "Camisa", "Vestido"]
print([(s,p) for s in sizes for p in products])