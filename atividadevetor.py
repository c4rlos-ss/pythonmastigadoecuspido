nota = []
numeros = 0
numeorosN = 0
soma = 0

for i in range(10):
    notas = float(input(f"digite a {i + 1}ª nota: "))
    nota.append(notas)

    if notas < 0:
        numeorosN = numeorosN + 1
    else:
        soma = notas + soma

print(f"a quantidade de numeros negativos escritos foi: {numeorosN}")
print(f"a soma dos numeros possitivos foi +{soma}")