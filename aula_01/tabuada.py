# ----------Tabuada-----------

numero = int(input("\nQual tabuada você quer? ")) 
# int == números inteiros | float == Números de ponto flutuante (ex: 54.3):

print (f"\n--- Tabuada do {numero} ---")

for i in range(1,21):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")