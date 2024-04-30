
n1 = 0
n2 = 0
operador = "0"

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
        print("operador invalido, tente novamente: ")
        return

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))

operador = input("deseja utilizar qual operador aritimetico: ")

calcular(operador, n1, n2)
print(f"o valor da soma foi {(n1 + n2) / 2}")