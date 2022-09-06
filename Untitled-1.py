print("-" *18)
print("TABUADA ATIVIDADE")
print("-" *18)


num = int(input("digite aqui o número inteiro para ver a tabuada: "))
for c in range(1, 11):
  print("{} x {:2} = {}".format(num, c, num*c))
print("-" *18)