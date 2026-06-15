import random

nomes = ["Felipe", "Gustavo", "Nathan", "Jonathan", "João que rouba", "João femboy"]
nomes_separados = len(nomes)
nomes_aleatorios = random.randint(0, nomes_separados - 1)
quem_pagar = nomes[nomes_aleatorios]
print(f"{quem_pagar} vai pagar a conta, R$: 1.000.000,00")