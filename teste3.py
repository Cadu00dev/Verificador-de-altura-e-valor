print("bem vindo a montanha russa!")

altura = int(input("qual é sua altura?\n"))

if altura > 120:
    print("bem vindo!")  
    idade = int(input("qual é sua idade?\n"))
    if idade >= 18:
        conta = 12
        print("o valor do ingresso sera de 12")
    elif idade >12 <18:
        conta = 9
        print("o valor do ingresso sera de 9")
    else:
        conta = 7
        print("o valor do ingresso sera de 7")
    fotos = input("Voce deseja adicionar fotos ao seu ingresso? Sim ou Nao\n")
    if fotos == "Sim":
        conta += 3
    print(f"O valor total da sua conta sera {conta}")
else:
    print("preisa crescer mais!")
