import random
pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
jogo_imagens = [pedra, papel, tesoura]
escolha = int(input("0 PARA PEDRA, 1 PARA PAPEL, 2 PARA TESOURA"))
if escolha >=3 and escolha < 0:
    print("NÃO É UM NUMERO VALIDO!")
else:  
    print(jogo_imagens[escolha])
    robo_escolha = random.randint(0,2)
    print(jogo_imagens[robo_escolha])
    if escolha == 0 and robo_escolha == 2:
        print("VOCÊ GANHOU!")
    elif robo_escolha == 0 and escolha == 2:
        print("VOCÊ PERDEU")
    elif robo_escolha > escolha:
        print("VOCÊ PERDEU!")
    elif escolha > robo_escolha:
        print("VOCÊ GANHOU!")
    else:
        print("EMPATE")