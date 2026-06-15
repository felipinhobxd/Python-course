linha1 = ["⬜", "⬜", "⬜"]
linha2 = ["⬜", "⬜", "⬜"]
linha3 = ["⬜", "⬜", "⬜"]
mapa = [linha1, linha2, linha3]

print("O X marca onde seu tesouro será escondido")
print(f"\n{linha1}\n{linha2}\n{linha3}")

posicao = input("Onde quer esconder seu tesouro? A1, A2, A3, B1, B2, B3, C1, C2 ou C3\n")
letra = posicao[0].lower()
abc = ["a", "b", "c"]
letra_index = abc.index(letra)
numero_index = int(posicao[1]) - 1

mapa[letra_index][numero_index] = "❌"

print(f"\n{linha1}\n{linha2}\n{linha3}")