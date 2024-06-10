"""
autor: Reuel Caetano
título: Lógica de Programação
subtítulo: Programando de forma moderna com Python 3
instruções: Crie um arquivo para o algoritmo
"""

message = "Oi,$Maria!#Estou@enviando@essa mensagem$para@avisar#que@amanhã$a@aula#será$ao$ar@livre."

def clearMessage(msg):
  clear = ''
  for char in msg:
    if char in '@#$':
      clear += ' '
    else:
      clear += char
  return clear

print(clearMessage(message))