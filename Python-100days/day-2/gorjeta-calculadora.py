print("Bem vindo a calculadora de gorjeta!")
conta = float(input("Quanto foi a conta? R$"))
gorjeta = int(input("Quanto de gorja você vai dar?\n"))
dividir = int(input("Quantas pessoas vão dividir a conta?\n"))
# Pega a porcentagem e ja calcula com o valor da conta
gorjeta_porcentagem = gorjeta / 100 + 1 
# Ele faz a conta dividido pelo total de pessoas e dai só faz quanto deu a conta +  porcentagem de gorjeta
quanto_pagar = (conta / dividir) * gorjeta_porcentagem 
print(f"Cada pessoa vai pagar: R${quanto_pagar:.3}")