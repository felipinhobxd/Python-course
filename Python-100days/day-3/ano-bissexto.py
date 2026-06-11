ano = int(input("Qual ano você que sabe que é bissexto?\n"))
if ano % 4 == 0:
    if ano % 100 == 0:
        print("É BISSEXTO")
    elif ano % 400 == 0:
        print("É BISSEXTO!")
    else:
        print("NÃO É BISSEXTO!")       
else:
    print("NÃO É BISSEXTO!")