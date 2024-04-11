import os

loginOK = "carlos123"
senhaOK = "123"

login = "ola"
senha = "321"

while(login != loginOK or senha != senhaOK): 
    login = input("Qual o seu login: ")
    senha = input("Qual a sua senha: ") 
    os.system("cls || clear")
    if login != loginOK or senha != senhaOK:
        print("Usuário ou senha inválidos, tente novamente!!")
    else:
        print("Seja bem-vindo ao portal aluno SENAI")
