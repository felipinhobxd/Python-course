altura = input("Digite sua altura em metros:\n")
peso = input("Digite seu peso em quilos:\n")
imc = float(peso) / float(altura) ** 2
print(imc)

if imc < 18.5:
    print("Você é o Jonathan!")
elif imc < 25:
    print("Você ta normal!")
elif imc < 30:
    print("Você ta ligeiramente acima do peso!")
elif imc < 35:
    print("Você está obeso!")
else:
    print("Você ta com obesidade morbida!")