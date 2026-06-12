print("Bem vindo a calculador do AMOR!")
nome1 = input("Qual seu nome?\n")
nome2 = input("Qual o nome da sua crush/namorada?\n") 
nomes_combinados = nome1.lower() + nome2.lower() 
quantidade_somada_true = nomes_combinados.count("t") + nomes_combinados.count("r") + nomes_combinados.count("u") + nomes_combinados.count("e")
quantidade_somada_love = nomes_combinados.count("l") + nomes_combinados.count("o") + nomes_combinados.count("v") + nomes_combinados.count("e")
true_total = str(quantidade_somada_true)
love_total = str(quantidade_somada_love)
total_real = true_total + love_total
if int(total_real) < 10 or int(total_real) > 90:
    print(f"Sua pontuação é {total_real}, vocês combinam como coca e mentos.")
elif int(total_real) >= 40 and int(total_real) <=50:
    print(f"Sua pontuação é {total_real}, vocês dão para o gasto juntos.")
else:
    print(f"Sua pontuação é {total_real}")