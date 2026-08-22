notas_estudantes = input("Digite as notas, separando cada uma com um espaço (" ")\n").split()
for n in range(0, len(notas_estudantes)):
    notas_estudantes [n] = int(notas_estudantes [n])
nota_maior = 0
for i in notas_estudantes:
    if i > nota_maior:
        nota_maior = i
print(f"A maior nota é: {nota_maior}")
