numero = int(input("Qual será o numero que você irá digitar? num. max 1000\n"))
soma = 0
for i in range(1, numero+1, 2):
    soma += i
print(f"A SOMA DOS IMPARES ENTRE 1-{numero} são: {soma}")
soma = 0
for i in range(0, numero+1, 2):
    soma += i
print(f"A SOMA DOS PARES ENTRE 1-{numero} são: {soma}")