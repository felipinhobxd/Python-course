print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')
print("Bem vindo a caça ao tesouro maluca!")
print("Sua missão é encontrar o tesouro!")
esquerda_ou_direita = input("Tem um caminho na sua frente, você quer ir para a (direita) ou (esquerda)?\n")
if esquerda_ou_direita == "esquerda":
    nadar_ou_esperar = input("Tem um rio do seu lado, você quer (nadar) ou só (esperar) algo acontecer?\n")
    if nadar_ou_esperar == "esperar":
        qual_porta = input("Apareceu três portas magicamente na sua frente, uma (vermelha), uma (amarela) e outra (azul), qual você quer ir?\n")
        if qual_porta == "azul":
            print("VOCÊ VENCEU PARABENS! AQUI ESTÁ SEU PREMIO:")
            print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`''')
        elif qual_porta == "vermelha":
            print("VOCÊ ABRE E UM DEMONIO DE PUXA PARA UM FORNO A 1000°C, FIM DE JOGO!")
        else:
            print("VOCÊ ABRE A PORTA AMARELA, E SAI UM MALUCO PELADO COM UMA PEXEIRA E TE MATA, FIM DE JOGO!")
    else:
        print("VOCÊ SE AFOGOU, POIS NÃO SABIA NADAR, FIM DE JOGO!")
else:
    print("VOCÊ TROPEÇOU E CAIU, FIM DE JOGO!")