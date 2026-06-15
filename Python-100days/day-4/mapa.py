linha1 = ["⬜", "⬜", "⬜"]
linha2 = ["⬜", "⬜", "⬜"]
linha3 = ["⬜", "⬜", "⬜"]
mapa = [linha1, linha2, linha3]

print("O X marca onde seu tesouro será escondido")
print(f"\n{linha1}\n{linha2}\n{linha3}")

posicao = input("Onde quer esconder seu tesouro? A1, A2, A3, B1, B2, B3, C1, C2 ou C3\n")
posicao_real = posicao.lower()

letra = posicao_real[0]
numero = posicao_real[1]

if letra == "a":
    coluna = 0
elif letra == "b":
    coluna = 1
else:
    coluna = 2

if numero == "1":
    linha = 0
elif numero == "2":
    linha = 1
else: 
    linha = 2

mapa[linha][coluna] = "❌"
print(f"\n{linha1}\n{linha2}\n{linha3}")