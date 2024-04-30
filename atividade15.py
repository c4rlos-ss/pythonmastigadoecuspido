notas = []

contador = 1;

while True:
    receber_vetor = int(input(f"escreva o {contador}º numero (inteiros, possitivos, pares): "))
                              
    if receber_vetor >= 0 and receber_vetor % 2 == 0:
        notas.append(receber_vetor)
        contador += 1
    else:
        print("tipo de numero invalido escreva novamnete ")

    if contador == 6:
        break
    
notas.reverse()

for i in range(len(notas)):
    print(f"aqui esta a lista dos numeros escritos em ordem inversa: {notas[i]}\n")