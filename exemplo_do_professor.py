nota = []

while True:
    notas = float(input("Digite a nota do aluno: "))
    nota.append(notas)

    continuar = input("Deseja digitar outra nota? (s/n): ") 
    if continuar.lower() != "s":
        break

for i in range(len(nota)):
    print(f"{i+1] nota: (notas[i])")