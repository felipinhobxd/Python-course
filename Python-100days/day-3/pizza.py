print("pizzaria da resenha, escolha sua pizza ")
valortotal = 0
tamanho = input("qual o tamanho? p $15, m $20 ou g $25\n")
peperoni = input("aceita adicional de peperoni? s ou n\n")
queijo= input("aceita adicional de queijo? s ou n\n")
if tamanho == "p":
    valortotal += 15
elif tamanho == "m":
    valortotal += 20
else: 
    valortotal += 25
if peperoni == "s":
    if tamanho == "p":
        valortotal += 2
    else:
        valortotal += 3
if queijo == "s":
    valortotal += 1
print(f"Sua conta deu:{valortotal}")