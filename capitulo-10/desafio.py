"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

import pickle


FILE_NAME = "data.db"
db = []
try:
  with open(FILE_NAME, "rb") as file:
    content = file.read()
    db = pickle.loads(content)
    file.close()
except:
  with open(FILE_NAME, "wb") as file:
    file.write(pickle.dumps(db))
    file.close()
  with open(FILE_NAME, "rb") as file:
    content = file.read()
    db = pickle.loads(content)
    file.close()

def create(obj: dict) -> None:
  for register in db:
    if register['id'] == obj['id']:
      return
  db.append(obj)
  with open(FILE_NAME, "wb") as file:
    file.write(pickle.dumps(db))
    file.close()

def find(id: str = '') -> list:
  if (id == ''):
    print(db)
  else:
    for register in db:
      if register['id'] == id:
        print([register])

def update(obj: dict) -> None:
  delete(obj['id'])
  create(obj)

def delete(id: str) -> None:
  for register in db:
    if register['id'] == id:
      db.remove(register)
      with open(FILE_NAME, "wb") as file:
        file.write(pickle.dumps(db))
        file.close()

create({'id':'1', 'name':'joe'})
create({'id':'2', 'name':'janet'})
create({'id':'3', 'name':'smith'})
find()

# update({'id':'1', 'name':'joe doe'})
# delete('2')
# find()