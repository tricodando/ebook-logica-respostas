"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

import pickle

pessoa = {
  "id": "1",
  "nome": "Fulano",
  "sobrenome": "de Tal"
}

with open("data.db", "wb") as file:
  file.write(pickle.dumps(pessoa))
  file.close()