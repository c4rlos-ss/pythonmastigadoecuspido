import os


soma = 0
contador = 0
while True:
    nota = float(input(f"insira {contador + 1} nota: "))

    contador = contador + 1
    soma = nota + soma
    media = 0
    print("=== MENU ===")
    print("S - INSERIR MAIS UMA NOTA")
    print("P - VER QUANTAS NOTAS FORAM INSERIDAS")
    print("N - CALCULAR A MÉDIA ARIMÉTRICA DAS NOTAS INFORMADAS")
    desejo = input("\n QUAL AÇÃO VOÇE DESEJA REALIZAR: ")

    if desejo == 's':
        os.system("clear")
    elif desejo == 'p':
        print(f"a quantidade de notas inseridas foram: {contador}")
        break
    elif desejo == 'n':
        media = soma / contador  
        print(f"a media foi: {media}")
        break
    else: 
        break

        