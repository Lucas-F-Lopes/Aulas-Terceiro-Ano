notas = []   # começamos fazendo uma lista

print("/n Digite as notas ( ou 'fim' para encerrar)")

while True:
    entrada = input ("Nota: ")

    if entrada.lower() == "fim": # .lower deixa toda a informação da variável em minúsculo
        break
# CTRL + C: Força o programa a parar
    nota = float(entrada)
    notas.append(nota)

if len(notas) == 0: # len é tudo aquilo que tem dentro da variável, mas contando em quantidade
    print("Nenhuma nota digitada.")
else:
    media = sum(notas) / len(notas)
    maior = max(notas) 
    menor = min(notas)

print(f"\n ----- RESULTADO -----")
    
print(f"Quantidade : {len(notas)}")
print(f"Média      : {media:.2f}")
print(f"Maior nota : {maior}")
print(f" Menor nota: {menor}")

if media >= 7:
    print(" Situação: APROVADO!")
else:
    print("Situação: REPROVADO!")