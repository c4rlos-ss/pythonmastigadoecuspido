nome = input("qual seu nome: ")
nota1 = int(input("qual foi sua nota na primeira unidade: "))
nota2 = int(input("qual foi sua nota na segunda unidade: "))

soma = (nota1 + nota2 ) 
media = soma / 2
produto = nota1 * nota2

print(f"\naqui estao os dados do launo {nome}")
print(f"\n a media foi: max{media}")
print(f"\n a soma foi: {soma}")
print(f"\n o produto foi: {produto}")
print(f"\n o menor numero digitado foi: {max(nota1,nota2)}")
print(f"\n o maior numero digitado foi: {min(nota1,nota2)}")