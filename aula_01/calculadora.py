print("=====CALCULADORA=====")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Operação ( +, -, *, /): ")
# print(a,b)
# print(op)

if op =="+":
    resultado = a + b
elif op == "-":
    resultado = a - b
elif op == "*":
    resultado = a * b
elif op =="/":
    if b == 0:
        resultado = " Erro: divisão por zero"
    else:
        resultado = a / b
else:
    resultado = "Operação inválida."

print(f"Resultado: {resultado}") # f é uma forma de formatação