import random

print("Bem vindo ao cara ou coroa")

moeda_aleatoria = random.randint(0, 1)
if moeda_aleatoria == 1:
	print("Deu Cara")
else: 
	print("Deu Coroa")