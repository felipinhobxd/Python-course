a = input()
b = input()
# isso só troca os valores de a e b em uma memoria, não tem nada a ver com o conteúdo de a e b
caixa = a
a = b
b = caixa
print("a: " + a)
print("b: " + b)