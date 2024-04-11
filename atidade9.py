nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))


if idade == 16 or idade == 17 or idade >= 65:
    print("Você pode votar, mas não é obrigado")
elif idade >= 18:
    print("Você é obrigado a votar")

elif idade < 1:
    print("Você não é obrigado a votar")

