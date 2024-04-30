nota = []

for i in range(5):
    notas = int(input(F"digite a {i + 1}ª nota: "))
    if notas < 0:
        notas = 0

    nota.append(notas)
    
print(nota)