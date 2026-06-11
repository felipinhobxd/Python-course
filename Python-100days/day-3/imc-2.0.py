altura = input("Digite sua altura em metros:\n")
peso = input("Digite seu peso em quilos:\n")
imc = float(peso) / float(altura) ** 2
if imc < 18.5:
    print(f"seu imc é {imc}, Você é o Jonathan!")
elif imc < 25:
    print(f"seu imc é {imc}, Você ta normal!")
elif imc < 30:
    print(f"seu imc é {imc}, Você ta ligeiramente acima do peso!")
elif imc < 35:
    print(f"seu imc é {imc}, Você está obeso!")
else:
    print(f"seu imc é {imc}, Você ta com obesidade morbida!")