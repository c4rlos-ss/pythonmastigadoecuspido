parar = 'n'
contador = 0
nota = 0
soma = 0
while True:
    if contador >= 1:
         parar = input("deseja parar (s ou n)? ")

    if parar == 's':
        contador = contador + 1
    else:
        break

    nota = float(input(f"digite sua {contador}ª nota: "))
    soma = nota + soma 

media = soma / contador 
print(f"sua media foi: {media}")