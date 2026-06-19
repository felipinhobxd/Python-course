import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Gerador de Senhas em Python!")
nr_letras = int(input(f"Quantas letras você gostaria de ter na sua senha?\n"))
nr_simbolos = int(input(f"Quantos símbolos você gostaria de ter?\n"))
nr_numeros = int(input(f"Quantos números você gostaria de ter?\n"))

lista_senha = []
for i in range(nr_letras):
    letras_aleatorias = random.choice(letras)
    lista_senha.append(letras_aleatorias)
for i in range(nr_numeros):
    numeros_aleatorios = random.choice(numeros)
    lista_senha.append(numeros_aleatorios)
for i in range(nr_simbolos):
    simbolos_aleatorios = random.choice(simbolos)
    lista_senha.append(simbolos_aleatorios)
random.shuffle(lista_senha)
senha_final = "".join(lista_senha)
print(f"A SUA SENHA NOVA É: {senha_final}")