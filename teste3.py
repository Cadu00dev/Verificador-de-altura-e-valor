print("bem vindo a montanha russa!")

altura = int(input("qual é sua altura?\n"))
conta = 0

if altura > 120:
    print("bem vindo!")  
    idade = int(input("qual é sua idade?\n"))
    if idade < 12:
        conta = 7
        print("o valor do ingresso sera de 7$")
    elif idade >12 >18:
        conta = 9
        print("o valor do ingresso sera de 9$")
    elif idade >= 45 and idade <=55:
        print("sua conta sera gratuita!") 
    else:
        conta = 12
        print("o valor do ingresso sera de 12$")
    fotos = input("Voce deseja adicionar fotos ao seu ingresso? Sim ou Nao\n")
    if fotos == "Sim":
        conta += 3
    print(f"O valor total da sua conta sera {conta}$")
else:
    print("preisa crescer mais!")
