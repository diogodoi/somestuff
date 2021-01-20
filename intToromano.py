'''
I = 1
IV = 4
V= 5
IX = 9
X = 10
L = 50
C = 100
D = 500
M = 1000
'''

val_roman = ["I","IV","V","IX","X","L","C","D","M"]

val_int = [1,4,5,9,10,50,100,500,1000]

x = zip(val_roman,val_int)

def unidades(value):    
    if value < 4:
      return str(value*"I")
    elif value == 4:
      return str("IV")
    elif value == 9:
      return str("IX")
    elif value >= 5:
      return str("V"+ (value-5)*"I")

def dezenas(value):
  
  if value <= 3:
    return str(value*"X")
  elif value == 4:
    return str("XL")
  elif value ==9:
    return str("XC")
  elif value >= 5:
    return str("L" + (value - 5)*"X")

def centenas(value):
  
  if value <= 3:
    return str(value*"C")
  elif value == 4:
    return str("CD")
  elif value == 9:
    return str("CM")
  elif value >= 5:
    return str("D" + (value - 5)*"C")
    
def milhares(value):  
  if value <= 3:
    return str(value*"M")
 

def transform(value):
  
  string = str(value)
  for i,j in x:
    if value == j:
      return str(i)
  if len(string) == 1:
    return str(unidades(value))

  elif len(string) == 2:
    dezena = []
    for i in string:
      dezena.append(int(i))    
    return str(dezenas(dezena[0])+unidades(dezena[1]))      

  elif len(string) == 3:
    centena = []
    for i in string:      
      centena.append(int(i))
    return str(centenas(centena[0])+dezenas(centena[1])+unidades(centena[2]))   

  else:
    milhar = []
    for i in string:
      milhar.append(int(i))
    return str(milhares(milhar[0])+centenas(milhar[1])+dezenas(milhar[2])+unidades(milhar[3]))
    
print("Digite um número inteiro para ser convertido: ")
valor = int(input())
if valor > 3999:
  print("Não é possivel escrever esse valor. Devido a falta de representação.")
else:
  string = str(valor)
  roman = transform(valor)
  print(f"O valor inteiro {valor} em Romano fica "+ roman)
