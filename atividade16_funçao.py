
def calcular(operador, n1, n2):
    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2
    elif operador == "/":
        return n1 / n2
    elif operador == "*":
        return n1 * n2
    else:
        return print("error")

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))

operador = input("deseja utilizar qual operador aritimetico: ")
 
resultado = calcular(operador, n1, n2)

print(resultado)
