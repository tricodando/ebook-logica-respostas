"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

import pickle


class Manager:
  def __init__(self):
    self.FILE_NAME = "data.db"
    self.db = []
    try:
      self.opendb()
    except:
      self.writedb()
      self.opendb()
  
  def opendb(self):
    with open(self.FILE_NAME, "rb") as file:
      content = file.read()
      self.db = pickle.loads(content)
      file.close()
  
  def writedb(self):
    with open(self.FILE_NAME, "wb") as file:
      file.write(pickle.dumps(self.db))
      file.close()

  def create(self, obj: dict) -> None:
    for register in self.db:
      if register['id'] == obj['id']:
        return
    self.db.append(obj)
    with open(self.FILE_NAME, "wb") as file:
      file.write(pickle.dumps(self.db))
      file.close()

  def find(self, id: str = '') -> list:
    if (id == ''):
      print(self.db)
    else:
      for register in self.db:
        if register['id'] == id:
          print([register])

  def update(self, obj: dict) -> None:
    self.delete(obj['id'])
    self.create(obj)

  def delete(self, id: str) -> None:
    for register in self.db:
      if register['id'] == str(id):
        self.db.remove(register)
        with open(self.FILE_NAME, "wb") as file:
          file.write(pickle.dumps(self.db))
          file.close()

db = Manager()
db.create({
  'id': '1',
  'description': 'Hamburger',
  'category': 'Food',
  'amount': 10,
  'price': 20.0,
  'cost': 12.0
})
db.find()