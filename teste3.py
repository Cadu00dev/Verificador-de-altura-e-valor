print("bem vindo a montanha russa!")

altura = int(input("qual é sua altura?\n"))

if altura > 120:
    print("bem vindo!")  
    idade = int(input("qual é sua idade?\n"))
    if idade >= 18:
        print("o valor do ingresso sera de 12")
    elif idade >12 <18:
        print("o valor do ingresso sera de 9")
    else:
        print("o valor do ingresso sera de 7")
else:
    print("precisa crescer mais!")
