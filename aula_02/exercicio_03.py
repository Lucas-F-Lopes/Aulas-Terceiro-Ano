# 03
# Escreva um programa de lista de compras onde o programa: 
# - Peça o nome de qual fruta você gostaria de adicionar a lista
# - Adicione o ítem a uma lista vazia
# - SE o usuário digitar "Fim", mostre todos os ítens listados

# frutas = []

# while True:
#     fruta = input ('Qual fruta você gostaria de adicionar a lista?\n')
#     if fruta.lower() == "fim": 
#         break
#     adicionar_lista = str(fruta) # STR string 
#     frutas.append(adicionar_lista)

# print

frutas = []

print("=== Lista de Compras de Frutas ===")
print("Digite o nome para cada fruta que deseja adicionar na lista.")
print("Digite 'fim' para encerrar.\n")

while True:
    fruta = input("Qual fruta você gostaria de adicionar a lista?")
    fruta = fruta.strip()

    if fruta.lower() == "fim":
        break

    if fruta =="":
        print("Você não digitou nenhuma fruta. Tente novamente.")
        continue
    
    frutas.append(fruta)

    print(f"{fruta} foi adicionado a lista!\n")

print("\n === Lista final de compras ===")

if len(frutas) == 0:
    print ("Nenhuma fruta foi adicionada.")
else:
    for numero, fruta in enumerate(frutas,start=1):
        print(f"{numero}.{fruta}")

print(frutas)